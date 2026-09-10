"""One-time, idempotent coordinator bookkeeping; never edits products or sources."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from textpatch import patch, append_row, PatchError


def add(relative, marker, block):
    path = ROOT / relative
    old = path.read_text(encoding='utf-8-sig')
    if marker not in old:
        # This coordinator-owned WIP contains 5 CRLF and 132 LF lines.
        # Explicitly own newline normalization there only; keep other files strict.
        patch(str(path), [(old, old.rstrip() + '\n\n' + block + '\n')],
              allow_mixed=relative == 'analysis/wip/mainloop_260908_math2_64_revision.md')


add('output/260910/260910_04_info_creation_report.md', '## 7. 비교 원본 변경', '''## 7. 비교 원본 변경 — 재개 감사 중단

[변경 점검 보고서](rev/260910_04_info_source_drift.md)와 JSON에 실측을 저장했다. 제품 revision2는 무변경이고 직접 해시16/16 및 자체계산50/50은 유지된다. 그러나 비교 원본4개 중 기존 정보26제가 변경됐다. 현행 최근접 비교13개(A1·A3·A5·A6·A9·A10·A13·A15·A18·A21·A23·B7·B21)는 재대조가 필요하며, 나머지37개도 신규 비교 후보 검토가 남는다.

`python -X utf8 analysis/wip/260910_info_lineage_check.py`는 변경1개를 출력하고 exit1/BLOCKED로 종료했다. 과거 신규성 JSON의 해시가 같다는 사실만으로 그 안의 원본까지 불변이라고 취급하지 않는다. 외부 검증0/50, 배포 ▲ blocked. Opus 프롬프트는 여전히 미발주이며 비교 입력이 안정되고 재동결되기 전 실행하지 않는다.''')

add('output/260910/260910_05_info_opus_review_prompt.md', '## 추가 중단 조건: 비교 원본 변경', '''## 추가 중단 조건: 비교 원본 변경

기존 정보26제 파일이 역사 신규성 JSON의 동결값과 다르다. 상세 증거는 `rev/260910_04_info_source_drift.md`·`.json`이다. 직접 제품 해시16/16만으로 선행 조건을 충족하지 않는다. 비교 원본 현행 판본을 확인하고 정보50제와 재대조한 뒤 발주 직전 새 입력 명세를 작성한다. 기존 JSON 값을 현행 값으로 단순 덮어써서 해소하지 않는다. 이 보고서도 맹목 답안 고정 전 읽지 않는다. 제품은 revision2, 외부 실행0회 유지.''')

add('output/260910/rev/HISTORY.md', '260910_04_info_source_drift.md', '- [비교 원본 변경 점검](260910_04_info_source_drift.md): 직접16/16 불변, 비교 원본1/4 변경·직접 영향13개. 신규성 재대조 전 ▲ blocked; 제품 무수정.')

add('analysis/wip/mainloop_260908_math2_64_revision.md', '### 260910 source-drift checkpoint', '''### 260910 source-drift checkpoint

owner=/root; executor=Codex/OMX; model/depth=unexposed; solo; no dispatch. NEXT의 입력 검증 중 추가 의존성 발견: 기존 정보26제 수정으로 신규성 비교 입력이 변경됨. 정보50 revision2 자체계산50/50·직접 입력/제품 해시16/16 유지. 비교 원본3/4 동일, 기존26제는45,287 bytes SHA256 e635fdd5f27edc96e7a9c96cffa6a474058d835078ec174d344204884fe456ce. 당시39,367 bytes와 불일치. 다른 소유자의 수정은 보존하고 제품 재생성/정제/승격을 진행하지 않았다.

증거=output/260910/rev/260910_04_info_source_drift.json; 검토=동명md. 직접 영향13개 목록은 JSON에서 현재 TSV 기준으로 산출. 제품12·카탈로그·학생원장 무수정. lineage 명령 exit1/BLOCKED는 발견을 숨기지 않는 중단이며 통과가 아니다. 신규 진단 AST 성공; textpatch seeded10 undetected0. 보고서§7·미발주 Opus 전달문·HISTORY 갱신.

NEXT: 기존26제 소유자의 수정 종료와 현행 판본을 확인하고 새 비교 증거로 정보50제 신규성 재대조. 먼저 현재26제 해시를 이 증거와 대조한다. 바뀌면 ▲ blocked로 입력 확인부터 다시 한다. 동일하더라도 과거 JSON을 덮어써 통과시키지 않는다. 교과서 명명/PRD 선행승인·정제, 두25제ID, 실제학생오답, 기존 수학50개 잔여검수 및 신규최고난도50 미완료. 다음 검증=python -X utf8 analysis/wip/260910_info_lineage_check.py (역사 기준 변경이므로 예상exit1). 외부 자동실행 금지. 수동 compaction 수행 주장 없음.''')

ledger = ROOT / 'analysis/REV_LOG.md'
if '260910_04_info_source_drift.md' not in ledger.read_text(encoding='utf-8-sig'):
    row = '| 260910 | [정보50 비교원본 변경](../output/260910/rev/260910_04_info_source_drift.md) | Codex/OMX 자체 재개 점검: 직접16/16 유지, 비교원본1/4 변경·직접 영향13개; lineage exit1 | ▲ blocked | 보고서§7·Opus 준비문 갱신; 원본·제품 무수정 |'
    try:
        append_row(str(ledger), row)
    except PatchError:
        add('output/260910/rev/260910_04_info_source_drift.md', '## 원장 반영 보류',
            '## 원장 반영 보류\n\nREV_LOG는 CRLF1/LF168 혼합으로 textpatch가 쓰기를 거부했다. 공유 원장의 다른 작업자 행을 정규화하지 않고 원본을 보존했다. 다음 행은 미반영 초안이다:\n\n' + row)
        add('analysis/wip/mainloop_260908_math2_64_revision.md', '### source-drift trace pending',
            '### source-drift trace pending\n\nREV_LOG append는 혼합 개행으로 거부되어 미반영. 초안 행은 source_drift 보고서 마지막 절에 보존. 공유 원장은 무수정. 본인 WIP만 CRLF5/LF132에서 LF로 정규화해 기존 텍스트를 보존했다. 보고서/전달문/HISTORY는 반영 완료. 원장 쓰기 완료로 보고하지 않는다.')
        print('Report/relay/history/WIP recorded; shared trace BLOCKED by mixed newlines.')
        raise SystemExit(1)
print('Recorded source-drift report, relay, history, WIP and 5-column trace.')
