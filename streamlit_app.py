

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

# NanumGothic 폰트 경로 지정
font_path = os.path.join(os.path.dirname(__file__), 'fonts/NanumGothic-Regular.ttf')
font_manager.fontManager.addfont(font_path)
rc('font', family='NanumGothic')

st.title("🎈 확률 분포 시각화 앱")

page = st.sidebar.selectbox(
    "페이지 선택",
    ("홈", "확률 분포 시각화")
)

if page == "홈":
    st.write(
        "이 앱은 다양한 확률 분포(정규, 이항, 포아송 등)를 직관적으로 시각화합니다.\n"
        "왼쪽 사이드바에서 '확률 분포 시각화'를 선택해보세요."
    )

elif page == "확률 분포 시각화":
    st.header("확률 분포 시각화")
    dist_type = st.selectbox("분포 종류", ("정규분포", "이항분포", "포아송분포"))

    if dist_type == "정규분포":
        mu = st.slider("평균(μ)", -10.0, 10.0, 0.0)
        sigma = st.slider("표준편차(σ)", 0.1, 10.0, 1.0)
        x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
        y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))
        fig, ax = plt.subplots()
        ax.plot(x, y, color='royalblue')
        ax.set_title(f"정규분포 (μ={mu}, σ={sigma})")
        ax.set_xlabel("x")
        ax.set_ylabel("확률밀도함수(PDF)")
        st.pyplot(fig)

    elif dist_type == "이항분포":
        n = st.slider("시행 횟수(n)", 1, 100, 20)
        p = st.slider("성공 확률(p)", 0.0, 1.0, 0.5)
        x = np.arange(0, n+1)
        from scipy.stats import binom
        y = binom.pmf(x, n, p)
        fig, ax = plt.subplots()
        ax.bar(x, y, color='seagreen')
        ax.set_title(f"이항분포 (n={n}, p={p})")
        ax.set_xlabel("성공 횟수")
        ax.set_ylabel("확률질량함수(PMF)")
        st.pyplot(fig)

    elif dist_type == "포아송분포":
        lam = st.slider("λ(평균 발생률)", 0.1, 20.0, 3.0)
        x = np.arange(0, 30)
        from scipy.stats import poisson
        y = poisson.pmf(x, lam)
        fig, ax = plt.subplots()
        ax.bar(x, y, color='orange')
        ax.set_title(f"포아송분포 (λ={lam})")
        ax.set_xlabel("발생 횟수")
        ax.set_ylabel("확률질량함수(PMF)")
        st.pyplot(fig)
