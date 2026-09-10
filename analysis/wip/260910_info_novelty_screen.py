"""Own textual comparison record. Not independent or a release ruler."""
from pathlib import Path
import importlib.util, json, hashlib, re
R=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('draft',R/'analysis/wip/260910_info_composite_author.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
sources={
 'EX':'corpus/EX-info-20252M/transcript.md',
 'S1':'corpus/SUP-info-2026-01/transcript.md',
 'S2':'corpus/SUP-info-2026-02/transcript.md',
 'P':'output/260908/260908_04_info_midterm_26.md',
 'A':'output/260910/260910_01_info_composite_a_questions_review.md',
 'B':'output/260910/260910_02_info_composite_b_questions_review.md'}
# Nearest comparisons selected by reading every source transcript and prior 26 items.
refs=[
('P','**20.**','누적값 조건이라는 공통점; 잔액 부족 시 충전하고 다음 지불조건이 달라진다.'),
('EX','[ 단답형2 ]','단일 고정 위치 대입에서 이전 갱신값을 연쇄 전달하는 순회로 변경.'),
('P','**13.**','중첩 호출 공통. 정적 산술 함수와 달리 중간값의 홀짝이 다음 반환식을 선택.'),
('S2','**Quiz 5 (고난이도)**','모든 원소를 값 기준으로 더하던 원본과 달리 행의 최댓값 위치로 행을 고르고 범위를 합산.'),
('P','**7.**','슬라이스 재참조 공통. 파생 문자열의 양끝/내부 관계가 출력 경로를 선택.'),
('P','**20.**','누적량 기준 공통. 다음 리스트 원소를 더하기 전 초과를 검사하고 인덱스까지 종료.'),
('P','**14.**','지역 반환값과 전역 갱신 후 동시 출력 골격이 동일; 중첩 호출 추가만으로 두 구조축을 입증하기 부족.'),
('S1','def list_sum(lst):','리스트축소 재귀 공통. 조건부 개수라는 분기가 추가되나 원본 합산과의 차이는 외부 확인 필요.'),
('P','**21.**','중첩 반복 조건부 계수 공통. 두 자료값의 거리와 i<j인 비중복 쌍으로 비교 모집단 변경.'),
('P','**22.**','삭제·삽입 공통. 삭제 결과로 삽입값을 계산해 두 연산 사이 의존성이 생긴다.'),
('S2','**Quiz 3**','행순회 공통. 이전 행이 다음 기준이 되고 선별 열과 갱신 열을 분리.'),
('P','**26.**','상태추적 공통. 홀짝분기 대신 곱셈후 보정 재귀식; 신규성 보수 검토가 필요.'),
('P','**7.**','슬라이스 공통. 양끝 관계에 따라 절단 방향을 선택한 뒤 동일 선택을 다시 수행.'),
('S2','**Quiz 4**','문자 결합 공통. 고정 위치 접근 대신 누적 이동과 모듈러 결과를 문자 위치로 변환.'),
('P','**13.**','함수합성 공통. 같은 두 함수를 교환하고 조건 경계 통과 여부를 비교.'),
('S1','**Quiz 7**','행렬수정 공통. 대각선 읽기값과 행 끝을 연결해 다른 열에 쓰는 의존성.'),
('EX','9. 파이썬','elif 분기 공통. 겹치는 배수 관계를 회차별 점수로 누적.'),
('P','**5.**','while 몫축소 공통. 나머지를 함께 누적해 반환한 결과를 재입력.'),
('B','**8.**','재귀 본체 2*f(n-1)+n과10*f(n-1)+n이 계수변경 동형. B8 교체 대상으로 지정.'),
('S1','**Quiz 6**','행렬조건 공통. 고정 행의 같은 열을 비교하고 차이를 새 리스트에 모은다.'),
('P','**14.**','유효범위 공통. 지역 인수의 분기 결과를 새 호출에 전달; 전역값은 유지.'),
('EX','15. 파이썬','remove 중복값 처리 골격에 단순 통계 출력을 부가했을 뿐, 약한 변형 위험.'),
('P','**20.**','누적 기준 통과 공통. 누적은 계속하고 최초 회차만 별도 보존.'),
('S1','**Quiz 12**','문자열 축소 공통. 반복으로 양끝 비교 후 둘 다 제거하며 쌍의 수를 계수.'),
('S2','**Quiz 5 (고난이도)**','행별 집계함수로 순위 결정 및 동점 최초 유지. 단일 원소 합산과 다름.'),
('P','**26.**','회차 홀짝에 따라 누적 변수에 서로 다른 산술연산을 적용하는 같은 골격. 연산교체만으로 부족.'),
('A','**2.**','원소수정 공통. 바로 이전 갱신값 전파 대신 양끝 대칭 쌍을 후반부에만 기록.'),
('S1','**Quiz 9**','함수 내 조건순회 공통. 전체합 대신 최초 발견에서 반환하고 미발견 경로를 분리.'),
('S2','**Quiz 3**','열 집계 공통. 여러 열의 독립 집계를 리스트에 저장하고 최댓값 선택.'),
('A','**14.**','문자열출력 공통. 이동누적이 아니라 문자조건과 위치조건으로 이전 문자를 수집.'),
('A','**6.**','while 인덱스 공통. 용량 조건 대신 양쪽 포인터 교차로 종료.'),
('P','**14.**','전역갱신 공통. 반환값 누적과 호출횟수 전역 기록이 병행.'),
('A','**19.**','재귀 본체가 상수계수만 다른 동형; A19와 구분할 핵심 풀이 구조 없음.'),
('A','**9.**','쌍 순회 공통. 두 목록 곱집합에서 중복 일치 다중도를 계산, i<j 필터 없음.'),
('EX','11. 파이썬','insert/del 순차조작 공통. 위치이동 후 슬라이스/길이 부가에 그쳐 보수 검토 필요.'),
('A','**11.**','이전 행 기준 공통. 직전 합의 증가 횟수이며 기준 및 누적 대상이 다름. 외부 유사풀이 확인 필요.'),
('EX','[ 단답형5 ]','삼각형 이중반복 누적에 회차기록을 붙인 정도; 약한 변형 위험.'),
('P','**7.**','슬라이스 접근 공통. 사본과 원본을 따로 수정하는 독립 상태라는 개념이 추가되나 수업근거 확인 필요.'),
('S2','**Quiz 4**','문자연결 공통. 길이 비교 결과에 따라 순서를 달리하는 함수.'),
('A','**3.**','조건반환 함수 공통. 두 인수의 순서관계 세 경로의 값을 합산.'),
('A','**16.**','행렬수정 공통. 읽은 행이 아닌 다음 행의 두 열을 교차 갱신하며 전파.'),
('A','**17.**','동일 배수관계 검사. 교집합제외 계수로 바꾸나 조건구조 변형이 충분한지 외부 확인 필요.'),
('A','**6.**','리스트 while 공통. 원소값이 이동폭을 정해 일부 인덱스만 방문.'),
('S1','**Quiz 11**','재귀 앞뒤의 대칭출력과 동일 풀이 골격. 출력 대신 문자열반환/중앙표식은 약한 변형 위험.'),
('S2','**Quiz 5 (고난이도)**','행별 내부 계수를 초기화하고 충족행 수를 외부에서 집계하는 두 수준 구조.'),
('P','**14.**','유효범위 공통. 함수내 대입이 아닌 전역읽기를 같은 인수로 시간차 비교.'),
('A','**22.**','반복삭제 공통. 고정삭제값 대신 현재최댓값을 매회 선택해 다른 목록으로 이동.'),
('A','**23.**','조건횟수 기록 공통. 최초회차 대신 연속길이를 초기화하며 과거최대 유지.'),
('A','**6.**','while 다음원소 검사 공통. 처음 음수 위치를 슬라이스 끝으로 반환.'),
('P','**25.**','행열 위치조건과 원소홀짝 조건을 결합한 동일 이중반복 누적. 조건만 바꾸는 약한 변형.')]
flags={'A/7','A/22','B/1','B/8','B/12','B/19','B/25'}
docs={k:(R/v).read_text(encoding='utf-8-sig') for k,v in sources.items()}
rows=[]
assert len(refs)==len(m.ITEMS)==50
for q,(key,needle,note) in zip(m.ITEMS,refs):
    matches=[i for i,s in enumerate(docs[key].splitlines(),1) if needle in s]
    assert matches,(key,needle)
    ident=f"{q['group']}/{q['number']}"
    rows.append(dict(item=ident,source=sources[key],line=matches[0],anchor=needle,
        finding=note,axes=q['axes'],disposition='replace-proposal' if ident in flags else 'retain-for-external-review'))
expected=[f'{g}/{n}' for g in ['A','B'] for n in range(1,26)]
assert [r['item'] for r in rows]==expected
frozen=[]
for p in list(sources.values())+['analysis/wip/260910_info_composite_author.py']:
    b=(R/p).read_bytes();frozen.append(dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
payload=dict(grade='proposal',executor='Codex/OMX',independence=False,scope='textual-selfscreen',
    expected=expected,observed=[r['item'] for r in rows],missing=[],extra=[],duplicates=[],
    replacement_proposals=sorted(flags),rows=rows,inputs=frozen,
    warnings=['rendered pages not reviewed this pass','not independent novelty approval'])
out=R/'output/260910/rev';out.mkdir(exist_ok=True)
path=out/'260910_02_info_novelty_text_screen.json'
assert not path.exists(),'Preserve first-pass evidence; do not overwrite after author fixes.'
path.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
text=['---','title: 情報50文항 신규성 텍스트 자체검수','author: 메인 루프','executor: Codex/OMX','grade: proposal','created: 2026-09-10','status: 검토필요','---','',
    '# 정보50문항 — 텍스트 자체검수 (독립 감사 아님)','',
    '## <document>','A/B각25 초안과 EX25 기출, SUP01·02 전사 전문, 기존정보26 본문을 읽어 대조했다. 이미지 시각 재대조는 이 회차에서 하지 않았다. 원본 유형을 새로 분류하지 않았으며 기존 승인 유형을 사용한 새 문항의 풀이 구조를 비교했다.','',
    '## <context>','최근접 비교는 수치유사도 자동검색 판정이 아니라 텍스트를 읽은 작성자 자체 판단이다. 출처의 줄번호·문자열 실존은 스크립트가 검증했다. A/B전50 식별자 커버리지는 JSON의 기대/관측/누락/초과/중복 목록으로 확인한다.','',
    '## <findings>','교체 제안7건: A7·A22·B1·B8·B12·B19·B25. 나머지43건은 신규성 PASS가 아니라 외부 확인 대상으로 보존. 특히 A8·A12·B10·B11·B13·B17은 추가 경계 검토가 필요하다.','',
    '| 문항 | 최근접 비교원 | 풀이 구조 대조 | 처리 |','|---|---|---|---|']
text += [f"| {r['item']} | `{r['source']}:{r['line']}` | {r['finding']} | {r['disposition']} |" for r in rows]
text += ['','## <questions>','교체 뒤 두 비수치축과 복합 의존성이 실제로 충분한가? 이미지 근거와 외부 판정 전에는 확정하지 않는다.','',
    '## <proposed_fixes>']+[f'- [ ] {x}: 기존 출력추적 골격에서 다른 정보 의존성·목표 추론으로 재설계.' for x in sorted(flags)]
text += ['','## <output_format>','본문 자체검수 이후 별도 작성 단계에서만 승인된 교체 요청을 적용한다. 사용자는 단순변형을 새 문제로 교체하도록 이미 요청했다. 이 보고서는 외부 승인 라벨을 부여하지 않는다.','',
    '## history','- 260910 Codex/OMX solo. 50행 최근접 근거 작성·앵커 확인. 현행 제품은 이 검수 단계에서 변경하지 않음.','',
    'Pipeline: 정보50 작성 → **신규성 텍스트 자체검수50 완료** → 교체7 → 재검산 → 외부 감사',
    'Stage: Codex/OMX = 모델 미확인 — 기대50/관측50; 누락·초과·중복0. 이미지·외부 감사 ▲ blocked',
    'Team: mode=solo; lead=Codex/OMX | 모델 미확인 | 자체검수 | 완료; lanes=없음; independence=not applicable; planned/unavailable/failed lanes=없음',
    'Next: 저자 단계로 전환해7건 교체 및 재계산; 외부 신규성 승인으로 주장하지 않는다.']
(out/'260910_02_info_novelty_text_screen.md').write_text('\n'.join(text)+'\n',encoding='utf-8')
print('TEXT SCREEN: expected=50 observed=50 missing=[] extra=[] duplicates=[]; replacement proposals=7; external approval=0.')
