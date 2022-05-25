# 와플스튜디오 Backend Seminar[3]

> Instructor 변다빈([@davin111](https://github.com/davin111))
> 2020.09.26.(토) 12:30 (사전 합의 하에 30분 일찍 시작)

## 배울 내용
DBMS의 query 실행과 배포 기초
> [슬라이드](https://github.com/wafflestudio/rookies/blob/master/backend/seminar3/wafflestudio%2018.5%20Rookies%20Backend%20Seminar%203.pdf) 참고

---

## 준비 사항
- [seminar2의 과제](../seminar2/assignment.md)를 진행한 경험

---

## 세미나
- Rookies 세미나는 와플스튜디오 동아리 활동을 함께하기 위한 시작 단계임을 잊지 말아주세요! 공식 일정의 세미나 영상은 원칙적으로 사유가 있는 불참자 외에는 영상 공유를 하지 않습니다.
충분한 사유 없이 불참하고 영상으로 갈음하는 것을 방지하고자 하는 차원입니다. 현장에서 바로 이어지는 질의응답과 잡담 등에도 많은 참여 부탁드립니다.

- 과제와 세미나를 다들 열심히 따라와주고 계신 것을 많이 느끼고 있습니다. 출석 체크를 꾸준히 하고 있는데, 사유가 있어 불참하시는 분들과 세미나 진행을 중도 포기하시는 분들 외에는 다들
꾸준히 매번 세미나에 잘 참여해주시고 계십니다. 세미나에 지각을 하게 되는 경우나 중도 이탈하게 되는 경우는 없게 해주시고, 부득이한 경우 미리 알려주세요!

- 영상 등 세미나의 자료는 허락 없이 외부 공유 하지 말아주세요. 세미나 내용에 대해 궁금하신 부분 있으면, 고민하고 찾아보신 후
[Issues](https://github.com/wafflestudio/rookies/issues) 에 자유롭게 공유해주세요!

- [seminar 3](https://youtu.be/XWeYnp6KeUw)

## 세미나 중 질문
- 1번째 세미나부터 세미나 직후 참여가 자유인 질의응답 시간을 따로 가지고 있습니다. 물론 개인 일정, 안드로이드 세미나 등으로 참여가 어려운 분이 있을 수 있습니다.
 그런 경우 Issues 등을 적극적으로 활용해주세요! 제 답변에는 당연히 부정확하거나 주관적인 의견이 섞여있을 수 있습니다. :) 저를 너무 믿기보다,
 더 많고 정확한 정보를 얻고 싶다면 구글링을 병행해주세요.

---

## 세미나장 후기
> 2번째 과제 같은 경우 이전보다 조금 큰 규모의 서버 개발이라 난이도와 소요 시간 모두 만만치 않으셨을 것 같습니다. 😓 기본적인 OOP 개념이 조금이라도 능숙하지 못하신 분들은
> 특히 더 어려움을 느끼셨을 것입니다. 9/25(금) 끝나는 자정부터 가졌던 질의 응답 시간과 3번째 세미나 시작 시점에도 말씀드렸듯이, 개발은 기본적으로 인내심과 시간이 많이 필요한 작업입니다.
> Django와 DRF, RDB 등 많은 것을 습득하는 과정이라 그렇지 과제 2의 스펙 자체는 일반적인 개발 복잡도를 상당히 간소화 시켜둔 편이라는 점을 잊지 말아주세요.
> 또한 실제 개발은 문제 및 명세 정의와 의사 소통 등 더 주체적인 판단과 활동이 많이 필요할 것입니다. 🤯 여러가지가 익숙치 않은 상황 속에서 과제 2를 어떻게든
> 해내셨다면(또는 그러고 계신다면) 정말 빠른 성장🚀을 하고 있다는 자부심을 가지시기 정말 충분하다고 생각합니다. 🥳 공식적으로 우리에게 주어진 5번의 세미나와 5번의 과제는 기본적인 서버 개발을 다루기에도
> 매우 부족한 시간입니다. 0번째 세미나와 질의 응답 시간, Issues 관리, 과제 피드백 등 세미나 진행자들이 부수적인 신경을 꾸준히 써오고 있고 앞으로도 그럴 것이지만,
> 스스로의 노력과 시간 투자가 가장 중요합니다. 과제로서의 적정 선을 위해 앞으로 소요될 시간과 난이도 등은 조절하려 노력할 예정입니다. 그리고 세미나로 다룰 내용과
> 과제로 드릴 내용은 어느 정도 구분될 수 있습니다. 모든 필수 내용을 세미나로 전달할 수 없기 때문이기도 하고, 그것보다는 직접 많은 시행착오를 겪어본 후
> 이에 대해 질문하고 소통하는 과정하는 방식으로 익혀야만 의미가 있는 부분이 많기 때문입니다. 지금까지 잘 따라와주신 분들께 감사하고 존경스럽다는 말씀을 남깁니다. 🙇‍
> 갈수록 Issues에서 남겨주시는 질문들의 수준이 빠르게 높아지고 있고 제가 놓친 부분들을 짚어주시는 경우들도 생기고 있습니다.
> 앞으로 지난 금요일의 즉흥적인 질의 응답 및 잡담 시간처럼, 추가적인 소통에도 종종 신경을 쓰도록 하겠습니다. 🤗 서로 더 친해지면 좋겠네요.
>
> 가장 남기고 싶은 이야기는, Rookies 과정을 잘 마치시고 와플스튜디오에서 함께 개발을 하며 더 많은 것들을 함께 배우고 만들면 좋겠다는 것입니다! 🚀
> 세미나에서 짚는 것들은 시작 중의 시작일 뿐이니까요. 실제 프로젝트를 진행하며 느끼고 배우는 것이 더욱 많을 것입니다. 그 자체가 개개인의 좋은 경험이자 스펙이 되기도 하구요.

---

## 과제
- [assignment.md](assignment.md) 참고.
- due: 2020.10.11.(일) 23:59

---

## 피드백
> Backend 세미나를 진행해나가는 과정에서 feedback 주시면 지속적으로 참고하도록 하겠습니다. 물론 익명이고, 여러 번 남겨주실 수도 있습니다.
> < [참여하러 가기](https://forms.gle/3K2NK2uge8aABDB66) >