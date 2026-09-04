#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tools/textpatch.py - line-ending-agnostic anchored text patching.

WHY THIS EXISTS (260902)
------------------------
CRLF misjudgment recurred three times in a single session. Every occurrence had the
same shape: an anchored multi-line edit was written with LF anchors while the target
file was CRLF, so the anchor did not match. The mitigation adopted after the first two
was a *discipline* rule ("check the file's line endings first") - and it failed
immediately, because the check itself was wrong: `grep -c` for a carriage return
reports 0 on a CRLF file (grep strips CR before matching), which reads as "this file
is LF".

A rule that must be remembered is not a fix. This module removes the decision
entirely: anchors are always written in LF, matching always happens on an
LF-normalized copy, and the file is written back with the line ending and BOM it
already had. There is nothing left to detect, so there is nothing left to get wrong.

CLAUDE.md 원칙 12-b: the ruler is made by code, not by hand.

USE
---
    import sys; sys.path.insert(0, "tools")
    from textpatch import patch, insert_before, append_row

    patch("CLAUDE.md", [(old, new)])          # anchors always written in LF
    insert_before("a.md", "## Section", block)
    append_row("analysis/REV_LOG.md", row)    # verifies column count vs header

Every function validates before writing, so a failed call leaves the target
byte-identical.

Self-test (proves detection power, CLAUDE.md 원칙 12-d):
    python tools/textpatch.py --self-test
"""
import io
import os
import sys

BOM = b"\xef\xbb\xbf"


class PatchError(Exception):
    """Raised before any write happens, so the target is never left damaged."""


def read(path):
    """Return (lf_text, newline, had_bom, stats). Never guesses from grep."""
    raw = io.open(path, "rb").read()
    had_bom = raw.startswith(BOM)
    txt = (raw[len(BOM):] if had_bom else raw).decode("utf-8")
    crlf = txt.count("\r\n")
    lf_only = txt.count("\n") - crlf
    cr_only = txt.count("\r") - crlf
    stats = {"crlf": crlf, "lf": lf_only, "cr": cr_only, "bom": had_bom}
    newline = "\r\n" if crlf > 0 and crlf >= lf_only else "\n"
    return txt.replace("\r\n", "\n"), newline, had_bom, stats


def write(path, lf_text, newline, had_bom):
    out = lf_text.replace("\n", newline) if newline == "\r\n" else lf_text
    data = out.encode("utf-8")
    if had_bom:
        data = BOM + data
    io.open(path, "wb").write(data)


def _norm(s):
    return s.replace("\r\n", "\n")


def _check_mixed(path, stats, newline, allow_mixed):
    """Mixed line endings: refuse by default (CLAUDE.md 원칙 11, fail-closed).

    260902: this used to print [WARN] and write anyway. A check whose result changes
    nothing is not a check - and this one is not cosmetic: writing a mixed-ending file
    back under a single convention rewrites EVERY line that used the other one, so a
    one-anchor edit silently becomes a whole-file rewrite. The caller that genuinely
    wants that normalization now has to say so with allow_mixed=True and owns the diff.
    """
    if not (stats["crlf"] and stats["lf"]):
        return
    as_ = "CRLF" if newline == "\r\n" else "LF"
    if not allow_mixed:
        sys.stderr.write(
            "[FAIL] %s has mixed line endings (crlf=%d lf=%d); refusing to write.\n"
            "       Writing back as %s would rewrite the %d line(s) using the other\n"
            "       convention. Pass allow_mixed=True to accept that normalization.\n"
            % (path, stats["crlf"], stats["lf"], as_,
               stats["lf"] if as_ == "CRLF" else stats["crlf"]))
        raise PatchError(
            "%s: mixed line endings (crlf=%d lf=%d); refused (allow_mixed=False)"
            % (path, stats["crlf"], stats["lf"]))
    sys.stderr.write(
        "[WARN] %s has mixed line endings (crlf=%d lf=%d); writing back as %s"
        " (allow_mixed=True, caller accepted the normalization)\n"
        % (path, stats["crlf"], stats["lf"], as_))


def patch(path, pairs, expect=1, dry_run=False, allow_mixed=False):
    """Apply (old, new) pairs; each `old` must occur exactly `expect` times."""
    lf_text, newline, had_bom, stats = read(path)
    _check_mixed(path, stats, newline, allow_mixed)
    staged = lf_text
    for i, (old, new) in enumerate(pairs):
        o, n = _norm(old), _norm(new)
        found = staged.count(o)
        if found != expect:
            raise PatchError(
                "%s: pair #%d matched %d time(s), expected %d.\n  anchor: %r"
                % (path, i + 1, found, expect, o[:120]))
        staged = staged.replace(o, n)
    if not dry_run:
        write(path, staged, newline, had_bom)
    return stats


def insert_before(path, anchor, block, dry_run=False, allow_mixed=False):
    """Insert `block` immediately before the single occurrence of `anchor`."""
    return patch(path, [(anchor, block + anchor)], dry_run=dry_run,
                 allow_mixed=allow_mixed)


def insert_after(path, anchor, block, dry_run=False, allow_mixed=False):
    """Insert `block` immediately after the single occurrence of `anchor`."""
    return patch(path, [(anchor, anchor + block)], dry_run=dry_run,
                 allow_mixed=allow_mixed)


def count_cells(row):
    r"""Column count of a markdown row, ignoring escaped pipes.

    260902: `row.count("|")` counted `\|` too. Ledger cells legitimately contain
    escaped pipes (a literal | inside a cell must be written `\|` or it splits the
    row), so a valid 5-column REV_LOG row carrying two of them measured as 7 and was
    refused. The guard was rejecting exactly the rows it exists to protect.
    """
    n = i = 0
    while i < len(row):
        if row[i] == "\\":
            i += 2
            continue
        if row[i] == "|":
            n += 1
        i += 1
    return n - 1


def table_columns(path):
    """Column count of the first markdown table header found, or None."""
    lf_text, _, _, _ = read(path)
    for line in lf_text.split("\n"):
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            return count_cells(s)
    return None


def append_row(path, row, dry_run=False, allow_mixed=False):
    """Append a markdown table row, verifying columns against the table header.

    Second recurring failure of the same family: rows were appended to REV_LOG
    (5 cols) and _index (8 cols) without reading the header, producing malformed
    ledgers. Same fix shape - the check is in the mechanism, not in the operator.
    """
    want = table_columns(path)
    if want is None:
        raise PatchError("%s: no markdown table header found" % path)
    r = _norm(row).rstrip("\n")
    got = count_cells(r)
    if got != want:
        raise PatchError(
            "%s: row has %d columns, header declares %d.\n  row: %r"
            % (path, got, want, r[:120]))
    lf_text, newline, had_bom, stats = read(path)
    _check_mixed(path, stats, newline, allow_mixed)
    if not lf_text.endswith("\n"):
        lf_text += "\n"
    if not dry_run:
        write(path, lf_text + r + "\n", newline, had_bom)
    return want


# --------------------------------------------------------------------------
# Self-test: seed each known failure, prove it is caught (CLAUDE.md 원칙 12-d)
# --------------------------------------------------------------------------
def _self_test():
    import tempfile
    tmp = tempfile.mkdtemp(prefix="textpatch_")
    body = "line one\nline two\n## Section\ntail\n"
    seeded = 0
    caught = 0

    def mk(name, data):
        p = os.path.join(tmp, name)
        io.open(p, "wb").write(data)
        return p

    def only_crlf(raw):
        return b"\n" not in raw.replace(b"\r\n", b"")

    # 1) CRLF file with LF anchors - the failure that recurred three times
    seeded += 1
    p = mk("crlf.md", body.replace("\n", "\r\n").encode("utf-8"))
    patch(p, [("line one\nline two", "LINE ONE\nLINE TWO")])
    raw = io.open(p, "rb").read()
    if b"LINE ONE\r\nLINE TWO" in raw and only_crlf(raw):
        caught += 1
    else:
        print("  FAIL 1: CRLF round-trip not preserved")

    # 2) LF file must not gain CR
    seeded += 1
    p = mk("lf.md", body.encode("utf-8"))
    patch(p, [("line one", "LINE ONE")])
    raw = io.open(p, "rb").read()
    if b"\r" not in raw and b"LINE ONE" in raw:
        caught += 1
    else:
        print("  FAIL 2: LF file gained CR")

    # 3) BOM + CRLF preserved together
    seeded += 1
    p = mk("bom.md", BOM + body.replace("\n", "\r\n").encode("utf-8"))
    patch(p, [("tail", "TAIL")])
    raw = io.open(p, "rb").read()
    if raw.startswith(BOM) and b"TAIL\r\n" in raw:
        caught += 1
    else:
        print("  FAIL 3: BOM or CRLF lost")

    # 4) Ambiguous anchor refused, file untouched
    seeded += 1
    p = mk("dup.md", b"x\r\nx\r\n")
    before = io.open(p, "rb").read()
    try:
        patch(p, [("x", "y")])
        print("  FAIL 4: duplicate anchor not refused")
    except PatchError:
        if io.open(p, "rb").read() == before:
            caught += 1
        else:
            print("  FAIL 4: file modified despite refusal")

    # 5) Missing anchor refused, file untouched
    seeded += 1
    p = mk("miss.md", body.encode("utf-8"))
    before = io.open(p, "rb").read()
    try:
        patch(p, [("nope", "y")])
        print("  FAIL 5: missing anchor not refused")
    except PatchError:
        if io.open(p, "rb").read() == before:
            caught += 1
        else:
            print("  FAIL 5: file modified despite refusal")

    # 6) Wrong ledger column count refused, file untouched
    seeded += 1
    p = mk("ledger.md",
           "| a | b | c |\r\n|---|---|---|\r\n| 1 | 2 | 3 |\r\n".encode("utf-8"))
    before = io.open(p, "rb").read()
    try:
        append_row(p, "| 1 | 2 |")
        print("  FAIL 6: bad column count not refused")
    except PatchError:
        if io.open(p, "rb").read() == before:
            caught += 1
        else:
            print("  FAIL 6: ledger modified despite refusal")

    # 7) Correct row appends with the file's own ending
    seeded += 1
    append_row(p, "| 4 | 5 | 6 |")
    raw = io.open(p, "rb").read()
    if raw.endswith(b"| 4 | 5 | 6 |\r\n") and only_crlf(raw):
        caught += 1
    else:
        print("  FAIL 7: appended row broke line endings")

    # 8) Mixed line endings refused by default, file untouched (260902 fail-closed fix)
    seeded += 1
    p = mk("mixed.md", b"a\r\nb\nc\r\n")
    before = io.open(p, "rb").read()
    try:
        patch(p, [("a", "A")])
        print("  FAIL 8: mixed line endings not refused")
    except PatchError:
        if io.open(p, "rb").read() == before:
            caught += 1
        else:
            print("  FAIL 8: file modified despite refusal")

    # 9) ...but an explicit caller can still opt in and own the normalization
    seeded += 1
    p = mk("mixed2.md", b"a\r\nb\nc\r\n")
    patch(p, [("a", "A")], allow_mixed=True)
    raw = io.open(p, "rb").read()
    if b"A" in raw and only_crlf(raw):
        caught += 1
    else:
        print("  FAIL 9: allow_mixed did not normalize as declared")

    # 10) Escaped pipes inside cells are not column separators
    seeded += 1
    p = mk("esc.md", "| a | b | c |\r\n|---|---|---|\r\n".encode("utf-8"))
    append_row(p, "| x \\| y | 2 | 3 |")
    raw = io.open(p, "rb").read()
    if raw.endswith("| x \\| y | 2 | 3 |\r\n".encode("utf-8")) and only_crlf(raw):
        caught += 1
    else:
        print("  FAIL 10: escaped pipe row refused or written wrong")

    print("textpatch self-test: seeded=%d undetected=%d" % (seeded, seeded - caught))
    return 0 if caught == seeded else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_self_test())
    sys.stdout.write(__doc__ + "\n")
    sys.exit(0)
