import streamlit as st
import pandas as pd
import numpy as np

# ── 사이드바 설정 ─────────────────────────────
st.sidebar.title("설정")
st.sidebar.markdown("---")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["꺾은선 그래프", "막대 그래프", "면적 그래프"]
)

n_points = st.sidebar.slider("데이터 포인트 수", 10, 100, 50)
n_cols   = st.sidebar.slider("데이터 열 수", 1, 5, 3)

st.sidebar.markdown("---")
st.sidebar.info("사이드바에서 설정을 변경하면\n메인 화면이 실시간으로 업데이트됩니다.")

# ── 메인 화면 ─────────────────────────────────
st.title("사이드바 대시보드 예제")
st.write(f"선택된 차트: **{chart_type}** | 데이터: {n_points}행 x {n_cols}열")

data = pd.DataFrame(
    np.random.randn(n_points, n_cols),
    columns=[f"시리즈{i+1}" for i in range(n_cols)]
)

if chart_type == "꺾은선 그래프":
    st.line_chart(data)
elif chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))
