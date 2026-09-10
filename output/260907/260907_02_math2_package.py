"""Rebuild review-only projections and their index from the two authoritative sets.

⚠️ STALE — 260908. 이 스크립트를 그대로 돌리면 안 된다. 세 가지가 어긋나 있다.

1. 출력 경로가 옛 위치다. 파생본은 260908에 각 세트 폴더로 옮겨졌다
   (DOC_LOCATION.md §3-2 — 완성본 홈은 세트 자신의 output/<YYMMDD>/):
     output/260907/260907_02_math2_25_questions_review.md
       -> output/260829/260829_02_math2_comprehensive_25_questions.md
     output/260907/260907_02_math2_25_answers_review.md
       -> output/260829/260829_02_math2_comprehensive_25_answers.md
     output/260907/260907_02_math2_40_questions_review.md
       -> output/260822/260822_01_math2_mock40_questions.md
     output/260907/260907_02_math2_40_answers_review.md
       -> output/260822/260822_01_math2_mock40_answers.md
   지금 돌리면 옛 경로에 파일을 다시 만들어 정본이 두 벌이 된다.

2. 머리말 문자열이 "검토용·미투입"으로 하드코딩돼 있다. 두 세트는 260908 외부
   재게이트를 통과해 "학생 배포본"이고, 40제 문제지에는 부교재 원본 재현 9문항
   안내가, 답지에는 9행의 개별 태그가 들어가 있다. 지금 돌리면 그 경고가 지워진다.

3. index 재생성 블록이 상태를 "검토필요"로, 예외 열을 옛 문구로 되돌린다.
   현행 output/_index.md는 상태 "배포가능" 65행이고 예외 열은 N-2/N-3이 분리돼 있다.

재사용하려면 위 세 가지를 먼저 고치고, 재생성 결과를 현행 파일과 diff해
차이가 의도된 것인지 확인한 뒤 덮어쓴다. 근거: output/260907/rev/260907_03_opus_audit_reply.md
"""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT=Path('output/260907')
SOURCES={25:Path('output/260829/260829_02_math2_comprehensive_25.md'),40:Path('output/260822/공통수학2_도형의방정식_모의40.md')}
base=json.loads((ROOT/'260907_02_math2_revision_baseline.json').read_text(encoding='utf-8'))
index=['# 문제 세트 기준 목록','',
'> 현재 사용 가능 여부는 상태 열과 외부 승인 근거로 판단한다. **정본 0문항; 아래 65문항은 검토필요·미투입.**',
'> 통합본이 편집 원본이며 문제지·답지는 재생성 사본이다. 구 인쇄물 output/test2/260830은 당시 판본으로 현행 정본이 아니다.',
'', '| 세트 / 문항 | 유형 | 통합본 | 문제지 | 답지·해설 | 상태 | 변경 | 검증 | 갱신일 | 예외 |', '|---|---|---|---|---|---|---|---|---|---|']
evidence={}
def parts(t):
    matches=list(re.finditer(r'^\*\*(\d+)\.\*\*',t,re.M))
    out={}
    for m in matches:
        tail=t[m.start():]; block=tail.split('\n---',1)[0].rstrip()
        out[m.group(1)]=block
    return out

for count,path in SOURCES.items():
    t=path.read_text(encoding='utf-8-sig'); blocks=parts(t)
    oldblocks=parts(base[path.as_posix()]['text'])
    matches=list(re.finditer(r'^\*\*(\d+)\.\*\*',t,re.M))
    ids=[m.group(1) for m in matches]; expected=[str(i) for i in range(1,count+1)]
    rows=re.findall(r'^\| (\d+) \|.*$',t,re.M)
    assert ids==expected and rows==expected, (count,ids,rows)
    changed=[n for n in expected if blocks[n]!=oldblocks[n]]
    assert changed==(['3','4','6','7','22','25'] if count==25 else [])
    qpath=ROOT/f'260907_02_math2_{count}_questions_review.md'
    apath=ROOT/f'260907_02_math2_{count}_answers_review.md'
    warning=f'> ⛔ 검토용·미투입. 외부 Opus 재검증 및 승인 전 정본 아님. 원본 {count}문항 = 이 파일 {count}문항.\n> ⚠️ 범위 미확정. 세트 추적: `{path.as_posix()}`.\n'
    question_blocks=[]
    for n,b in blocks.items():
        # Keep all problem statements, conditions and scope warnings. Omit author change notes and type tags.
        clean='\n'.join(line for line in b.splitlines() if not (count==25 and line.startswith('>')) and not line.startswith('> 260') and not re.match(r'^`?\[SM2-',line))
        # Following continuation lines belong to historical notes in legacy blocks; retain rather than guess.
        question_blocks.append(clean.strip())
        tag=re.search(r'`?\[(SM2-[^\]\n]+)\]',b).group(1)
        tags=list(dict.fromkeys(re.findall(r'SM2-\d{2}',tag)))
        status='작성자 자기검산(부분); 외부 대기' if n in changed else '기존 이력; 새 외부 검증 대기'
        exception='N축 예외: 카탈로그 의도 재현(일반 면제 아님)' if count==40 and n in ['28','29','30'] else ('N축 예외 미확정' if count==40 and n in ['4','9','13','17','20','23','38','40','6'] else '—')
        sid=re.search(r'^set_id: (.+)$',t,re.M).group(1)
        index.append(f'| {sid} / {n} | {", ".join(tags)} | [{path.name}]({path.relative_to("output").as_posix()}) | [문제지]({qpath.relative_to("output").as_posix()}) | [답지·해설]({apath.relative_to("output").as_posix()}) | 검토필요 | {"교체" if n in changed else "답 표현 보완" if count==40 and n in ["28","29","30"] else "유지"} | {status} | 2026-09-08 | {exception} |')
    qpath.write_text(f'# {count}제 문제지 — 검토용\n\n'+warning+'\n\n'+'\n\n---\n\n'.join(question_blocks)+'\n',encoding='utf-8')
    start=re.search(r'^# .*정답.*$',t,re.M).start()
    apath.write_text(f'# {count}제 답지·해설 — 검토용\n\n'+warning+'\n'+t[start:],encoding='utf-8')
    evidence[str(count)]={'expected':expected,'observed':ids,'answers':rows,'duplicates':[],'missing':[],'extra':[],'changed_question_ids':changed,'unchanged_question_count':count-len(changed),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'questions_sha256':hashlib.sha256(qpath.read_bytes()).hexdigest(),'answers_sha256':hashlib.sha256(apath.read_bytes()).hexdigest()}

Path('output/_index.md').write_text('\n'.join(index)+'\n',encoding='utf-8')
(ROOT/'260907_02_math2_coverage.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PACKAGE_OK expected=65 observed=65 answer_rows=65 duplicates=[] missing=[] extra=[] review_files=4 index_rows=65 canonical_rows=0 warnings=0')
print('question_changes: 25=[3,4,6,7,22,25] 40=[]; unchanged_questions=59')
