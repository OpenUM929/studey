---
title: 정보 A/B50 배포 선행 수리 명세 초안
requested_by: main-loop
author: 메인 루프 (Codex/OMX)
grade: proposal
state: blocked
---

## 사용자 결정 기록
사용자 발언: 「이제 배포좀 해보자」. 직전 제시한 세 방향(현 원천 검사 모집단·불완전 자료의 검사/통계 적격성 분리 규약·정보 구조 기반 난이도 기준)의 수리안 작성 및 독립 판정 진행 승인으로 접수한다. 구체적인 경고 면제, 적용 코드 diff 또는 미검증 배포 승인을 받은 것으로 확대하지 않는다. 배포 요청을 다시 되묻지 않는다.

## 기준 판정 수령
근거: output/260911/rev/260911_03_info_ab50_ruler_ruling.md.
Q1/Q3 revise-required, Q2/Q4 경계·절차 approve. 수리 코드 반영 및 배포는 blocked. 본 문서는 판정이 허용한 읽기 전용 명세 준비이며 실행 패치·검증 완료물이 아니다.

## 1. Q1 구현 명세 후보
- 검사 모집단: 아래 현행 EX 디렉터리의 transcript/meta 바이트 동결표. 승인 후 manifest를 실제 원천에서 재생성하고 frozen 집합과 비교한다. 신규·삭제·수정 입력은 자동 수용하지 않는다.
- 통계 적격 여부는 별도 열로 관리한다. 선택형 비적용, 부분 자료, 선언 불일치, 합계축 미확인, 중복 후보를 하나의 제외 플래그로 합치지 않는다.
- regen derive의 고정 계층 개수 조건을 제거할 후보를 준비하되, 대체 조건은 원천 메타로 산출한 expected 계층 집합과 파싱한 observed 집합의 동등성 및 중복 없음이다. 상수 6 또는 측정기 출력에서 자기 기대값을 복사하는 구현은 불가.
- 목록 출력: expected/observed/duplicates/missing/extra. 합계는 계층→연도→ALL, Tier+outside 및 fit<=n을 정확산술로 검증한다.
- measure 비영 종료 및 미해결 경고는 regen/assurance까지 전파한다. 범위 확장만으로 기존 개별 문항의 score/r/Tier가 변하면 회귀 실패다.
- 루브릭 현재 수치만 원천에서 재생성한다. 역사 수치와 독립 목표값은 일괄 치환하지 않는다. ALLOW 확대는 별도 심사 대상이다.

## 2. Q2 상태 모델 후보 — 승인 전 적용 금지
| 차원 | 기록할 사실 | 현재 제안의 효력 |
|---|---|---|
| 원천 검사 | declared/extracted, 합계축 근거, 불일치 | 기존 FAIL과 WARN을 그대로 노출 |
| 통계 적격성 | 적용/비적용/부분/미확정 및 근거 | 검사 통과와 별개; 부분 관측을 완전 시험으로 표시하지 않음 |
| 역사 면제 | 해당 판정·해당 유닛·부분 활용 범위 | 다른 유닛 또는 전역 PASS로 전파 금지 |
| 배포 적격성 | 세트가 의존하는 기준과 독립 검증 | 통계가 계산됐다는 이유로 배포 승인 금지 |
이 분리는 현재 전역 게이트를 PASS로 바꾸지 않는다. 불완전 자료를 어떻게 처리해야 전역 규약이 만족 가능한지는 독립 판정에서 적용 단계·분모·상태별 종료 코드를 확정해야 한다. known duplicate 경고와 uncovered 문제도 각각 남는다. 이를 단순 WARNING→INFO 변경으로 숨기지 않는다.

## 3. Q3 별도 명세 작업의 경계
정보 서답형 기준은 선택형 4점과 동일시하지 않는다. 제안될 기준은 필수 사고 단계, 상태 의존성, 조건 경계, 오류 진단/일반화, 가장 가까운 원본 대비 필수 추가 사고의 증거를 요구한다. 이것들은 아직 공식 Tier 정의나 통과 기준이 아니다. 코퍼스 경계 사례와 독립 판정을 확보해 별도로 서명해야 한다. 최고 난이도는 기존 최고 수준+필수 추가 사고력을 유지한다. A/B50을 만족시키도록 기준을 역설계하지 않는다.

## 4. 구현 전 회귀 검증 명세
정상 입력, 계층 누락/중복/추가/동수 대체, 원천 유닛 삭제/추가/중복, 합계 불일치, 비적용/부분 혼동, 하위 exit1/WARN 전파, 현행 개별 score/r/Tier 보존을 검증한다. 기대 집합은 원천에서 유도하고 실행 제품이 자기 기대값을 고치지 못하게 한다. 각 결함은 독립 복제본/메모리에서만 주입하고 정상 오탐0·미검출0을 요구한다. 현재 테스트를 작성하거나 통과시켰다고 주장하지 않는다.

## 5. 독립 판정에 넘길 정확한 잔여
1. Q2 상태 모델의 원천 적격성·미해결 결함과 전역 성공 조건 사이 모순을 해결하는 구체 계약.
2. Q1 소스 manifest/계층 유도 구현의 정확한 diff 및 회귀·knockout 결과 승인.
3. Q3 기준 원천/경계 사례 및 별도 서명.
이번 명세는 1~3의 완료를 대체하지 않는다. 동일 작성 컨텍스트가 이를 독립 승인하지 않는다. 검사 명령은 기존 판정서 §2 Q4의 세 명령/계약을 소비하며 임의 수정하지 않는다.

## 다음 단계
이 명세의 상태 계약을 별도 깨끗한 Astra 컨텍스트에서 판정한 뒤, 승인된 계약하 패치 후보와 테스트를 준비하고 독립 패치 판정을 받는다. 그 후 두 키가 갖춰진 변경만 반영·재동결한다. A/B50 파일럿/전수 재검증 및 최종 배포 판정은 그 다음이다. 이 순서를 생략한 배포는 하지 않는다.

## 원천 inventory (기대값 정본 아님; 이번 실측 스냅숏)
| unit | transcript bytes | transcript SHA256 | meta bytes | meta SHA256 |
|---|---:|---|---:|---|
| EX-english-20241F | 46720 | 359c09da7842f5a0cdc716b42efc254c878d7b84e75fb409cb53933e1fd4c2ed | 382 | e14b74738e5e64e40bf031eaeb7ca133a885c322c1884c0900c2fed0e7c99939 |
| EX-english-20241M | 46751 | 842b287b87837dc28220055cbf2d5f5eff9986fa176c7f9eb0394e8d67d6f279 | 382 | beac7ed74f8fb9693e8532c9215a796f815bf3b3a60b6b45967cd38bbd61993d |
| EX-english-20242F | 57638 | 38a96c6e5aa1d2272e41826dc4448ef0e922bfb492c459255018f6e9c507a5a9 | 923 | b0e917a4df6c2a817f3516ed9373f899e1cef893a8f7e7102e8f60694f0e47e4 |
| EX-english-20242M | 57734 | c29d3ef592360b8695f2be9dc32e8d6d00e7e5626708487b7dbb7a87e6bb0b82 | 878 | d224aaeac7cd26035ad0ae7bb58b82f4e35e48acb10d4cebf46705e20e7e9d92 |
| EX-english-20251F | 55259 | 80042274dc869f5b37d535675ed231887e5e40e4e365a1a2d32b1f0f532a61d1 | 389 | bffc97abc43e936e677497c7ef00183de14d1d10fc1df9aaa725f4c478f1fcdb |
| EX-english-20251M | 45809 | 28fdfd0a65a7932652a238f073581ab56d55a93b6b9ccc75d171b4da5d25b2d2 | 389 | 55deb5709fc4a94ebdb552a2f66be4e24ec7b2ddd5eda471e1cffe48c5a0c927 |
| EX-english-20252F | 54395 | c320a939ba431432189c1a50ef8a507f914be5267252badef9294677c9066df7 | 361 | 2e7feda1975e893226dd0fa81c305e8de2551f36588b65e44be6f5dc11f2fc15 |
| EX-english-20252M | 51305 | 7c60c4fe031690bbcdd948970abf2c0bf654d72ba927ea3b2029a08502ee88f8 | 435 | d12ffff4b50a06ae60283010f2c94867ba6b600de50afd97d1ebbb07a69423f7 |
| EX-english-20261F | 54763 | 7f2cdc95cf34a8903493cc5b316cd8ac2185b925b8dd56d62336e0875b876999 | 4000 | 01a05692173186fc0e8424e1bf1822a18885765d967b7a2b5628409c582e7d78 |
| EX-english-20261M | 50149 | 33fde64cf038755874eb532f5473ce383e80cf12caa2dc454447d00cff37f6d4 | 3847 | 195ace6ebbcdad604a2e8bc64d8091d9388af8c00b60656ee4056c40d1b7ab6e |
| EX-history-20241F | 24518 | 05d8f8cbcd43fa80f4d4828d167c3f2177bb8d57837ce0d13a6a8d6f6b3eb4ed | 384 | 9357e4a8a0a1e3d4230534611ab4c1868268c0c9743173065f08c475745f7ee8 |
| EX-history-20241M | 23384 | 605a6d061162b558e2bb6e0361defdb665e0ee21e9916d1ac422ad881d7cf83e | 384 | 1e1e54aefee8b2437e67bd7d04f274bac32f7df532b28b97603fb647dedf94ee |
| EX-history-20242F | 41865 | bfff9aaf4b4077f0f2f9370df2a587c7a9c972c5963377e90e0434f224a19bfc | 963 | 9e89a7d3c2362000ebcec79517c222bf9c87c36ceca56221c77b67f639e7ec5b |
| EX-history-20242M | 39216 | f67b1f96d0505b59b9350968aacb61be03c51584b67d97bfb49e1ac4fdf3beab | 997 | 4658266cb3632d0bb5c675e1a595c6e95944f7745b4433b652d1d56b1396a7c5 |
| EX-history-20251F | 29139 | 00548ed4eb43b1a443f79a2ffd40031c5149464b8b665b641ec0c57a520c1e54 | 385 | cc44a9e66de5c147436f96c75057801a63e9827596dfc5e9e8d9d8ce5ad6a368 |
| EX-history-20251M | 27710 | 027cda44c645f2f600fdf2df7c5c566c5e7aa9f676ae72f5621af228b7d6e6ac | 385 | 8ea4b5643a3d990a839183cc221feb0c267c842ec662dd410976b5c157b9fbc4 |
| EX-history-20252F | 26277 | 26595f4c36436d5cceaa46d5bf884f7ea997801a0f398782ff55e2e441ec7df3 | 357 | ead51a75d29779330757c14a0f1314b121c8deb8681338b94109ef72e4c0f22c |
| EX-history-20252M | 25057 | e0ee96c8403a7e50059129a4ef5cdb944ae1cde04206f0e24383ee978ee7e5c9 | 357 | e1a8ee74e62ad74161ac1b0be3fd394ac4b482e7210f804b61dd859e6e531947 |
| EX-history-20261F | 37852 | 065cf1dbc1c5420ee5b1bb4a2f8da48efd4ff06a96feb5faa3d0d549bd264754 | 2936 | b380d4ae13c3cd4b24033291f7b8971b228ec90fb36298ac9dda0480cc31534b |
| EX-history-20261M | 34247 | 19409adaef5259a69f1c0f1c7dccaf7c251e59dd58dc0ff6e4da7bc46ef79701 | 3042 | 3dc0293de077e72139183883acd25c85b5793289cef86c87366502c6d0bab9db |
| EX-info-20252F | 10512 | fe07ad3612ce7054343d48f2e29accd48a68d3fa6b9edcb88528c2ce8fa8035e | 1905 | 6742859af13a5428689ed3975f036bd1515f1de4e709bb6ebbda470ef34b247a |
| EX-info-20252M | 8412 | bcd760fe017095b0683a9327e77c6597389c557b2a7b975b041704106861cb85 | 424 | 86b0458fc6c6f6ea3640e170b1c4f614d38fc57ac27cf466ccce308ffbc921e7 |
| EX-korean-20241F | 72799 | f8d80427344aa0dc1d50685f7ab0a25d71216266f1f2126e04ff3d9e52a4b853 | 381 | a2759e453ef90eebd3ef4a4755e195b2c7df5a026f2677b6137407161c96d3bf |
| EX-korean-20241M | 67713 | 8386f99b79d7c2399527d8b1d066c468a35ccbcdc0eb663aa7c7d8cbcc86dc82 | 381 | b4c83c8c260e860712157167fab6eb4c2f10d297d5bac58186ed0bf526e96fe4 |
| EX-korean-20242F | 75745 | 5f2bc589aaeb47d424b9eabf902fae283e81977e113d68b7b3b2e5adab1a4d91 | 518 | 66e102dc41c6de2fb34c6cad2224abb5343cc5283c4a2bc353948668145cfb49 |
| EX-korean-20242M | 65068 | 3b53aff6e2d83c3b5c9f72df746d5d59e2b0d44d034ece074753f5d7bb8ae6f6 | 950 | 54be57f74eddbafb280f77b2032955541fcc5f9b07f21644d46e2869a1e1b0e7 |
| EX-korean-20251F | 53701 | 31418f4f31a43d0ce4eae62db1c906811e00b181459e511e024520cbc2c47a44 | 388 | 7b7aa6c9bc6936a9ff1c507656a17cab239c002c60729f8a0aeebdee5ac012dd |
| EX-korean-20251M | 79841 | 11f2d18a4726f9c3adc9a2db954c698ee54847fec38c9193a4c8e277a0019af8 | 388 | e265649740ddc14acd7417ea31c3ef34f9ac4cdd370109986527881ae0f3d5a0 |
| EX-korean-20252F | 82077 | c543179ce05e34d02b03feac838f263f9ffed83f0d46a8bd2a64962b49002497 | 360 | 0c938a47fe0ef34ffca71e17a47d7d55664f0e20c4e8942a265f87c138b4cdac |
| EX-korean-20252M | 84171 | d5d8125181bea6c93de548fc7ae51f10096c6ea5da1a6d52ca3452ff90d96938 | 1688 | 49f88ae197f8e31160f348ff03ab0ed3200e687fae02924f15879c743a0dcfa0 |
| EX-math1-20241F | 6679 | bc7c62c3a58648e3e7ca35119919a31d1052e0bbe5cdc2d748a5dab804b4cfee | 379 | a05dd3e79e8dee3ee90c0f3339dfa2ff3d52da30e50fdadedfad4e5160c0acc0 |
| EX-math1-20241M | 7400 | 25b5eb75745649547661f85940e055ef99b9d9eaa2235026b90f31a083fa3266 | 379 | aa20499eebc8fa2f14b4300b3044d252c75edcdc5d10b5fb5d34f88c4470b36c |
| EX-math1-20242F | 11338 | 207128e4d8a10338de6538ce42dd33c096f1bb0556272f3118a4b0de3d17081a | 597 | 100ad6043346bfa06fcd57cfd3367d4cb087d6a5d6a05562f75804844f6b3e4a |
| EX-math1-20242M | 13883 | 070d330410de1cd73239d487c544354ba34c69a82a3b6fdf58e5b4135a43c80e | 627 | 1ddf5f8e5c5553e5c25c3c66ce9d8e705853cde9cc9c9267f7d48f3e05e3c8d8 |
| EX-math1-20251F | 8687 | 3f8325628401d6f16e5265c02b62efd2965bcc8abec11026fdc53c04199f2826 | 386 | 00fbfe4f5aba32be991735fe9a9844e8fba659f27c3502cdf2a583f5b4d673fa |
| EX-math1-20251M | 8022 | 966e3d13c2db6d52ff1298f195ca42d99e1c1de5e772b122f5714f6d78906345 | 386 | b11abe72ad3b81e086ed3d7440330908f35b3224d98013d73c30233301abcde9 |
| EX-math1-20261F | 17929 | 7c8305b123d80affd2ae516a359180bab4e68861941acdc1f633a39579480d81 | 4091 | 74185b42c20daa9762900ae7c65e7b528c83765f95f48d9b76f862a3231c8b53 |
| EX-math1-20261M | 18573 | 0f950f961b2be17c41de2fd85e0d19d197a73d57eaaf6f8cf4fb0469b08ac159 | 3845 | ba6645f1f779c98686327a0fb0bbc4261a374b7468634109a3395e108abf6c36 |
| EX-math2-20252F | 15058 | 580d5655566ae2abe234e46b48c4c71b2eeb40c1a23570ec770b0164aa1dd6ef | 413 | 832d888bb9b018906f80f80c54c0ba87c5310577ee9e6cc9e25a3a9ea8f5b12c |
| EX-math2-20252M | 8336 | 9e2ed478c120c790327eec4e68404bbfbf6e50028f099934b22803d3671744be | 384 | 976ad866e106401c607e93ea3e955f208743ff88e38fa10cc603b272af077450 |
| EX-science-20241F | 28362 | faa2c7f9b3601bc6bf78bdee4a935ef4185db2139d2709d8eb3e7f1297a2be9f | 387 | 796ca4dce2558f778fa7eeeb1e2e845df1e7c663c30767b959c74bafcc61d823 |
| EX-science-20241M | 24707 | d478a9aa95b65ad84a9b9b0b6d0c9096f35efc919141fa7ede4af4a641564735 | 387 | f8b59c59c95267823b034060f2e6571106e246c40fee7b97c1f0245f6f733159 |
| EX-science-20242F | 39812 | 04c409afe27b732f72310aa5f5b9813ea8eec9e3eb4cbd1ae0c0fcb331d94e11 | 503 | 50e59a9650ac2bd694e815e2f177e1f36f391f63cf7b961a667578a83d6e7211 |
| EX-science-20242M | 29981 | 04be3c40e25a1b21502e08dadadbff01c476d5e70bb21d84dc896e4462c6b3a9 | 462 | 1823eda57b61487a39d9118cee49914683fb5906c11a4d015dabc15499e3200e |
| EX-science-20251F | 26331 | 90143add4bb75ad2ef42bac687d0987cc5f205c47312564bbabf5a0708695e40 | 388 | be80489266c5818b5f9b2da408990c74e1f8ebd452af4cd0c2b1d991b502857b |
| EX-science-20251M | 25967 | ddbd9cb5c1d66bc935172ec751f3eece494e4646dbb944471c2e5eadc879dd4a | 388 | c378163dddb6c4911dac5e48b5f93f690ff70f320d765a90e77629a177a71b05 |
| EX-science-20252F | 25725 | d2788c7a36262adc622d661cc39aee93b154c79036b073f6b4c053d7fab2c2d7 | 367 | f78433a8924aaa135c760b495470acf6158eb4714b1c4822e972fa5e78fbc16c |
| EX-science-20252M | 31991 | 541d0a5bcc41d144cb58ccddec3fe01f7a102ada3f021282ceafb8a0fa1c01c6 | 428 | 2598226487f44977f2d570f2681a174f88162980a99099de6027fc28e6bd46e6 |
| EX-science-20261F | 41349 | 361532951a582237cfd806321f9c07b47c7ae2809dfe069f22a51339cbaa7e8c | 4753 | 8f54533a3a686f428855a278083ac6e1beccdba9f45b3e098cdc5bb2a550252f |
| EX-science-20261M | 47861 | 313f5ed4f50ccb3fcb020220ae08d297c475243a241f5e6c763d27aade80a85f | 4874 | a722fb0dc021460446cbb9dca661e2f16ed7121a6079a3dfc3816f0c0fa3d579 |
| EX-social-20241F | 28130 | 5af58b42b2774847bb202ff3196e8ba3b30fb6fd047668ecac0e4d207d1a1593 | 386 | 318d06fc6d7ec60f582692b3e5452a7ac501bbad1b6992f62b598809e9c73207 |
| EX-social-20241M | 31666 | 69e8707f12d24fb51acc307a66bf2b660438e36efc4ef9cc1a3f88e3447fa7d6 | 386 | f948a73599fb7c29742a3e9d05d340c071585bf07ea29bf4b0c60500db74cca1 |
| EX-social-20242F | 38669 | 49f7d257fd85fa088415896a70c1ed5e2e37a70c9b4f8d50a708ef150d7bf701 | 852 | b8509ee0a9ba498767531feb1d5658e0dda1dceffda600e9ca57d37047c81ab1 |
| EX-social-20242M | 45054 | 3e7fc678538e0ed0b1c1df103dd572e83c4685f6b87c3410fc727d16161bb3a8 | 854 | 420b3451893788b32a1ab1b113976fdeab6634fe98ae98f781069d38da4e5829 |
| EX-social-20251F | 27956 | 39737a4527339c4977e5de8376b3314a3f2b7dcfe917279ff9dbb35c75ed2289 | 387 | 35dbf0c0693c5bd4fc449ce516c82cca523a97416e1d292172193c90bdc12205 |
| EX-social-20251M | 27376 | 80a915d89664fd7cf58013fafc41308052966194fb04348f4da116930c4c1a89 | 387 | 8b68b6d8b06128a35b2ccec5c8f33dfaa137b4532e9b47030f149f34f54e2837 |
| EX-social-20252F | 25634 | ce1f7efc73f5f31e69510bddc0e56183eb5c04085d2cd11e8217a372a60838fc | 359 | 3fe424c22dfb4e0739c2998832f81f250f941807d754c827bf3c1547502f2618 |
| EX-social-20252M | 30293 | bcd14fefa2642492017741ea94af8cac67fe5fd3ce7d0c3ba9a3101f01a2bcad | 359 | 1be39403087e3739d03649bda6ac1f9902e6544e7e25ed78bc2557c52b17b4b4 |
| EX-social-20261F | 47598 | 67e3c525b27e97d37fab7a4b558b27becca5064865bc8491365f291aff755cac | 3069 | aeb50bb7e020597b2eab987696618c906ebfb4c9d66d1d2121c269c09ef2e3eb |
| EX-social-20261M | 36874 | 34868967890b7519abd9ab2fc68038495a5f762ac31789b015d4fcc009648b8d | 4948 | e2de8f9f251950cf18584ef172a501a4be86670d0586548dab8add36cd97ced3 |
