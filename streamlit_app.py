import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 토메함수(예시: tan(x)) 그래프 시각화
st.header("토메함수 그래프 시각화")
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)

fig, ax = plt.subplots()
ax.plot(x, y, label='y = tan(x)')
ax.set_ylim(-10, 10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('토메함수: y = tan(x)')
ax.grid(True)
ax.legend()

st.pyplot(fig)
