
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("토메함수 개형 시각화")

st.write("토메함수(예: sinc 함수)의 그래프를 아래에서 확인하세요.")

# x 값 범위 설정
x = np.linspace(-20, 20, 400)
# sinc 함수 정의 (토메함수)
y = np.sinc(x / np.pi)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("토메함수 y = sinc(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

st.pyplot(fig)
