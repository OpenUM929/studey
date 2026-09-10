"""Update owned progress reports without modifying source or authority policy."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.textpatch import patch

ROOT = Path(__file__).resolve().parents[2]

def append(path, marker, text):
    p = ROOT/path
    old = p.read_text(encoding='utf-8')
    if marker not in old:
        patch(p, [(old, old.rstrip()+'\n\n'+text+'\n')])

report = ROOT/'output/260910/260910_04_info_creation_report.md'
old = report.read_text(encoding='utf-8')
heading = '## 8. ??'
if heading in old:
    prefix = old.split(heading,1)[0]
    replacement = '''## 8. 현행 원본 기준 13쌍 대조 — revision2 이력

[13쌍 비교 기록](rev/260910_05_info_pair13_review.md)은 revision2 당시의 작성자 대조이다. A3·A10·B7의 경미 변형 위험을 발견했다. 독립 감사는 실행하지 않았다. 이때 일부 보고서와 WIP의 한글이 물음표로 손상되어, 이 절은 원래 JSON 근거에 맞춰 복구했다. 아래 revision3이 현재 제품이며 13쌍 증거는 과거판이다.
'''
    patch(report,[(old,prefix+replacement)])

section = '''## 9. revision3 — 구조 중복 위험7건 교체, 전체 텍스트 비교 기록

사용자 지시: 숫자만 바꾸거나 풀이가 유사한 문제를 배제하고 실제 결과물까지 진행. 이전에 ‘독립 감사 진행 중’이라고 알린 표현은 잘못됐다. 실제 실행은 Codex/OMX 작성자의 비교·재작성·자체 검산이며 독립 감사는 0/50이다.

### 실제 변경

- 교체: **A3·A8·A10·A19·B7·B11·B24**. [교체 전 검토](rev/260910_06_info_rewrite_notes.md), [revision2 보존본](rev/260910_06_info_revision2_archive.json).
- 함수 중첩 전달, 단순 리스트 누적 재귀, 삭제→삽입, 가중합 재귀, 호출수 카운터, 직전 행 기준 비교, 접두 탐색을 각각 순환 이동 제어·동점 순위·삭제 자리 재검사·겹친 구간 교환·자원 승인·작업대 배정·두 자료원 병합으로 교체했다.
- 현재 문제/답 Markdown4개·HTML4개·통합본2개·novelty TSV2개 동기화. 표 정답 볼드 및 명시적 ‘⚠️ 범위 미확정’도 보완했다.
- [문항별50개 비교 기록](rev/260910_07_info_revision3_comparison.md), [해시·코드 증거](rev/260910_07_info_revision3_comparison.json). 전사된 기출·퀴즈·개념 문서 및 현행 기존26제와 작성자 텍스트 대조. 원본 이미지의 재검증이나 교과서 전면 반영을 뜻하지 않는다.

### 검증 결과와 한계

- `python -X utf8 analysis/wip/260910_info_composite_author.py --write`: 저장 코드50/50과 작성 정답 일치, 정확 식별자 누락·초과·중복0, exit0. 경고6개 유지, 배포 BLOCKED.
- `python -X utf8 analysis/wip/260910_info_revision3_review.py`: A1~25/B1~25의 관측 기록50/50. 현재 세트 상호1225쌍에서 이름·상수 정규화 AST 일치0. **이 검사는 풀이의 의미상 유사성이나 원본 전체 대비 신규성을 보증하지 않는다.**
- A17·A21·B2·B9·B15·B16·B21은 작성자 관측상 구조 차이가 있지만, 엄격한 ‘유사 풀이 배제’ 충족 여부를 독립 검토해야 할 잔여 후보이다. 이들을 신규성 PASS로 바꾸지 않았다.
- 제품은 각25문항, 문제·답 분리본을 실제 저장했으나 **사용자가 요청한 모든 자료 활용·모든 유사 풀이 제거·독립 감사·배포 완료는 아직 아니다.**

### 실제 차단 요소

1. 새 교과서33장의 명명 정책/운영 PRD 승인·정제가 미완료다. 현행 지침은 승인 전 신규 데이터 가공을 금지하므로 임의 등록·전사로 우회하지 않았다. 모든 참고자료를 썼다고 할 수 없다.
2. 현재 세트는 프로그래밍 부분 연습이다. 기출의 보안·CCL 영역까지 포괄하는 최종 범위 설계가 남아 있다.
3. 외부 전용 검증을 Astra나 작성자 자기검산으로 대신하도록 하는 개정안은 미적용이다. 기존 개발자 지침의 권한 제한을 이 저장소 편집으로 없앨 수 없다.
4. 정식 두25제 식별자 충돌과 실제 학생 정보 오답 입력도 미해소다.

이 차단 요소를 단순한 다음 단계 안내로 숨기지 않는다. 추가 자료 활용과 최종 감사·배포는 위 조건 해소 전 완료 처리할 수 없다. 진행 기록은 현재 상태와 다음 작업을 저장한 것이며 작업 전체 완료 선언이 아니다.
'''
append('output/260910/260910_04_info_creation_report.md','## 9. revision3',section)
append('output/260910/rev/HISTORY.md','revision3 structure7',
       '## 260910 revision3 structure7\n\nCodex/OMX 작성자: A3/A8/A10/A19/B7/B11/B24 교체; 50/50 자체검산. 260910_06_info_rewrite_notes.md 및 260910_07_info_revision3_comparison.md. 독립 검증0/50, 배포BLOCKED.')
append('analysis/wip/mainloop_260908_math2_64_revision.md','### 260910 revision3 checkpoint',
'''### 260910 revision3 checkpoint

owner=/root; executor=Codex/OMX; model/depth=unexposed; solo, no agents. User reaffirmed full-source non-clone deliverable. Review then author changes A3,A8,A10,A19,B7,B11,B24. Revision2 archive retained. Current50 saved-code answers match50/50. Comparison observations cover exact50 identifiers; current1225 normalized AST pair checks have0 identical shapes, not a semantic novelty verdict. Sources3 transcripts plus current26 read; textbook33 unrefined. Report section9 and current index revision3 updated. Prior pair13 script is historical and should not be rerun against revision3.

NEXT: strict semantic review/reengineering of A17,A21,B2,B9,B15,B16,B21; then full-source coverage requires textbook naming/PRD approval and refinement, nonprogramming coverage design. Do not substitute a Codex lane for the external-only audit. Student errors/ID policy unresolved. Math remaining50 review/new hardest50 preserved. First validation: python -X utf8 analysis/wip/260910_info_revision3_review.py; current input/artifact hashes in output/260910/260910_03_info_selfcheck.json and rev/260910_07_info_revision3_comparison.json. Writes: own scripts, own12products, report, review evidence, index/history, WIP. No manual compaction claimed. Earlier pair13 WIP paragraph contains encoding damage; use original JSON and this checkpoint instead of interpreting question marks.
''')
append('output/260910/260910_05_info_opus_review_prompt.md','## revision3 dispatch hold',
'''## revision3 dispatch hold

현재 문제는 revision3이며 앞선 revision2/13쌍 입력 동결은 현행이 아니다. A3/A8/A10/A19/B7/B11/B24 교체됨. 외부 발주 전에 현재 selfcheck/비교 JSON을 재측정하고 입력 목록을 재작성해야 한다. 본 파일은 **미발주 준비본**이며 지금 그대로 실행할 프롬프트가 아니다. 독립 검증0/50. 교과서·학생입력·범위·잔여 신규성 검토 및 발주 예산 게이트 미해소.
''')
print('Owned report/history/WIP/prompt updated; no source or authority changes.')
