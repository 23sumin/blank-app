
import streamlit as st
import pandas as pd
import numpy as np

st.title('간단한 데이터 시각화')

# 임의의 데이터 생성
data = pd.DataFrame({
	'A': np.random.randn(50),
	'B': np.random.rand(50),
	'C': np.random.randint(1, 100, 50)
})

st.subheader('데이터 미리보기')
st.dataframe(data)

st.subheader('A 컬럼 히스토그램')
st.bar_chart(data['A'])

st.subheader('B vs C 산점도')
st.scatter_chart(data, x='B', y='C')
