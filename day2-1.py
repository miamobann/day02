import streamlit as st
import pandas as pd   # DateFrame 생성해야하므로
import os             # 외부 파일 반출용


csv_path = os.path.join(os.path.dirname(__file__), "..", "common", 'raw_trade_data.csv')
# path ~경로에서 join: 파일 가져오기 (os.path =내 시스템의 경로)
# dirname() : ()이름인 파일     - __file__ : 내가 지금 작업하고 있는 이 파일  
# ".."으로 상위디렉토리로 이동 후 이어서 경로 작성

# 만약 같은 폴더 내에 있다면 dirname(__file__), '파일명.csv' 형식으로 작성

#환율 샘플데이터
# 딕셔너리로 표 만들기
ex_rate = {
    '통화':['USD',"EUR",'JPY(100엔','CNY'],
    '환율(KRW)':[1390.50,1503.20,930.80,191.30],
    '전일대비':[+5.2,-3.1,+1.0,-0.4],
}

df_ex_rate = pd.DataFrame(ex_rate)



st.title("오늘의 환율 대시보드")
st.caption("아래 데이터는 실제 완율이 아닌 실습용 샘플 데이터입니다.")


st.subheader('1. 환율 표 보기')

# st.dataframe을 이용한 상호작용 가능한 표
st.write('▶ st.dataframe (상호작용 가능한 표)')
st.dataframe(df_ex_rate, use_container_width=True) 

# st.table을 이용한 고정 표
st.write('▶ st.table (정적인 표)')
st.table(df_ex_rate)



st.markdown('---')



st.subheader('2) 주요 환율 키워드 (st.metric)')

col1, col2, col3 = st.columns(3)   # 사용할 columns 갯수와 변수명 설정.

# st.metric(라벨, 현재값, 증감값)
with col1:
    st.metric(label="USD/KRW", value="1,450.5", delta="+5.2")
    # 여긴 텍스트로 값을 줬지만 진짜 데이터를 이용할 때는 그것 대로 출력 가능
with col2:
    st.metric(label="EUR/KRW", value="1,525.5", delta="+3.1")
with col3:
    st.metric(label="JPY/KRW", value="865.5", delta="-1.2")



st.markdown('---')



st.header('3) 보너스: 무역 원본 데이터 미리보기')
st.caption("공용 데이터 파일 raw_trade_data.csv 파일을 이용한 예시입니다.")

ex_rate2 = pd.read_csv(csv_path, encoding='utf-8')
st.dataframe(ex_rate2.head(5))


