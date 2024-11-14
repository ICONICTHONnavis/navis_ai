gen_nl_template = """
These grades are for all past semesters for students in the Department of Computer Engineering at Dongguk University.
Please write detailed information about the student in Korean using natural language prompts, referring to this Score.
Don't add any other comments, don't use markdown, just output the prompt as a string.

!!! Answer Korean !!!
"""

recommend_template = """
You can recommend subjects by looking at the two natural language prompts. Think in the following order and recommend subjects. Recommend subjects in a friendly, chat-like conversation.

1. Refer to the natural language prompts for the curriculum of Dongguk University's Department of Computer Science.
2. Refer to the natural language description for the user who is a computer science student and recommend about three subjects that this student should take.
3. Also attach the reason why you recommended a specific subject.
4. If you don't have a subject to recommend, don't recommend it, but explain a reasonable reason for it.

<cse_template>: 2024학년도 동국대학교 AI융합대학 컴퓨터공학전공은 공학교육인증 프로그램 운영에 따라 심화과정과 일반과정으로 구분되며, 입학 연도별 졸업 기준은 다음과 같습니다. 2015~2022학년도 입학생은 공통교양 14~16학점(신입학생 필수 이수 교과목: 동국인성 4학점, 자기계발 3학점, 사고와소통 6학점, 창의융합 3학점, 디지털 리터러시 9학점 (25학점)), 지정교양 28학점 (BSM 기준, 기본소양 9학점 + MSC 교과목), 전공은 심화과정 84학점 (설계 12학점 포함), 일반과정 72학점을 이수해야 합니다. 심화과정 학생은 전공전문 교과목을 50% 이상 이수해야 합니다. 2023학년도 입학생은 공통교양 25학점 (신입학생 필수 이수 교과목: 동국인성 4학점, 자기계발 3학점, 사고와소통 6학점, 창의융합 3학점, 디지털 리터러시 9학점), 지정교양 21학점 (BSM 기준, 기본소양 9학점 + MSC 교과목 (전산학 영역 제외)), 전공은 심화과정 84학점 (설계 12학점 포함), 일반과정 45학점을 이수해야 합니다. 심화과정 학생은 전공전문 교과목을 50% 이상 이수해야 합니다. 전공별 졸업기준표는 다음과 같습니다. 컴퓨터공학전공 심화과정 (2015~2024학년도): 공통교양 및 지정교양 이수, 전공 84학점 이수 (설계 12학점 포함, 전공전문 교과목 50% 이상 이수), 필수 교과목 이수 (어드벤처디자인(CSC2004), 컴퓨터공학종합설계1(CSE4066), 컴퓨터공학종합설계2(CSE4067), 자료구조와실습(CSE2017), 개별연구1(DAI0000), 개별연구2(DAI0000), 컴퓨터구성(CSE2018), 시스템소프트웨어와실습(CSE2013), 공개SW프로젝트(CSC4004), 계산적사고법, 이산구조(PRI4027)), 졸업 요건 (취득학점 140학점 이상, 평점평균 2.0 이상, TOEIC 700점 이상, 영어 강의 4과목 이상 (전공 2과목 이상 포함), 졸업논문 또는 대체 과목 이수, 산학협력프로젝트 순차 이수)을 충족해야 합니다. 컴퓨터공학전공 일반과정 (2015~2024학년도): 공통교양 및 지정교양 이수, 전공 72학점(2015~2019) / 45학점(2020~) 이수, 필수 교과목 이수 (어드벤처디자인(CSC2004), 컴퓨터공학종합설계1(CSE4066), 컴퓨터공학종합설계2(CSE4067), 자료구조와실습(CSE2017), 개별연구1(DAI0000), 개별연구2(DAI0000), 컴퓨터구성(CSE2018), 시스템소프트웨어와실습(CSE2013), 주니어디자인프로젝트, 공개SW프로젝트(CSC4004), 계산적사고법, 이산구조(PRI4027)), 졸업 요건 (취득학점 130학점 이상, 평점평균 2.0 이상, TOEIC 700점 이상, 영어 강의 4과목 이상 (전공 2과목 이상 포함), 졸업논문 또는 대체 과목 이수, 산학협력프로젝트 순차 이수)을 충족해야 합니다. 전공 교과목은 학수번호 체계에 따라 구분되며 (CSC: 학부 공통, CSE: 컴퓨터공학전공, MME: 멀티미디어소프트웨어공학전공, AIA: 인공지능전공, AID: 데이터사이언스전공, AIE: 엔터테인먼트테크놀로지전공), 2022년, 2023년에 개설된 일부 과목은 해당 연도의 전공 인정 여부에 따라 학점으로 인정됩니다. 과거 학부 공통 과목이나 폐지된 과목들은 현재 과목으로 대체 인정되지만, 중복 수강은 인정되지 않습니다. 컴퓨터공학전공 학생은 전공별 필수 선수·후수 체계를 준수해야 하며, 이를 지키지 않으면 학점이 인정되지 않을 수 있습니다. 학점이 3.0 미만인 수업만 재수강할 수 있습니다.
!!! Answer Korean !!!
"""