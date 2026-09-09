

## 위젯 활용

# 설문조사를 만드는 실습.
# 버튼, 체크박스, 라디오단추, 셀렉트박스, 멀티셀렉트박스, 슬라이더, 텍스트입력 등

import streamlit as st

st.title('선호도 조사')
st.caption('위젯을 조작하면 화면 아래 "실시간 응답 요약"이 바뀝니다.')

st.markdown('---')


# 1) 텍스트 입력 위젯. st.text_input("label", value="example", key="type")
name = st.text_input("1) 이름을 입력하세요.", value="홍길동", key="widget_name")
# age = st.text_input("1) 나이를 입력하세요.", value="25", key="widget_age") 

# 2) 슬라이드 위젯: 최소/최대/기본값 지정해 숫자로 선택하게 한다.
age = st.slider('2) 나이를 선택하세요', min_value=10, max_value=80, value=25, 
                key = "widget_age")

# 3) 라디오단추 : 하나만 선택할 수 있는 선택지
job = st.radio(
    "직군을 선택하세요.",
    options=["학생", '직장인', '취준생', '기타'],
    key = 'widget_job'
    #index = 기본값 index 설정
    )       


# 4) 셀렉트박스(드롭다운) : 라디오와 비슷하지만 목록이 길 때 공간 절약
country = st.selectbox(
    '4) 가장 관심 있는 무역 상대국은?',
    options=['미국', '중국', '일본','베트남','독일'],
    key="widget_country",
)

# 5) 멀티 섹렉트 박스: 여러개를 동시에 선택할 수 있음.
interest = st.multiselect(
    "5) 관심있는 데이터 분야를 모두 고르세요.",
    options=['무역통계', '환율', '주가', '날씨', '인구통계'],
    key='widget_interests',
    default=['무역통계']
)

# 6) 체크박스: 참/거짓 값중 하나만 가짐
satif = st.checkbox("6) 강의 내용에 만족하시나요?", key="widget_agree")


# 7) 슬라이더 만족 점수 1~5
score = st.slider('7) 이 강의 만족 점수', 1, 5, 4, key='widget_score')

# 8) 텍스트 영역: 여러줄의 입력이 필요할 때
feedback = st.text_area("8) 자유롭게 의견을 남겨주세요", key="widget_feedback")

# 9) 버튼: 클릭 여부 (True/False)를 반환한다. 클릭시에만 동작한다.
submitted = st.button("제출하기", key="widget_submit_btn")

st.markdown('---')
st.subheader('실시간 응답 요약')


# if 문을 넣지 않으면 버튼을 누르지 않아도 위젯값을 조작하는 즉시 바로 갱신
# 이름: 홍길동/ 나이: 25세
if submitted == True:
    st.write(f'- 이름: **{name}** / 나이: **{age}세**')
    st.write(f'- 직군: **{job}** / 관심국가: **{country}**')
    st.write(f'- 관심 분야: **{", ".join(interest) if interest else "선택없음"}**')
    st.write(f'- 강의 만족 여부: **{"만족" if satif else "미선택"}** / 만족도 점수: **{score}점**')
    st.write(f'- 자유의견: {feedback if feedback else "(입력 안함)"}')

