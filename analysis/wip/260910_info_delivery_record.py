"""Append current delivery evidence without altering products or old ledger rows."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.textpatch import patch

record = json.loads((ROOT / 'output/260910/rev/260910_11_info_delivery_check.json').read_text(encoding='utf-8'))
assert record['expected'] == record['observed'] and len(record['observed']) == 50
assert all(not record[key] for key in ['duplicates', 'missing', 'extra', 'answer_mismatches'])

def append(relative, marker, body):
    path = ROOT / relative
    old = path.read_text(encoding='utf-8-sig')
    if marker not in old:
        patch(path, [(old, old.rstrip() + '\n\n' + body + '\n')])

append('output/260910/260910_04_info_creation_report.md', '## 13. 실제 문제 전달 경로와 현재 검증', '''## 13. 실제 문제 전달 경로와 현재 검증

사용자의 목적은 보고서가 아니라 실제 문제 수령이다. 현재 저장된 정보 A/B 각25문항은 아래 파일에서 직접 확인한다. **신규 최고난도 완성본이 아니라 기존 revision4 검토본**이다.

| 구분 | 문제 | 정답·해설 |
|---|---|---|
| 정보 A형25 | [문제지](260910_01_info_composite_a_questions_review.html) | [답지](260910_01_info_composite_a_answers_review.html) |
| 정보 B형25 | [문제지](260910_02_info_composite_b_questions_review.html) | [답지](260910_02_info_composite_b_answers_review.html) |

이번 재검증은 작성 데이터가 아니라 저장된 문제지의 Python 코드50개를 실행하여 저장된 정답50개와 대조했다. 식별자 A/1~25·B/1~25의 예상/관측 집합 일치, 중복·누락·초과·정답 불일치0이다. 문제지 정답·해설 표식 혼입0, MD4·HTML4 존재 및 HTML 각각25문항을 확인했다. 브라우저 인쇄 검사는 미실행이다.

검증 명령: `python -X utf8 analysis/wip/260910_info_delivery_check.py`, 종료0. [전체 식별자·8파일 해시·미완료 경고7건](rev/260910_11_info_delivery_check.json). 첫 실행의 B/1 불일치는 검사기의 줄바꿈 표시를 `/`로 가정한 오류였으며, 실제 답지의 `⏎` 표기를 적용해 재실행했다. 문제와 정답은 변경하지 않았다. 자체 실행 대조는 독립 풀이 또는 의미상 신규성 감사가 아니다.

**진행을 막는 실제 조건:** 교과서33장 운영 PRD 승인·정제가 아직 없으며 CLAUDE의 신규 데이터 가공 선행 게이트가 적용된다. Astra 대체 자체는 승인돼 있지만 현재 노출된 전문 역할에는 Sol 모델 고정이 명시되어 있고, 앞선 verifier 파일럿도 모델 불일치로 중단됐다. 같은 요청을 반복하거나 다른 모델을 Astra로 표시하지 않는다. 실제 Astra로 실행되는 독립 검토·판정 경로가 필요하다. 따라서 교과서 반영·최고난도25×2·학생 배포 승인 완료라고 주장하지 않는다.

§12 일부 문장은 이전 기록 과정에서 물음표로 손상됐다. 해석하지 말고 다음 내용을 따른다: 중간고사 범위 내 심화 훈련 목적이며, 기존 최고난도는 학생별 상급 연습 기준선으로 취급한다. 새 최고난도 목표는 풀이 선택의 비자명성, 조건 간 의존성, 경계·존재성 검증이다. 공식 Tier 기준 변경이나 독립 난도 인증은 아직 아니다. 해당 손상은 새 문제 작성 증거가 아니다.
''')
append('analysis/wip/mainloop_260908_math2_64_revision.md', '### 260910 delivery evidence checkpoint', '''### 260910 delivery evidence checkpoint

Owner=/root; solo; actual model/depth unexposed. User requests actual problem delivery. Fresh saved-code vs saved-key checks: 50/50, exact IDs A/1..25,B/1..25; missing/extra/duplicates/mismatches0; 8 split artifact hashes captured in output/260910/rev/260910_11_info_delivery_check.json. Products unchanged. First test failure was validator newline display mapping, corrected to existing answer convention and rerun exit0. Baseline16/textbook33 snapshots match. Report section13 carries direct links and current blockers; earlier section12 has literal question-mark encoding damage, not a reliable Korean record.

NEXT: actual Astra-capable independent PRD review/ruling is prerequisite for textbook33 processing; exposed specialist roles remain fixed Sol and previous verifier pilot failed model identity. Do not repeat same model-mismatched dispatch or process unapproved new source. Existing A/B remain review-only, not new hardest50. Preserve math64/new50 backlog. Resume verification: python -X utf8 analysis/wip/260910_info_delivery_check.py. No quota exhaustion or reset time observed; this is a model/approval blocker, not resource HOLD. No manual compaction claimed.
''')
print('Recorded delivery links, saved-answer evidence, and precise blockers; products unchanged.')
