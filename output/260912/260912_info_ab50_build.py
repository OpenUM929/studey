"""Render author's revision proposal. Does not update or approve revision4."""
import csv
import hashlib
import importlib.util
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('selfcheck',HERE/'260912_info_ab50_selfcheck.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def build():
    d=json.loads((HERE/'260912_info_ab50_reasoning.json').read_text(encoding='utf-8'))
    check=json.loads((HERE/'260912_info_ab50_selfcheck.json').read_text(encoding='utf-8'))
    assert check['data_sha256']==hashlib.sha256((HERE/'260912_info_ab50_reasoning.json').read_bytes()).hexdigest()
    base=mod.load_base(); made=[]
    for letter,number in [('A','14'),('B','15')]:
        stem=f'260912_{number}_info_{letter.lower()}_reasoning_proposal'
        header=f'''---
title: 정보 {letter}형 25제 — 사고력 보강 수정 후보
created: 2026-09-12
author: 메인 루프
executor: Codex/OMX
grade: proposal
subject_code: info
intended_use: practice
scope_confirmed: false
set_id: null
status: 검토필요
revision: reasoning-candidate-2-in-progress
---

# 정보 {letter}형 — 사고력 보강 25제

> ⚠️ 범위 미확정 · 수정 후보 · 미배포. 정식 Tier 및 기존 최고 수준 초과 여부는 독립 판정 전 미확정입니다. 정식 세트ID는 미발급입니다. 기존 revision4를 대체한 승인본이 아닙니다.

기존 {letter}형의 코드를 비교·수정 대상으로 재사용하고, 출력 추적 뒤 역조건·반례·수정 설계·정당화 문항을 새로 붙인 **개정 후보**입니다. 코드까지 모두 새로 만든 별개 신규 세트로 세지 않습니다. 함수·재귀는 학습지 근거이며 올해 공식 중간 시험범위 확정을 뜻하지 않습니다.

각 문항 4점(총100점): (1) 출력 전체1점, (2) 요구 결론·구성1점, 필수 근거2점. (2)는 부가 설명이 아니라 필수 답안입니다. 계산 결과만 쓰면 최대2점입니다. 구성형은 제시 조건을 모두 만족하는 다른 답도 인정합니다. 문제에 나온 파이썬 코드는 파이썬3을 기준으로 합니다. 일반 길이의 정당화는 실제로 큰 입력을 실행하라는 뜻이 아닙니다.

'''
        qs=[];ans=[];nov=[]
        for item in [x for x in d['items'] if x['id'].startswith(letter+'/')]:
            id=item['id'];n=id.split('/')[1];b=base[id]
            question=f"**{n}.** {b['title']}\n\n(1) 다음 프로그램의 출력 전체를 쓰시오. (1점)\n\n```python\n{b['code'].rstrip()}\n```\n\n(2) {item['question']} (3점)\n\n{b['tag']}\n\n답안: ____________________________________________________\n\n"
            qs.append(question)
            answer=f"### {n}. {id}\n\n**(1) 정답**\n\n```text\n{check['base_outputs'][id]}\n```\n\n**(2) 정답·해설**\n\n{item['answer']}\n\n**채점 기준(4점)**\n- (1) 출력의 값·순서 전체: 1점.\n- (2) 요구된 결론·입력·수정안을 조건에 맞게 제시: 1점.\n- (2) 위 해설의 핵심 관계 또는 상태 변화를 설명: 1점.\n- (2) 발문이 요구한 모든 경우의 포괄성·최소성·반례 대조·전제의 필요성 중 해당 근거까지 완결: 1점. 부분 점수는 서로 독립이며, 구성형의 다른 올바른 예도 동일하게 채점한다.\n\n**유형ID**: {b['tag']}\n\n**비교 근거**: {b['source']} — {n}번. 기존 개정 문항 위치이며 원천 비수치 축 인증을 뜻하지 않는다.\n\n**변경 근거**: {item['axis']}. 기존 {id} 대비. 원천까지 포함한 두 비수치 축 독립 검토는 미완료.\n\n"
            ans.append(answer)
            axis=item['axis'].split(';')
            nov.append([id,b['tag'],'기존 코드의 실행 의미',axis[0],axis[1],item['question'],b['source']+'#'+n,'REVIEW'])
        paths={
            HERE/(stem+'_questions.md'):header+'\n---\n\n'.join(qs),
            HERE/(stem+'_answers.md'):header+'## 정답·해설 및 채점 기준\n\n'+'\n'.join(ans),
            HERE/(stem+'.md'):header+'\n---\n\n'.join(qs)+'\n## 정답·해설 및 채점 기준\n\n'+'\n'.join(ans),
        }
        for p,content in paths.items():
            p.write_text(content,encoding='utf-8');made.append(p)
        p=HERE/(stem+'.novelty.tsv')
        with p.open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.writer(f,delimiter='\t');w.writerow(['item_id','type_id','invariant','non_numeric_axis_1','non_numeric_axis_2','structural_difference','nearest_prior','verdict']);w.writerows(nov)
        made.append(p)
        for p in paths:
            txt=p.read_text(encoding='utf-8')
            if not p.name.endswith('_answers.md'):assert re.findall(r'^\*\*(\d+)\.\*\*',txt,re.M)==[str(i) for i in range(1,26)]
            if not p.name.endswith('_questions.md'):assert re.findall(r'^### (\d+)\.',txt,re.M)==[str(i) for i in range(1,26)]
    result={'author':'Codex/OMX','status':'review-required','expected':[x['id'] for x in d['items']],
            'artifacts':[{'path':p.relative_to(mod.ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in made],
            'independent_review':False,'novelty':'50 rows REVIEW, not PASS','warnings':[],'exit_code':0}
    (HERE/'260912_info_ab50_build.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('proposal questions=50 answers=50 grading=50 novelty=50(REVIEW) artifacts=8 warnings=0 exit=0')

if __name__=='__main__':build()
