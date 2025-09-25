

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

# NanumGothic 폰트 경로 지정
font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')
font_manager.fontManager.addfont(font_path)
rc('font', family='NanumGothic')

st.title('간단한 데이터 시각화')

# 임의의 데이터 생성
data = pd.DataFrame({
	'A': np.random.randn(50),
	'B': np.random.rand(50),
	'C': np.random.randint(1, 100, 50)
})

st.subheader('데이터 미리보기')
st.dataframe(data)

st.subheader('A 컬럼 히스토그램 (matplotlib)')
fig, ax = plt.subplots()
ax.hist(data['A'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('A 컬럼 히스토그램')
ax.set_xlabel('값')
ax.set_ylabel('빈도')
st.pyplot(fig)

st.subheader('B vs C 산점도 (matplotlib)')
fig2, ax2 = plt.subplots()
ax2.scatter(data['B'], data['C'], color='tomato')
ax2.set_title('B vs C 산점도')
ax2.set_xlabel('B')
ax2.set_ylabel('C')
st.pyplot(fig2)
