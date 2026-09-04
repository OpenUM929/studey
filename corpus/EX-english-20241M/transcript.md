# transcript — EX-english-20241M

- 원본: `origin_data/2024_1학기_1학년_중간/2024_1학기_중간_1학년_영어_고사원안.hwp`
- 전사 기준: `tools/hwp2md.py` 변환 텍스트(hwp5html 경유 — 표 내용과 이미지 마커 보존).
- 전사 방식: 변환 텍스트를 축자 보존하고, 문항수·배점표식·이미지 참조를 **원문 선언과 대조**한다.
  **이미지 내용·정답·유형 판단은 하지 않는다** (CLAUDE.md 원칙 1 — 1차 정제 = 전사).
- 생성: `tools/build_corpus_unit.py` (결정론적 재현 가능, 원칙 12-b).
- 개행: 변환 텍스트의 CRLF 를 **LF 로 정규화**했다(내용 무변경 — 혼합 개행 파일이 되면 앵커 편집 한 번이 전면 재작성이 된다). 기존 코퍼스 유닛도 LF 단일이다.

## 0. 사실 header

- 인쇄 선언: 총 11쪽, 선택형 26문항, 서답형 6문항.
  - 선언 원문: `◑ 총( 11 )쪽, 선택형( 26 )문항, 서답형( 6 )문항`
- 실측 배점 표식: **32건** (`[3.0 점 ]`·`(2.8점)` 두 계열 모두 계수. 서답형 소문항 배점이 섞이므로 문항 수 이상일 수 있고, **미만이면 격차**로 잡는다).
- 본문 번호 문항(`n.` 행머리): **26건**.
- 실측 서답형 문두(`[ 서술형n ]`·`[ 서답형n(단답) ]` 등 실측 24형태): **6건**.
- 이미지 참조: 1회 / 고유 1건 / bindata 파일 1건.

## 1. 이미지 참조 대조

- `[[BIN0001.jpg]]` → `corpus/_images/EX-english-20241M/bindata/BIN0001.jpg`

## 2. 원문 전사 (변환 텍스트 보존)

```text
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
영어과
제 1학기 중간고사 문제지

| 결 재 | 교과과장 | 부 장 | 교 감 |

제 1학년 전체 2024년 5월 2일 1교시 출제자: 이의리 인
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
2024학년도 1학기
( 1 )학년 ( 영어 )과 중간고사 문제지
◑ 총( 11 )쪽, 선택형( 26 )문항, 서답형( 6 )문항
◑ 서답(서술) 답안 작성 : 별도의 답안지
◑ 고사반영 비율 : 중간고사(30)%, 기말고사(30)%, 수행평가(40)%

| 유의사항 1) 문제지를 받은 후 문제지 쪽수, 인쇄 상태, 문항 수(선택형, 서답형)를 확인하시오. 2) 해당 답안지에 학번, 이름, (교과명) 을 쓰고 정확히 표기하시오. 3) OMR 카드 작성 시 카드가 훼손되지 않도록 주의하시오.(불이익을 받을 수 있음) 4) 문항에 따라 배점이 다르니, 각 물음의 끝에 표시된 배점을 참고하시오. 5) 서답형(서술형) 답안지 작성 관련 사항 ① 답안 작성 지시사항에 따라 해당 답안지에 작성 ② 필기구 : 검정색과 청색 펜으로만 작성(미준수 시 불이익을 받을 수 있음 ) |

| ※ 시험이 시작되기 전까지 표지를 넘기지 마시오. |

[[BIN0001.jpg]] 상 산 고 등 학 교
본 시험문제의 저작권은 상산고등학교에 있습니다. 무단 전송 · 복제, 배포 시 저작권법에 의거 처벌될 수 있습니다. [ 11 - 4 ]
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
영어과
제 1학기 중간고사 문제지

| 결 재 | 교과과장 | 부 장 | 교 감 |

제 1학년 전체 2024년 5월 2일 1교시 출제자: 이의리 인
영어과 제 1학기 중간고사 문제지 제 1학년 전반 2024년 5월 2일 1교시
선택형, 서답형 문항
1. 다음 문장이 들어가기에 가장 적절한 곳은? [2.5 점 ]

| But these disciplines also provide a good foundation for continued study in graduate school. |

Both business and engineering are viewed as majors that will help students launch their careers after graduation. ( ① ) Many students who pursue an MBA feel that the best way to get into a good program is to study business and management in college. ( ② ) Students who want to get a graduate degree in engineering will have a hard time with the subject if they have not already taken engineering courses in college, which is different from degrees more oriented toward the humanities. ( ③ ) Finally, both areas require the use of mathematics. ( ④ ) Business majors will need to be able to work with budgets and financial and accounting ideas, and engineers rely on mathematical calculations for their work. ( ⑤ )
[ 서답형1(단답) ] 다음 글을 읽고, <답안>과 같이 정리하고자 할 때, 빈 칸 안에 들어갈 말을 <조건>에 맞추어 쓰시오. [(A)2 점,( B)3 점, 총 5점 ]
Perhaps the most important decision a college student has to make is what subject to major in. Most colleges offer a wide variety of interesting subjects from which to choose, so for some students the choice can be difficult. Some students want to follow their academic interests and major in something that is not directly linked to a future career, such as history or philosophy. Others are looking for a degree in a practical subject that provides concrete skills for the working world. For these students, subjects like business and engineering are attractive options. Despite this common ground, however, there are significant differences between these two majors in terms of their popularity and the gender ratio of students.

|  | < 조 건 > |  |
| (1) (A), (B) 모두 한 단어로 쓸 것. (2) (A), (B) 모두 윗글에서 찾아 변형없이 쓸 것. |

|  | < 답 안 > |  |
| Business and engineering differ in regards to (A) and the gender gap, while both are sought after by individuals pursuing a degree in (B) disciplines. |

[2-3] 다음 글을 읽고, 물음에 답하시오.
In terms of gender balance, many college majors are commonly more popular with one gender than the other, but business majors are split about evenly between male and female students. When asked why they have chosen business, many women say that they want to study something that makes them employable but that also focuses on communication skills. In the case of engineering, which has less of a focus on communication skills, only 14% of students are women, according to the American Society of Engineering Education . Engineering is the E in the acronym STEM, which stands for science, technology, engineering, and mathematics. For male students, engineering is the most popular STEM major, while for female students it is biology. There are different theories about why women are so underrepresented in engineering, and in STEM in general. Some people think that it is simply because fewer women are interested in these fields, while others think that young girls may be discouraged by parents, teachers, and society in general from pursuing STEM occupations. Even though women make up 47% of all U.S. employees, only 14% of engineers are women. In certain fields, such as mechanical engineering, the percentage is even less than 10%.
2. 위 글의 제목으로 가장 적절한 것은? [2.5 점 ]
① What Biological Aspects Distinguish Male From Female
② Gender Disparity in Major Preferences and Its Reasons
③ A Common Ground That Business and Engineering Share
④ Engineering and STEM Making Efforts to Engage More Women
⑤ Gender Gap Shifting the Entire Nation, Leaving Gender Conflicts Behind
3. 위 글의 내용과 일치하는 것은? [2.9 점 ]
① Women account for almost half of business students, which is similar to most college majors.
② Female students in biology say that they choose their major not only for future employment but also for communication skills.
③ Women make up less than 10 percent of engineering students in a college.
④ Among STEM majors, engineering is the most popular for males, while biology is the most popular for females.
⑤ According to a theory, it is parents, teachers, and society in general that encourage young women to pursue STEM career.
[4, 서답형2 ] 다음 글을 읽고, 물음에 답하시오.
In 1810, a German physician named Saumuel Hahnemann published an overview of his medical theories and research in a book titled The Organon of the Healing Art , which stated that consuming a substance that causes the symptoms of an illness could cure that illness. This was the birth of homeopathy. Ever since then, many people have tried this alternative treatment and found success with it. Often, homeopathic treatment is less expensive than conventional medicine, since it is made from plants and other natural substances. Also, but perhaps less importantly, over 400 doctors in the United States regularly recommend homeopathic treatments. Since they are cheap and popular, I find it difficult to understand why Medicare and Medicaid do not fund them. Why shouldn ’ t people be allowed to make their own health choices? They have this freedom in other aspects of their lives – for example, which school to send their children to – so why not in terms of their healthcare? As for the critics who argue that homeopathy doesn ’ t work, I could give hundreds of examples of patients who have been cured by my treatment. On top of that, there ’ s plenty of research that shows the benefits it can bring. Homeopathy wouldn ’ t have survived so long if it were complete nonsense. It has much more than just a placebo effect. Too much emphasis is sometimes put on providing “ proof ” of why something works. Belief is just as powerful.
4. 위 글의 내용과 일치하지 않는 것은? [2.9 점 ]
① The concept of homeopathy originated from a book which stated that taking a substance inducing symptoms of a disease could heal that ailment.
② Homeopathic treatment has many successful cases, with the therapy costing less than conventional medicine.
③ More than 400 doctors in the U.S. frequently suggested homeopathic remedies.
④ The writer advocates the individuals ’ freedom to make health decisions on their own, just as people choose many other aspects of their lives.
⑤ The writer refutes the opponent who doubt efficacy of homeopathy, pointing out the fact that its practice did not survive for a long time.
[ 서답형2(서술) ] 위 글의 “ Belief is just as powerful ” 이 의미 하는 바를 <답안>과 같이 정리하고자 할 때, 다음 빈 칸 ( A), (B) 에 들어갈 말을 <조건>에 맞추어 쓰시오. [(A) 1 점, ( B) 3 점, 총 4점 ]

|  | < 조 건 > |  |
| (1) (A) 는 한 단어로 쓸 것. (2) (B) ‘ 의문사절 ’ 을 활용할 것. |

|  | < 답 안 > |  |
| The writer emphasizes the trust in the efficacy of (A) , even though (B) has yet to be proven. |

5. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은? [2.5 점 ]
In countries where citizens use private providers, health care is only available to patients who pay for it, and health care providers are commercial companies. In wealthier countries, most citizens take out health insurance to cover their potential medical costs.
(A) In other nations, there is no such safety net, and those who cannot pay simply do not get the health care they need, unless they can get help. The disadvantages of this system are obvious.
(B) People are not only deprived of the medical attention they need, but also the lack of preventative medicine contributes to the rapid spread of infectious diseases. One advantage, however, is that commercial organizations can sometimes provide higher-quality care than struggling government-funded ones.
(C) However, not everyone can afford this, and some governments have a program that gives financial assistance to those who need urgent medical care but are unable to afford it.
① ( A)-(C)-(B) ② ( B)-(A)-(C) ③ ( B)-(C)-(A)
④ ( C)-(A)-(B) ⑤ ( C)-(B)-(A)
6. 다음 글의 내용과 일치하지 않는 것은? [ 3.2점 ]
Although many people think it is a modern phenomenon, distance learning has been around for at least 200 years in one form or another. Historical examples of long-distance learning include students being sent a series of weekly lessons by mail. The technological advances of the past 20 or so years, however, have meant that this form of education is now a credible alternative to face-to-face learning. Indeed, 1996 saw the establishment of the world ’ s first “ virtual university ” in the United States, showing how far distance learning has come in a relatively short space of time. When comparing the two systems, the most obvious difference lies in the way that instruction is delivered. Distance learning is heavily dependent on technology, particularly the Internet. In a face-to-face course, students may only require a computer for the purpose of writing an essay. In comparison, when learning remotely, technology is the principal means of communication. Face-to-face instruction must take place in real time and in one location. Conversely, distance learning can happen at any time and in any location, since the learning is not restricted by geography. The flexibility this provides means that students may be better able to learn at their own pace, but it may also mean that learners have to be well organized and self-disciplined. In other words, they must be more highly motivated in order to do well in distance-learning courses.
① Despite the common belief that distance learning is a recent trend, it has been in existence for at least 200 years in diverse forms. One historical example includes students receiving weekly lessons through mail.
② Technological improvements over the last 20 years have allowed distance education to be a reliable alternative to face-to-face instruction.
③ The main distinction between face-to-face and distance learning is the delivery method of instruction. Remote learning relies heavily on technology, which also serves as the primary communication tool in traditional learning in general.
④ Face-to-face classes occur in real time and in a fixed location, while virtual classrooms allow students to learn anytime and anywhere without geographical restriction.
⑤ Distance learning allows flexibility in time and place, enabling students to learn at their own pace, but it demands higher levels of self-organization and motivation.
[ 서답형3(서술) ] 다음 글 [B] 는 글 [A] 를 작성한 저자와 학생 간의 대화이다. 다음 글을 읽고 글 [A] 의 필자가 학생에게 했을 조 언을 아래 <조건>에 맞게 영어로 서술하시오. [6 점 ]
[A]

| Although the nature of the teacher-student relationship may differ in face-to-face leaning and distance learning, they do share the same core principles. Just as a teacher is the “ knower ” in the classroom, he or she is the one responsible for helping students understand the key sections of an online course. In any case, all the usual elements of the teacher ’ s role are necessary, no matter what kind of instruction is being used. It is difficult to state whether one form of learning is better than another, since they are geared toward different learning situations. They are certainly different experiences. Nevertheless, there are strong similarities between the two systems, which can both produce positive results. A student who has the choice need to consider the advantages and disadvantages of each method before deciding to take a course. |

[B]

| Student A: Hi. I am trying to take a Computer Engineering course this year. The class is available both online and offline. So, I was wondering which learning method suits me the best. Can you recommend one? Author: Well, it ’ s hard to say because teachers play the same role in both learning methods and both methods are designed for distinct learning situations. Rather than asking me about which form of learning is better, I believe . |

|  | < 조 건 > |  |
| (1) 다음 표현을 모두 포함하여 완전한 문장으로 작성할 것. (단, 형태는 변형하지 말 것) it / each approach / drawbacks / benefits / should weigh / that / the student with the choice (2) It~ that 강조구문을 활용할 것 (3) 단어 추가는 가능하되 16단어 이내로 작성할 것. |

|  | < 답 안 > |  |

7. 다음 글 [A], [B] 를 읽고, 글의 내용과 가장 일치하지 않는 것을 고르면? [3.2 점 ]
[A]

| Within the countries that provide free public health care, there are many models. In some countries, consultations, treatment, and medicines are free to all citizens. This may be paid for directly by the government, perhaps funded by the country ’ s valuable natural resources that the government owns. Other countries collect money from citizens through taxes based on their income. Workers pay according to how much they earn, and employers also make a contribution. Hospitals and other medical services are then provided and run by the government. There may also be some private medical services that people can choose to buy. The advantage of systems such as these is clear: free basic health care for all, regardless of income. However, it is a very expensive system and, as life expectancy and costs rise, many countries are facing either an unsustainable financial burden, or a drop in the quality of services and facilities provided. |

[B]

| John K : It ’ s crazy to have citizens in a free country pay such high prices for healthcare. The system must change! Only the government can help pay the cost of medical care for its citizens. Becky : People need to take care of themselves. My tax dollars can go to better things than paying for you if you ’ re sick. I wouldn ’ t want you to pay for me! |

① Free public medical services are financially supported by either invaluable government resources or income-based taxes.
② Residents can use hospitals and other medical services run by the government, or if they foot the bill, they can also use some private medical care.
③ The merit of free public healthcare is that free basic healthcare is available to every citizen, no matter how much they earn.
④ Due to the rising life expectancy and costs, many nations suffer from unsustainable financial burden, with the quality of services and facilities maintained.
⑤ Based on [B], John K is more likely to support the system stated in the passage [A] than Becky is.
8. 다음 글 [A], [B] 를 읽고, 밑줄 친 This system 에 대한 설명으로 옳지 않은 것을 고르면? [3.4 점 ]
[A]

| In many countries, there is a mix of public and private funding. This system requires all its citizens to take out health insurance. This is deducted from salaries by the employer, who also has to make a contribution for each worker. Citizens are able to choose their health care providers, which may be public or private. However, in some systems, private companies are not permitted to make a profit from providing basic health care. This model provides more flexibility than either the public or private models, and ensures access to health care for all. However, it has been criticized for driving up the cost of labor, which can lead to unemployment. |

[B]

| In Germany, most workers have to pay for government health insurance from their salaries or buy insurance on their own. Also, in the Democratic Republic of Congo, many people do not have access to a doctor and in some areas there is an insufficient supply of medicine. Doctors are typically paid in cash, and even those who do manage to see a doctor often cannot afford the treatment. |

① Taking out health insurance is mandatory for all citizens and they can select either public or private health providers.
② Employers not only deduct health insurance from workers ’ wages but also contribute on behalf of each employee.
③ It has greater flexibility than either the public or private model and it guarantees that everyone has access to healthcare.
④ It has been criticized for increasing the cost of labor, which can result in layoffs.
⑤ According to the features mentioned in [A], both Germany and the Democratic Republic of Congo in [B] are good examples of this system.
9. 다음 글의 제목으로 가장 적절한 것은? [2.5 점 ]
It is hard for street trees to survive with only foot-square holes in the pavement. The average life of a street tree surrounded by concrete and asphalt is seven to fifteen years. Many factors underground determine if a street tree will make it. If the soil is so dense that the roots cannot get in, it will surely die. If they can get in, there is a better chance of getting the water and nutrients needed to survive. Another question is whether adequate water supplies are getting into the growing area. Some of the water comes from underground sources and some from rain, and it is hard to measure where the tree is getting it. Of course, if the roots get into the sewers, they can get everything they need.
① Who Will Make It: Street Trees vs Forest Trees
② Biodiversity: Key Ingredients for Trees to Make It
③ Getting Enough Water: The Best Strategy for Trees
④ Elements Below the Surface: Keys to Street Trees ’ Survival
⑤ Water and Soil: Current Challenges Forests Are Faced With
10. 다음 글의 제목으로 가장 적절한 것은? [ 2.7 점 ]
The mind has parts that are known as the conscious mind and the subconscious mind. The subconscious mind is very fast to act and doesn ’ t deal with emotions. It deals with memories of your responses to life, your memories and recognition. However, the conscious mind is the one that you have more control over. You think. You can choose whether to carry on a thought or to add emotion to it and this is the part of your mind that lets you down frequently because — fueled by emotions — you make the wrong decisions time and time again. When your judgment is clouded by emotions, this puts in biases and all kinds of other negativities that hold you back. Scared of spiders? Scared of the dark? There are reasons for all of these fears, but they originate in the conscious mind. They only become real fears when the subconscious mind records your reactions.
① Positivity vs. Negativity: Silent Battles for Memories
② Reactions Over Emotions: How Our Body Affects Our Mind
③ F rom Recognition to Fears: The Power of Positive Thinking
④ The Mind's Dependence on Emotions Prevents Being Prejudiced
⑤ Subconscious Mind: The Real Keeper of Memories of Responses
11. 밑줄 친 as unrevealed information it remains socially inactive 가 다음 글에서 의미하는 바로 가장 적절한 것은? [2.7 점 ]
To begin with a psychological reason, the knowledge of another ’ s personal affairs can tempt the possessor of this information to repeat it as gossip because as unrevealed information it remains socially inactive . Its possessor can turn the fact that he knows something into something socially valuable like social recognition, prestige, and notoriety only when the information is repeated. As long as he keeps his information to himself, he may feel superior to those who do not know it. But knowing and not telling does not give him that feeling of “ superiority that, so to say, latently contained in the secret, fully actualizes itself only at the moment of disclosure. ” This is the main motive for gossiping about well-known figures and superiors. The gossip producer assumes that some of the “ fame ” of the subject of gossip, as whose “ friend ” he presents himself, will rub off on him.
① keeping someone ’ s private information to oneself and not revealing it to others leaves the information without any social impact or recognition
② the well-known figures will always feel superior simply by listening to the information about themselves, even if it is fake gossip
③ information about someone, even when shared, will not affect the social environment or relationships at all
④ concealing the information of others will have a negative impact on the social reputation of people who possess it
⑤ t he information of others ’ personal affairs becomes reality regardless of its disclosure to others
*다음장에도 문제가 있습니다.
12. 밑줄 친 that threshold is reached 가 다음 글에서 의미하는 바로 가장 적절한 것은? [ 2.6 점 ]
Scholars of myth have long argued that myth gives structure and meaning to human life; that meaning is amplified when a myth evolves into a world. A virtual world ’ s ability to fulfill needs grows when lots and lots of people believe in the world. Conversely, a virtual world cannot be long sustained by a mere handful of adherents. Consider the difference between a global sport and a game I invent with my nine friends and play regularly. My game might be a great game, one that is completely immersive, one that consumes all of my group ’ s time and attention. If its reach is limited to the ten of us, though, then it ’ s ultimately just a weird hobby, and it has limited social function. For a virtual world to provide lasting, wide ‑ ranging value, its participants must be a large enough group to be considered a society. When that threshold is reached , psychological value can turn into wide ‑ ranging social value.
① historical evidence makes the myth plausible
② individual values are applied to all of their affairs
③ people who have faith in the world grow sufficiently
④ the selected elite gains a high level of understanding
⑤ the religious value system gets approval from the society
13. 다음 글의 밑줄 친 부분 중, 어법상 틀린 것은? [2.4 점 ]
Here ① are the results of a 2019 survey on the views of American age groups on targeted online advertising. In total, 51% of the respondents said targeted ads were intrusive, with 27% ② saying they were interesting. The percentage of respondents who believed that targeted ads were interesting was the highest in the age group of 18 to 24. The percentage of respondents aged 25 to 34 who said that targeted ads were intrusive was the same as ③ that of respondents aged 45 to 54 who said the same. Among all age groups, the gap between respondents who said targeted ads were interesting and those who believed them to be intrusive ④ were the largest in the 55 and above. The age group of 55 and above was the only group ⑤ where the percentage of respondents who believed targeted ads were intrusive was more than 50%.
14. 다음 글의 밑줄 친 부분 중, 어법상 틀린 것은? [2.4 점 ]
North America ’ s native cuisine met the same unfortunate fate as its native people, save for a few relics like the Thanksgiving turkey. Certainly, we still have regional specialties, but not only does the Carolina barbecue ① have California tomatoes in its sauce, but the Louisiana gumbo is just as likely to contain Indonesian-farmed shrimp. If one of these ② shows up on a fastfood menu with lots of added fats or HFCS, we seem unable either to discern or resist the corruption. We have yet to come up with a strong set of generalized norms, passed down through families, for savoring and sensibly consuming ③ what our land and climate give us. We have, instead, a string of fad diets ④ convulsing our bookstores and bellies, one after another, at the scale of the national best seller. Nine out of ten nutritionists view this as evidence ⑤ which we have entirely lost our marbles.
15. 다음 중 문맥상 낱말의 쓰임이 적절한 것끼리 짝지어진 것은? [2.5 점 ]
The idea that people expose themselves to news content based on their preference has been around for a long time, but it is even more important today with the fragmentation of audiences and the proliferation of choices. (A) [ Selective / Entire ] exposure is a psychological concept that says people seek out information that conforms to their existing belief systems and avoid information that challenges those beliefs. In the past when there were (B) [ many / few ] sources of news, people could either expose themselves to mainstream news - where they would likely see beliefs expressed counter to their own - or they could avoid news altogether. Now with so many types of news constantly available to a full range of niche audiences, people can (C) [ easily / hardly ] find a source of news that consistently confirms their own personal set of beliefs. This leads to the possibility of creating many different small groups of people with each strongly believing they are correct and everyone else is wrong about how the world works.

|  | (A) |  | (B) |  | (C) |
| ① | Selective | … | many | … | hardly |
| ② | Selective | … | few | … | easily |
| ③ | Selective | … | few | … | hardly |
| ④ | Entire | … | few | … | easily |
| ⑤ | Entire | … | many | … | hardly |

16. 다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은? [3.1 점 ]
Investigating the history of distance education reveals both diversity and an ongoing change in its practice. Historically, diverse practices of distance education have been developed according to the resources and philosophies of the organizations providing instruction. The history also shows that advances in technology have ① promoted key changes in distance education. These changes have been most evident in the rapid development of electronic communications in recent decades. How the future of distance education will be shaped by the integration of its history and these new technologies is yet to be seen. Changes in society, politics, economics, and technology are impacting the status of distance education around the world. In some cases, distance education is seen as an answer to ② inadequate educational opportunities caused by political and economic instability. In other situations, established distance education providers are being required by a changing society to convert from mass instruction to a more decentralized approach to ③ meet the diverse needs of their students. In many countries, the need for continuing education or training and access to degree programs is ④ suspended by the demands of a changing society. Students in rural or isolated parts of the world look to distance education for opportunities to "keep up" with the outside world. Again, technology advances are a ⑤ major influence for change in distance education worldwide. The globalization of the world enabled by these new technologies will challenge distance educators to rethink the practice of distance education to take advantage of these new opportunities.
17. 다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은? [ 2.5 점 ]
Many early dot ‑ com investors focused almost entirely on revenue growth instead of net income. Many early dot ‑ com companies earned most of their revenue from selling advertising ① space on their Web sites. To boost reported revenue, some sites began ② exchanging ad ground. Company A would put an ad for its Web site on company B ’ s Web site, and company B would put an ad for its Web site on company A ’ s Web site. No money ever changed hands, but each company recorded revenue (for the value of the space that it gave up on its site) and ③ expense (for the value of its ad that it placed on the other company ’ s site). This practice ④ scarcely boosted net income and resulted in no additional cash inflow ─ but it did boost reported revenue. This practice was ⑤ sustained because accountants felt that it did not meet the criteria of the revenue recognition principle.
18. 다음 빈칸에 들어갈 말로 가장 적절한 것은? [ 2.3 점 ]
Managers frequently try to play psychologist, to figure out why an employee has acted in a certain way. Empathizing with employees in order to understand their point of view can be very helpful. However, when addressing a problem area, in particular, remember that it is not the person who is bad, but the actions exhibited on the job. Avoid making suggestions to employees about personal traits they should change; instead suggest more acceptable ways of . For example, instead of focusing on a person ’ s “ unreliability, ” a manager might focus on the fact that the employee “ has been late to work seven times this month. ” It is difficult for employees to change who they are; it is usually much easier for them to change how they act.
① performing ② concentrating ③ believing
④ personalizing ⑤ playing
*다음장에도 문제가 있습니다.
19. 다음 빈칸에 들어갈 말로 가장 적절한 것은? [ 2.5 점 ]
One of the most striking characteristics of a sleeping animal or person is that they . If you open the eyelids of a sleeping mammal the eyes will not see normally ― they are functionally blind. Some visual information apparently gets in, but it is not normally processed as it is shortened or weakened; same with the other sensing systems. Stimuli are registered but not processed normally and they fail to wake the individual. Perceptual disengagement probably serves the function of protecting sleep, so some authors do not count it as part of the definition of sleep itself. But as sleep would be impossible without it, it seems essential to its definition. Nevertheless, many animals including humans use the intermediate state of drowsiness to derive some benefits of sleep without total perceptual disengagement.
① adopt a fully awakened state
② show a lack of response to stimuli
③ respond normally to environmental stimuli
④ become more sensitive to visual information
⑤ are deprived of the chance to cooperate with others
20. 다음 빈칸에 들어갈 말로 가장 적절한 것은? [ 3.1 점 ]
Doctors and patients certainly should consult guidelines since they provide considerable background information about disorders and treatment options. But, it's important to recognize that guidelines aren't strictly "scientific." They . Experts select which clinical studies to use and which to discard when they formulate their recommendations. Further, all studies have limitations. They provide results from statistical averages of selected groups of study subjects. These averages may not be applicable to a particular patient. Even the most rigorous, inclusive studies cannot address all the variables of age, gender, genetics, lifestyle, diet, and concurrent medical conditions that make us individuals and often influence how effective a particular treatment will be or what sorts of side effects we might experience. Many studies exclude the elderly or those who have coexisting common medical problems. When making their final recommendations about the need for treatment, experts also apply their own personal evaluation about how much risk is worth taking in order to obtain a certain benefit. Concerns have also been raised by the Institute of Medicine about potential conflicts of interest, since some experts who write guidelines are consultants to drug and device companies or private insurers. Finally, guideline committees have an imperative for consensus and present their recommendations with one voice. As a result, their conclusions usually fail to mention dissenting opinions that may have arisen among committee members.
① redefine the concept of scientific guidelines
② include some biases and subjective judgments
③ underestimate the comprehensive coverage of research
④ embrace others ’ criticism in the pursuit of accuracy
⑤ account for potential side effects of a particular treatment
*다음장에도 문제가 있습니다.
21. 다 음 글에서 전체 흐름과 관계 없는 문장은? [2.4 점 ]
When we think of leaders, we may think of people such as Abraham Lincoln or Martin Luther King, Jr. ① If you consider the historical importance and far-reaching influence of these individuals, leadership might seem like a noble and high goal. ② But like all of us, these people started out as students, workers, and citizens who possessed ideas about how some aspect of daily life could be improved on a larger scale. ③ Educational leaders have to engage teachers, students, parents, and even wider communities daily. ④ Through diligence and experience, they improved upon their ideas by sharing them with others, seeking their opinions and feedback and constantly looking for the best way to accomplish goals for a group. ⑤ Thus we all have the potential to be leaders at school, in our communities, and at work, regardless of age or experience.
22. 다음 글에서 전체 흐름과 관계 없는 문장은? [ 2.5점 ]
Sellers often have information about the quality of a good or service that they do not make available to consumers. ① Sellers of used cars have information about the car ’ s quality that they are unlikely to reveal to potential buyers if the car has a defect. ② The manufacturers adjust the quality of their cars to meet the budgets of buyers from different walks of life. ③ In a free and unregulated market, sellers of food could sell products that are unsafe for human consumption, possibly leading to illness and even death. ④ Sellers of medicines could sell unsafe medications that could be ineffective to human health. ⑤ Individuals claiming to be doctors, some of whom have little training, could practice medicine and even surgery, resulting in huge costs in terms of human health and safety.
23. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은? [ 2.5점 ]

| Agriculture includes a range of activities such as planting, harvesting, fertilizing, pest management, raising animals, and distributing food and agricultural products. |

(A) It is one of the oldest and most essential human activities, dating back thousands of years, and has played a critical role in the development of human civilizations, allowing people to create stable food supplies and settle in one place.
(B) As the world ’ s population continues to grow, it is essential to find sustainable solutions to address the challenges facing agriculture and ensure the continued production of food and other agricultural products.
(C) Today, agriculture remains a vital industry that feeds the world ’ s population, supports rural communities, and provides raw materials for other industries. However, agriculture faces numerous challenges such as climate change, water scarcity, soil degradation, and biodiversity loss.
① ( A)-(C)-(B) ② ( B)-(A)-(C) ③ ( B)-(C)-(A)
④ ( C)-(A)-(B) ⑤ ( C)-(B)-(A)
24. 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은? [ 2.5 점 ]

| It seems natural to describe certain environmental conditions as ‘ extreme ’, ‘ harsh ’, ‘ benign ’ or ‘ stressful ’. It may seem obvious when conditions are ‘ extreme ’: the midday heat of a desert, the cold of an Antarctic winter, the salinity of the Great Salt Lake. |

(A) Rather, the ecologist should try to gain a worm ’ s ‑ eye or plant ’ s ‑ eye view of the environment: to see the world as others see it. Emotive words like harsh and benign, even relativities such as hot and cold, should be used by ecologists only with care.
(B) Nor are the icy lands of Antarctica an extreme environment for penguins. It is lazy and dangerous for the ecologist to assume that all other organisms sense the environment in the way we do.
(C) But this only means that these conditions are extreme for us, given our particular physiological characteristics and tolerances. To a cactus there is nothing extreme about the desert conditions in which cacti have evolved.
① ( A)-(C)-(B) ② ( B)-(A)-(C) ③ ( B)-(C)-(A)
④ ( C)-(A)-(B) ⑤ ( C)-(B)-(A)
25. 다음 글의 내용을 아래와 같이 요약하고자 한다. 빈칸 ( A), (B) 에 들어갈 말로 가장 적절한 것은? [2.5 점 ]
A key feature particular to stories is that they have the ability to transport the reader. While experiencing stories, one can feel emotionally involved and as if being swept away as a participant. There is some evidence that being transported into a story requires a suspension of disbelief; enjoying Jurassic Park or a Harry Potter tale may involve putting aside what one knows about the world that contradicts the story. A story that suggests an unexpected outcome ( “ George Washington declined the nomination to become the first president of the United States ”) results in readers being slower to verify well-known facts ( “ George Washington was elected first president of the United States ”). This suspension of disbelief may make one less likely to spot problems in a narrative, as illustrated by a study in which participants read a story and circled any “ false notes ” or parts that did not make sense. Green and Brock refer to this method as “ Pinocchio circling ”: just as the puppet ’ s nose signaled when he told a falsehood, authors also leave clues when they are being untruthful. But readers who were more transported by the story spotted fewer “ Pinocchios .”
󰀻

| Stories have a unique ability to make readers become so (A) in reading a story that they set aside their knowledge of reality, allowing them to enjoy fictional worlds. This suspension of disbelief can make it relatively difficult for readers to (B) factual errors within the narrative. |

|  | (A) | … | (B) |
| ① | motivated | … | translate |
| ② | isolated | … | confront |
| ③ | immersed | … | overlook |
| ④ | marked | … | prevent |
| ⑤ | engaged | … | identify |

26. 다음 글의 내용을 아래와 요약하고자 한다. 빈칸 ( A), (B) 에 들어갈 말로 가장 적절한 것은? [3.2 점 ]
Hearing “ both sides ” of an issue makes sense when debating politics in a two-party system, but there ’ s a problem when that framework is applied to science. When a scientific question is unanswered, there may be three, four, or a dozen competing hypotheses, which are then investigated through research. Or there may be just one generally accepted working hypothesis, but with several important variations or differences in emphasis. When geologists were debating continental drift in the 1940s, Harvard professor Marlin Billings taught his students no less than nineteen different possible explanations for the phenomena that drift theory — later plate tectonics — was intended to explain. Research produces evidence, which in time may settle the question (as it did as continental drift evolved into plate tectonics , which became established geological theory in the early 1970s). After that point, there are no “ sides. ” There is simply accepted scientific knowledge. There may still be questions that remain unanswered — to which scientists then turn their attention — but for the question that has been answered, there is simply the consensus of expert opinion on that particular matter. That is what scientific knowledge is.
󰀻

| There could be (A) scientific explanations for a certain phenomenon, but once a theory or hypothesis is supported by evidence from researchers, it becomes scientific knowledge beyond (B) . |

|  | (A) |  | (B) |
| ① | multiple | … | common sense |
| ② | various | … | dispute |
| ③ | numerous | … | experience |
| ④ | a handful of | … | reason |
| ⑤ | few | … | controversy |

*다음장에도 문제가 있습니다.
[ 서답형4(단답) ] Complete the sentences, choosing one of the phrases below. Change the form, if necessary.[ 각 1점씩, 총 5점 ]

|  | < phrases to choose > |  |
| figure out/ waste (of) time/ in advance/ thanks to / look forward/ aptitude/ be interested in / be the key to/ think through/ take part in |

|  | < answer > |  |
| (a) I was able to finish my homework Minho ’ s help. (b) My computer suddenly froze, but I can ’ t why. (c) To understand your class material better, you might want to read it . (d) I to swimming this summer. (e) I think that I might be able to find my through club activities. *답안지에는 빈칸 내용만 적을 것. |

[ 서답형5(서술) ] There is a new club at Sangsan called Wings and Motors. Read their advertisement and answer question [A].
[5 점 ]

| Have you ever dreamed of flying high in the sky? Do you wish to drive a fancy car? We promise to give you the chance to own the airplane or car of your dreams. Does this sound too good to be true? Not at all! Join Wings and Motors , and you can assemble your own model airplane or car. By making your own aircraft and vehicles, you can improve your concentration. If you want to, you can also take part in our annual airplane and car race. Who knows? The next award for the farthest-flying airplane or the fastest car may be yours. Do not miss this chance to achieve your dream. Fly high and move fast with Wings and Motors ! |

[A] What do the Wings and Motors club members do annually?

|  | < direction > |  |
| Write at least one complete sentence. |

|  | < answer > |  |
| _________________________________________________ _________________________________________________ |

[ 서답형6(서술) ] There is another new club at Sangsan called Burning Fire . Read their advertisement and answer question [B].
[5 점 ]

| Have you ever imagined yourself in the middle of a big stage? You can relieve your stress by joining Burning Fire ! Anyone who can sing or play an instrument is welcome to join us. We meet every day after school for practice sessions. Preparing for a perfect performance takes a lot of time and effort, but it brings great rewards and helps form stronger bonds with the other members. Our performances are known to be the best part of the school festival. Creating wonderful sounds together under the shining lights of the stage will keep your heart beating with excitement. With Burning Fire , your high school years will be completely fantastic! |

[B] Who can apply for this club?

|  | < direction > |  |
| Write at least one complete sentence. |

|  | < answer > |  |
| _________________________________________________ _________________________________________________ |

● 수고하였습니다.
본 시험문제의 저작권은 상산고등학교에 있습니다. 무단 전송 · 복제, 배포 시 저작권법에 의거 처벌될 수 있습니다. [ 11 - 4 ]
```
