"""Append-only draft index/history registration; does not grant release."""
from pathlib import Path
import importlib.util, json, hashlib, re

root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('own',root/'analysis/wip/260910_info_composite_author.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

def append_once(path, marker, text):
    old=path.read_text(encoding='utf-8') if path.exists() else ''
    if marker in old:
        return
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('a',encoding='utf-8',newline='\n') as f:
        f.write('\n'+text+'\n')

marker='## 260910 정보 복합 A/B 초안 — 구조 중복14건 교체 후 현행 revision4'
lines=[marker,'','앞선 260910 정보 복합 A/B 초안 표는 교체 전 이력이며 아래가 현재 판본이다. 정식 세트ID가 없는 제안 초안이다. A/B는 문서 묶음 이름이며 신규 영구 ID가 아니다. 외부 검증0/50; 배포 미승인. 아래 각 문항의 실제 유형·직접 경로를 기록한다.','',
    '| 문서/문항 | 유형 | 통합본 | 문제지 | 답지/해설 | 상태 | 변경 | 검증 근거 | 갱신일 | 예외·미해결 |',
    '|---|---|---|---|---|---|---|---|---|---|']
for q in module.ITEMS:
    stem=module.stem(q['group'])
    lines.append(f"| {q['group']}/{q['number']} (ID 미발급) | {'+'.join(q['types'])} | "
        f"[통합본](260910/{stem}_review.md) | [문제지](260910/{stem}_questions_review.md) | "
        f"[답지](260910/{stem}_answers_review.md) | 검토필요 | 신규 초안 | "
        '[자체검산](260910/260910_03_info_selfcheck.json) | 2026-09-10 | 외부감사·신규성·교과서정제·학생맞춤·ID·Tier 미완료 |')
append_once(root/'output/_index.md',marker,'\n'.join(lines))
append_once(root/'analysis/REV_LOG.md','260910_04_info_creation_report.md',
    '| 260910 | [정보 복합50 작성·자체검산](../output/260910/260910_04_info_creation_report.md) | '
    'Codex/OMX proposal: A25+B25 작성, 자체 실행50/50·누락/초과/중복0, 정답오기3건 수정. '
    '외부0/50·신규성 등 경고6건; 문제/답 MD4+HTML4 분리. | 검토필요 | output/260910/260910_04_info_creation_report.md |')
append_once(root/'analysis/wip/mainloop_260908_math2_64_revision.md','### 260910 정보50 작성 산출 체크포인트',
    '### 260910 정보50 작성 산출 체크포인트\n\n'
    'A1~25/B1~25 작성 완료. 실제 저장본 코드50/50 실행·작성정답 대조 일치. '
    '초기 정답오기 A1/A13/A19 수정 후 재실행 exit0. 원본·학생원장·카탈로그 무변경. '
    '문제/답 MD4·HTML4, 통합MD2, 신규성초안TSV2, 검산JSON, 보고서, 미발주 Opus 프롬프트 저장. '
    '증거 및 파일별SHA256: output/260910/260910_03_info_selfcheck.json. '
    '보고서: output/260910/260910_04_info_creation_report.md. exclusive owner=/root, model/depth 미노출, native lanes 없음. '
    '▲ blocked: 배포는 외부감사0/50·신규성미검·학생정보없음·교과서정제·ID충돌·Tier미확정6건. '
    'NEXT=정보 신규성 원본/기존26/상호 전수 대조와 교과서 정제, ID정책 처리. '
    '그 후 A25 외부pilot 예산 실측/사용자 회차 승인, 회신 전 배포 승격 금지. '
    '수학 미판정50검수·새 최고난도50은 보존된 별도 미완료 NEXT. '
    '다음 검증=python -X utf8 analysis/wip/260910_info_composite_author.py (읽기/계산 전용); '
    '먼저 selfcheck JSON artifacts SHA256 대조. --write는 자기 출력 재생성이므로 외부 수정 발생 뒤 금지. '
    '수동 compaction 또는 외부 실행을 했다고 주장하지 않는다.')

evidence=json.loads((root/'output/260910/260910_03_info_selfcheck.json').read_text(encoding='utf-8'))
for row in evidence['artifacts']:
    assert hashlib.sha256((root/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
index=(root/'output/_index.md').read_text(encoding='utf-8').split(marker,1)[1]
seen=re.findall(r'^\| ([AB]/\d+) \(ID 미발급\)',index,re.M)
assert seen==evidence['expected_ids']
for target in re.findall(r'\]\((260910/[^)]+)\)',index):
    assert (root/'output'/target).is_file(),target
print('DRAFT-INDEX: 50/50 item rows; all links exist; 12 product hashes unchanged; release=BLOCKED.')
