from pathlib import Path
import hashlib
import json
import sys
sys.path.insert(0,'tools')
from textpatch import append_row, patch

report='260908_05_math2_64_similarity_review.md'
home=Path('output/260908/rev')
manifest=json.loads((home/'260908_04_math2_64_manifest.json').read_text(encoding='utf-8'))
for row in manifest['sources']+manifest['copies']:
    data=Path(row['path']).read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'], row['path']
wip=Path('analysis/wip/mainloop_260908_math2_64_revision.md')
state={
    'stage':'standardization-and-similarity-partial',
    'owner':'Codex/OMX main loop; actual model/depth not exposed',
    'completed_units':['32/A1','32/C6','32/C7','32u/B2','32u/D7'],
    'source_manifest':'output/260908/rev/260908_04_math2_64_manifest.json',
    'manifest_sha256':hashlib.sha256((home/'260908_04_math2_64_manifest.json').read_bytes()).hexdigest(),
    'validation':'STRUCTURAL_COPY_OK: sources=5 unchanged; questions=64 answers=64 copies=4 content_equal=4; warnings=0',
    'blockers':['32u naming ruling pending','external independent audit not run','review/fix separation'],
    'next':'Resume audit source/copy hashes; complete remaining59 item comparisons including9 candidates; record proposed changes before owner-authoring stage. Do not regenerate completed5 evidence units.',
    'next_validation':'python -X utf8 output/260908/rev/260908_04_math2_64_review_prepare.py',
    'quota':'No resource-exhaustion/reset notice observed; context checkpoint only',
}
content='''---
title: "32+32제 표준화·유사성 검수·교체"
created: 2026-09-08
author: 메인 루프
status: in-progress
---

## 사용자 승인과 단계
상산고 수학 출제위원 관점으로 표준화→유사성 검수→교체→정답감사→완료본 등록 요청.
기존25·40제 WIP NEXT를 바꾸지 않고 이 요청의 별도 단위로 실행한다.
이전32 A1 외부pilot 준비는 폐기하지 않되, 새 요청의 전수 유사성 점검을 먼저 수행한다.
외부 독립검증·명명 판정은 대체하지 않는다. 검사자와 원본 수정자 분리 유지.

## 완료 단위
구조 중복 근거5개: 32 A1/C6/C7, 32u B2/D7. 원문 이미지 p01/p08/p10/p12 확인.
추가후보9개는 보고서에 있고 아직 검수완료에 합산하지 않았다.
검토용 문제·답 사본4개, 문항/답64/64, 원본93·25·40 입력 동결, 원본5개 무변경.
표준화 전체·교체·정답감사·완료본 등록은 미완료. 최종 승인본0개.
새 파일만 Codex/OMX 배타 소유. 기존25·40 산출물은 최근 외부 변경이 있어 쓰지 않는다.

## 상태·검증·재개
'''+json.dumps(state,ensure_ascii=False,indent=2)+'\n\nNEXT: '+state['next']+'\n'
if wip.exists():
    raise RuntimeError('Existing WIP requires resume, not overwrite')
wip.write_text(content,encoding='utf-8',newline='\n')
old=Path('analysis/wip/mainloop_260907_math2_revision_release.md')
t=old.read_text(encoding='utf-8')
anchor=next(x for x in t.splitlines() if x.startswith('NEXT:'))
note='260908 새 사용자 4항 요청: 32+32 전수 유사성·교체 작업은 analysis/wip/mainloop_260908_math2_64_revision.md로 분기한다. 기존25·40 NEXT는 보존하며, 선행32 A1 외부pilot보다 전수 유사성 검수를 먼저 하는 의존성을 기록한다.\n\n'
if note not in t:
    patch(str(old),[(anchor,note+anchor)])
history=home/'HISTORY.md'
line=f'- [{report}]({report}): 구조 중복5건·추가후보9건, 검토용 사본4개. 전수 검수·교체·외부 감사 미완료.\n'
if line not in history.read_text(encoding='utf-8'):
    prior=history.read_text(encoding='utf-8')
    patch(str(history),[(prior,prior+'\n'+line)])
row=f'| 260908 | 2 | Codex/OMX proposal | two 32-item sets | 5 reproduced structural overlaps; 59 pending; 4 review copies | {report} | flagged | finish comparisons then owner authoring and external audit |'
if row not in (home/'_index.md').read_text(encoding='utf-8'):
    append_row(str(home/'_index.md'),row)
row=f'| 260908 | [32+32 신규성 사전검수](../output/260908/rev/{report}) | Codex/OMX proposal: 구조중복5건 이미지 확인·추가후보9건; 사본4개 내용일치·원본5개 무변경; 전수검수·교체·외부감사 미완료 | 검토필요 | output/260908/rev/{report} |'
if row not in Path('analysis/REV_LOG.md').read_text(encoding='utf-8'):
    append_row('analysis/REV_LOG.md',row)
(home/'260908_06_math2_64_checkpoint.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('CHECKPOINT_OK; hashes=9 unchanged; ledger_rows=2; release=BLOCKED')
