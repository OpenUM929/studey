---
actor: type-extractor
task: EX-math2-20252M_render_recovery
target: origin_data/2025_2학기_1학년_중간/2025_2학기_중간_1학년_공통수학2_고사원안.hwp
status: in-progress
updated: 2026-08-28
---

| no | 범위 | state | 산출물 | 비고 |
|---:|---|---|---|---|
| 1 | 정본·기존 전사·이미지 경로·render 도구 조사 | done | `.claude/agents/type-extractor.md`, `docs/DATA_STANDARD.md`, corpus 실측 | meta 5쪽·22문항, `corpus/_images/EX-math2-20252M/pNN.png` 0건. Hwp Office 2022·PyMuPDF·win32com 사용 가능. 유형 판단 없음. |
| 2 | HWP→PDF→PNG 재현 도구 작성 | in-progress | `tools/render_hwp_pages.py` | 1차 실행은 보안 모듈 미등록으로 fail-closed. 한컴 공식 `FilePathCheckerModuleExample.dll`(SHA-256 `9AC5B97C47AC8AED1E8BCA27A3EEF39411361D8F68C262509F0C40A8F9D21BB6`)을 HKCU에 등록했다. 임시 출력에서 5쪽·가독성·해시를 검증하기 전 정본 이미지/메타/로그는 수정하지 않는다. |

NEXT: 임시 디렉터리에 dpi 160으로 렌더하고 PDF 5쪽·PNG 5건·이미지 가독성을 검증한다. 통과 시에만 `corpus/_images/EX-math2-20252M/p01.png`~`p05.png`를 생성하고 meta/verify_log를 append-only 규칙으로 갱신한다.
