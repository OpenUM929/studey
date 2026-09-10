"""Persist requested storage procedure without changing assessment thresholds or authority."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path('tools').resolve()))
from textpatch import insert_before

updates={
'CLAUDE.md':('## 작업 흐름','''## 문제 완성본 관리 (260908 사용자 요청)

문항 신규 생성·교체·수정 시 문제만 저장하고 종료하지 않는다. 기존 외부 solve-back·품질감사·
arbiter·사용자 확인 게이트를 통과한 완성본은 기존 `output/<YYMMDD>/` 체계에 보존하고,
`output/_index.md`에 현재 정본의 통합본·문제지·답지/해설 경로와 문항별 상태를 같은 작업에서 등록한다.
미검증은 `검토필요`, 최종 승인분만 `정본`, 폐기 결정분은 `폐기`로 구분한다. 기존 정본은 새 판본 승인 전 제거하지 않는다.
문항의 본문·태그·정답표·해설·채점기준·역검산표·요약표·이력과 관련 인쇄 사본의 현행 여부를 함께 대조한다.
문제지와 답지는 동일 통합본에서 분리 생성하고 문항 ID의 누락·중복·추가 및 내용 일치를 검사한다.
적용한 예외 규칙과 판정 근거, 작성자 검산과 독립 검증의 구별, 감사 이행 기록을 남긴다.
경로 기준은 `analysis/DOC_LOCATION.md` §3-1, 검토·승인 권한은 기존 `analysis/REV_GUIDE.md`를 따른다.
이 절은 저장·동기화 절차이며 N축 기준·난이도 자·외부 권한을 변경하거나 면제하지 않는다.

'''),
'AGENTS.md':('## Context-continuity checkpoint','''## 문제 정본 저장·인덱스 동기화 (260908)

문항을 생성·교체·수정하면 `CLAUDE.md`의 「문제 완성본 관리」와
`analysis/DOC_LOCATION.md` §3-1을 적용한다. 최종 게이트 통과 후 기존 output 날짜별 저장소의
정본·별도 문제지·답지/해설과 `output/_index.md`를 같은 작업에서 갱신하고 감사 이력을 남긴다.
미검증 문항은 `검토필요`로 기록하며 작성자 자기검산을 외부 Opus 독립검증으로 표시하지 않는다.
문제 작성만으로 완료 선언하지 않는다. 기존 N축 예외와 two-key·write surface는 그대로 유지한다.

'''),
'analysis/DOC_LOCATION.md':('## 4. 명명·참조 규칙','''### 3-2. 문제 완성본 기준 목록 (260908 사용자 요청)

완성 문제의 기존 홈은 §3-1의 `output/<YYMMDD>/`이며 별도 경쟁 정본 폴더를 만들지 않는다.
`output/_index.md`는 현재 사용 가능한 승인 판본과 검토 대기 판본을 구분하는 기준 목록이다.
문항은 기존 세트ID와 세트 내 번호의 쌍으로 식별한다(새 ID 체계 도입 아님).
등록 정보: 유형, 통합본·문제지·답지/해설 직접 경로, `정본/검토필요/폐기`, 변경 구분,
검증 근거, 갱신일, 예외 규칙. `정본`은 기존 release 게이트를 통과한 경우에만 쓴다.
검토용 분리본은 파일명·머리말에 검토용과 미투입을 표시한다. 원본 이력과 구 인쇄물은 보존하되
현행 index에서 과거판임을 식별한다. 정본 변경 시 답·해설·index·감사 기록을 동반 갱신한다.

'''),
'analysis/catalog/AUTHORING_GUIDE.md':('## 2. 모델 선택','''## 1-C. 교체 후 동반 갱신과 보관 (260908 사용자 요청)

교체 시 본문·태그·정답표(유형ID 포함)·해설·채점기준·역검산표·요약표·이력을 같은 작업에서 대조한다.
값이 변하지 않은 면은 재집계 결과가 같음을 기록하고 불필요하게 바꾸지 않는다.
완성본 보관·분리 문제지/답지·`output/_index.md` 등록·감사 이력은 `CLAUDE.md` 「문제 완성본 관리」를 따른다.
기존 품질 기준과 외부 검증 권한은 변경하지 않는다. 미검증 문항은 정본으로 표시하지 않는다.

'''),
'README.md':('## 30초 폴더 지도','''## 문제·답지 찾기

현재 판본과 사용 가능 상태는 [문제 세트 기준 목록](output/_index.md)에서 확인한다.
`검토필요`는 학생 투입 승인본이 아니다. 완성본 관리 절차는 [CLAUDE.md](CLAUDE.md)의
「문제 완성본 관리」, 저장 위치는 [DOC_LOCATION](analysis/DOC_LOCATION.md) §3-1·§3-2를 따른다.

''')}
for name,(anchor,block) in updates.items():
    t=Path(name).read_text(encoding='utf-8-sig')
    if block.strip() not in t: insert_before(name,anchor,block)
    print('GUIDANCE',name)
