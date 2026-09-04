#!/usr/bin/env python3
"""Render an HWP document to deterministic pNN.png evidence pages on Windows."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import tempfile

import pymupdf
import pythoncom
import win32com.client


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def export_pdf(source: pathlib.Path, destination: pathlib.Path) -> None:
    pythoncom.CoInitialize()
    hwp = None
    try:
        hwp = win32com.client.gencache.EnsureDispatch("HWPFrame.HwpObject")
        registered = hwp.RegisterModule(
            "FilePathCheckDLL", "FilePathCheckerModuleExample"
        )
        if not registered:
            raise RuntimeError("HWP FilePathCheckerModule registration failed")
        hwp.SetMessageBoxMode(0x00000001)
        try:
            hwp.XHwpWindows.Item(0).Visible = False
        except Exception:
            pass
        if not hwp.Open(str(source)):
            raise RuntimeError(f"HWP Open returned false: {source}")
        if not hwp.SaveAs(str(destination), "PDF"):
            raise RuntimeError(f"HWP SaveAs(PDF) returned false: {destination}")
        if not destination.is_file() or destination.stat().st_size == 0:
            raise RuntimeError(f"HWP PDF export is missing or empty: {destination}")
    finally:
        if hwp is not None:
            try:
                hwp.Quit()
            except Exception:
                pass
        pythoncom.CoUninitialize()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=pathlib.Path)
    parser.add_argument("output_dir", type=pathlib.Path)
    parser.add_argument("--dpi", type=int, default=160)
    parser.add_argument("--expected-pages", type=int)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve(strict=True)
    if source.suffix.lower() != ".hwp":
        raise SystemExit(f"source must be .hwp: {source}")
    if args.dpi < 72 or args.dpi > 600:
        raise SystemExit("dpi must be between 72 and 600")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix="hwp-render-", dir=output_dir.parent
    ) as temporary:
        temporary_dir = pathlib.Path(temporary)
        pdf = temporary_dir / "source.pdf"
        export_pdf(source, pdf)
        document = pymupdf.open(pdf)
        try:
            page_count = len(document)
            if args.expected_pages is not None and page_count != args.expected_pages:
                raise RuntimeError(
                    f"page count mismatch: expected={args.expected_pages} observed={page_count}"
                )
            staged: list[pathlib.Path] = []
            for index, page in enumerate(document, start=1):
                target = output_dir / f"p{index:02d}.png"
                if target.exists() and not args.force:
                    raise FileExistsError(f"refusing to overwrite without --force: {target}")
                staged_page = temporary_dir / target.name
                pixmap = page.get_pixmap(dpi=args.dpi, alpha=False)
                pixmap.save(staged_page)
                if staged_page.stat().st_size == 0:
                    raise RuntimeError(f"rendered page is empty: {staged_page}")
                staged.append(staged_page)
        finally:
            document.close()

        outputs = []
        for staged_page in staged:
            target = output_dir / staged_page.name
            os.replace(staged_page, target)
            outputs.append(
                {
                    "path": str(target),
                    "bytes": target.stat().st_size,
                    "sha256": sha256(target),
                }
            )

    print(
        json.dumps(
            {
                "source": str(source),
                "source_sha256": sha256(source),
                "dpi": args.dpi,
                "rendered_pages": len(outputs),
                "outputs": outputs,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
