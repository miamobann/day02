# random 모듈을 이용해서 1~45중 중복 없는 번호 6개를 뽑고
# 자료 구조 set, 버튼을 누르면 5세트를 한번에 생성
# datetime 으로 생성 시간도 함께 보여준다.

import streamlit as st
import random as r
from datetime import datetime




st.header('🎱 로또 번호 자동 생성기')
st.caption('버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만들어줍니다.')

st.markdown('---')

# def launch_lott() -> list :
#     '''버튼을 누를 때마다 1~45에서 중복 없이 번호 6개를 뽑아 정렬된 리스트로 반환'''    
#     number = set[int]()
#     while len(number) < 6:
#         number.add(r.randint(1,45))  #1~45 정수 하나 뽑기
#     return sorted(number)


# gogo = st.button("돌려잇", key='lotto_generate_btn')

# now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# st.write(f'생성 시각 : **{now_str}**')

# for set_index in range(1,6):
#     lotto_num = launch_lott()
#     st.write(f'{set_index}세트: {lotto_num}')


import random as r
from datetime import datetime
import streamlit as st

def get_colored_ball(num: int) -> str:
    """번호 대역에 맞춰 색상 공 이모지와 번호 텍스트 결합"""
    if num <= 10:
        emoji = "🟡"   # 1 ~ 10
    elif num <= 20:
        emoji = "🔵"   # 11 ~ 20
    elif num <= 30:
        emoji = "🔴"   # 21 ~ 30
    elif num <= 40:
        emoji = "⚪"   # 31 ~ 40
    else:
        emoji = "🟢"   # 41 ~ 45
    return f"{emoji} {num:02d}"

def launch_lott() -> list:
    """1~45에서 중복 없이 번호 6개를 뽑아 정렬된 리스트로 반환"""
    number = set()
    while len(number) < 6:
        number.add(r.randint(1, 45))
    return sorted(number)

gogo = st.button("돌려잇", key="lotto_generate_btn")

# 버튼을 눌렀을 때만 번호 생성 및 출력
if gogo:
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.caption(f"생성 시각 : **{now_str}**")
    st.write("---")

    for set_index in range(1, 6):
        lotto_num = launch_lott()
        # 번호별 이모지 변환 후 공백으로 연결
        formatted_balls = " ".join(get_colored_ball(n) for n in lotto_num)
        st.write(f"**{set_index}세트** | {formatted_balls}")



# if gogo == True:
    
#     count = 0
#     while count <5:
#         lott = set()
#         while len(lott) < 6:
#             lott.add(r.randint(1,45))
#         result = sorted(lott)
#         count += 1
#         st.write(f'{count}세트: {result}')


