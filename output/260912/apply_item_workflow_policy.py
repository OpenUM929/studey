"""One-shot procedural update; preserves existing user edits via anchored textpatch."""
from pathlib import Path
import hashlib
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
from textpatch import read, patch

ROOT = Path(__file__).resolve().parents[2]
targets = ['AGENTS.md', 'CLAUDE.md', 'README.md', 'analysis/REV_GUIDE.md',
           '.claude/agents/item-writer.md', '.claude/agents/solve-back-verifier.md',
           '.claude/agents/item-quality-auditor.md', '.claude/agents/set-release-manager.md']
block = ('\n> **260912 문항 생성·배포 절차 우선 적용:** `docs/ITEM_DELIVERY_WORKFLOW.md`. '
         '기존 유형 기반 출제는 세트 전체 2~3라운드로 묶고, 체크포인트를 별도 승인·미세 발주 단위로 삼지 않는다. '
         '이 문서의 일반 라운드/분할 권장보다 해당 절차가 우선한다. 내용 검증·독립성·보호 자·append-only는 유지한다.\n')
protected = ['analysis/catalog/DIFFICULTY_RUBRIC.md', 'tools/measure_score_bands.py', 'tools/regen_rubric_values.py']
before = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in protected}
for rel in targets:
    p = ROOT / rel
    txt = read(p)[0]
    if '260912 문항 생성·배포 절차 우선 적용' in txt:
        continue
    anchor = next(line for line in txt.splitlines() if line.startswith('# ' ) or line.startswith('## '))
    patch(p, [(anchor + '\n', anchor + '\n' + block)])

p = ROOT / '.claude/agents/set-release-manager.md'
old = ('2. **게이트 단위 분할 발주** — G0~G8을 **1~2개 게이트씩** 끊어 발주하고, 각 슬라이스가 끝날\n'
       '   때마다 메인 루프가 산출물을 실측 확인한 뒤 다음을 낸다. 중간에 죽어도 완료분이 남는다.\n'
       '   **분할 발주가 이 배우의 기본 권장 형태다** — G0~G3(반영)과 G4~G8(생성·등록)이 자연스러운 경계다.')
new = ('2. **유계 작업으로 저장하며 진행** — 세트 배포를 한 작업으로 묶고 완료 증거를 저장한다.\n'
       '   실제 자원 한계가 확인될 때만 분할하며, G0~G8을 1~2개씩 발주하는 것을 기본값으로 삼지 않는다.\n'
       '   체크포인트 뒤에는 같은 승인 범위에서 계속한다. 문항 전용 절차는 `docs/ITEM_DELIVERY_WORKFLOW.md`를 따른다.')
if old in read(p)[0]:
    patch(p, [(old, new)])

p = ROOT/'tools/check_assurance_contract.py'
txt = read(p)[0]
anchor = 'TEXT_REQUIREMENTS = {\n'
addition = '    "docs/ITEM_DELIVERY_WORKFLOW.md": ["2~3라운드", "독립", "정답", "신규성", "3라운드", "two-key"],\n'
if addition not in txt:
    patch(p, [(anchor, anchor+addition)])
for rel in ('AGENTS.md','CLAUDE.md'):
    anchor = f'    "{rel}": [\n'
    txt = read(p)[0]
    if anchor+'        "docs/ITEM_DELIVERY_WORKFLOW.md",\n' not in txt:
        patch(p, [(anchor, anchor+'        "docs/ITEM_DELIVERY_WORKFLOW.md",\n')])

after = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in protected}
assert before == after, 'protected ruler changed'
print('policy links: 8; protected rulers unchanged: 3')
for p,h in after.items(): print(p, h)
