import streamlit as st
import pandas as pd
import numpy as np

# ── 여기서부터 자유롭게 수정하세요 ───────────────

st.title("나의 관심 주식 변동폭 대시보드")   # ← 제목을 바꿔보세요

# ── 사이드바 ──────────────────────────────────
st.sidebar.title("설정")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["꺾은선 그래프", "막대 그래프", "면적 그래프"]   # ← 유형을 바꿔보세요
)

n = st.sidebar.slider(
    "조회할 기간(일)",
    min_value=5,    # ← 최솟값을 바꿔보세요
    max_value=60,   # ← 최댓값을 바꿔보세요
    value=14
)

# ── 메인 화면 ─────────────────────────────────
st.write("최근 선택한 기간 동안의 관심 주식 종목 등락폭(가상 데이터)을 시각화하는 대시보드입니다.")   # ← 설명을 바꿔보세요

data = pd.DataFrame(
    np.random.randn(n, 3),
    columns=['삼성전자', '애플', '테슬라']   # ← 컬럼 이름을 바꿔보세요
)

if chart_type == "꺾은선 그래프":
    st.line_chart(data)
elif chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))

# ── 여기까지 ──────────────────────────────────
