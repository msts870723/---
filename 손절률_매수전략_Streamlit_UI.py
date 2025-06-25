
import streamlit as st
import pandas as pd

# 데이터 정의
data = {
    '손절률(%)': list(range(3, 26)),
    '매수비중(%)': [
        100, 75, 60, 50, 43, 38, 33, 30, 27, 25,
        23, 21, 20, 19, 18, 17, 16, 15, 14, 14,
        13, 13, 12
    ],
    '매수금액': [
        2000000, 1500000, 1200000, 1000000, 857143, 750000,
        666667, 600000, 545455, 500000, 461538, 428571, 400000,
        375000, 352941, 333333, 315789, 300000, 285714, 272727,
        260870, 250000, 240000
    ]
}
df = pd.DataFrame(data)

# 앱 타이틀
st.markdown("<h1 style='text-align: center;'>📈 손절률 계산기</h1>", unsafe_allow_html=True)

# 입력 UI
col1, col2 = st.columns(2)
with col1:
    현재가 = st.number_input("현재가", min_value=1, value=112900, step=100)
with col2:
    손절가 = st.number_input("손절가", min_value=1, value=107600, step=100)

# 계산 버튼
if st.button("🔍 손절률 계산 및 매수 전략 확인"):
    if 손절가 >= 현재가:
        st.error("⚠️ 손절가는 현재가보다 작아야 합니다.")
    else:
        손절률 = round((현재가 - 손절가) / 현재가 * 100, 2)
        st.success(f"📉 계산된 손절률: **{손절률}%**")

        추천 = df[df["손절률(%)"] == round(손절률)]
        if not 추천.empty:
            st.markdown("### 💡 추천 매수 전략")
            st.dataframe(추천)
        else:
            st.warning("해당 손절률에 맞는 전략이 없습니다.")

# 전체 테이블 보기 (선택)
with st.expander("📋 전체 전략표 보기"):
    st.dataframe(df)
