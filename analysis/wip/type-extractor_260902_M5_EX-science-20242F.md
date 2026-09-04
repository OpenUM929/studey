---
actor: type-extractor
task: M5_EX-science-20242F
target: corpus/EX-science-20242F/transcript.md (L17-18) + verify_log.tsv corrected row
status: done
updated: 2026-09-02
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | origin_data 실측 — `origin_data/EX-science-20242F/`는 존재하지 않음을 확인, 실제 원본은 `origin_data/2024_2학기_1학년_기말/2학기 기말고사 1학년 선택형정답.pdf`(단일 A4 페이지, 5과목 통합표) + `...서답형정답.pdf`(2쪽) | done | 스크래치패드 렌더 PNG(bf5/) | 원본 텍스트 추출은 CJK 폰트 cmap 깨짐 — 이미지 렌더+육안 판독으로 대체 |
| 2 | 선택형정답 PDF 통합과학 열 1~24번 배점 전건을 dpi 500~600 크롭으로 재열람, transcript.md 기존 열거값(3.5,3.4,3.0,...,3.6)과 1:1 대조 | done | 대조 결과: 열거값 자체는 PDF와 완전 일치, 산술합만 78.8→80.0 정정 필요 확인 | Counter 결과 3.0×4/3.2×4/3.3×4/3.4×4/3.5×4/3.6×4=80.0 |
| 3 | 서답형정답 PDF(2쪽) 통합과학 표 확인 — 배점 칸 없음(정답만 기재), 단답형 배점 근거로 사용 불가 확인 | done | subj_p1.png, subj_p2.png (스크래치패드) | 단답형 21.2→20.0은 기존 전사 열거값(3+2+2+3+2+3+2+3)의 산술 재계산으로 정정, PDF는 이 값을 반증하지 않음(근거 없음일 뿐) |
| 4 | `corpus/EX-science-20242F/transcript.md` L17(라벨 2개: 78.8→80.0, 21.2→20.0) + L18(배수표: 3.0×3/3.2×4/3.3×5/3.4×3/3.5×4/3.6×5 → 3.0×4/3.2×4/3.3×4/3.4×4/3.5×4/3.6×4) 정정, LF 개행 보존 확인 | done | `corpus/EX-science-20242F/transcript.md` | 분류 판단 없음 — 요약 라벨만 정정, 원문 열거값·문항 전사 불변 |
| 5 | `verify_log.tsv`에 `corrected` 행 append(8열, LF, 기존 43행 뒤에 44번째 행) | done | `corpus/EX-science-20242F/verify_log.tsv` | append-only, 기존 행 무변경 확인(lf count 43→44) |
| 6 | 수용기준 게이트 실행: `python tools/measure_score_bands.py`(파이프 없이 `$?` 확인) | done | exit=0; GATE 0 PASS undetected=0; GATE 1 PASS undetected=0; mismatches=0; EX-science-20242F got n=24 sum=80.0 want n=24 sum=80.0 OK | 도구 무수정, 원칙 12 준수 |

NEXT: 없음 — M5 완료. meta.yml은 요약 라벨(배점 합계) 값을 직접 인용하지 않아 수정 불필요로 판단, 무변경.
