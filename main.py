import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("쉼표 모양 그리기")

fig, ax = plt.subplots(figsize=(2,2))

# 원 부분
theta = np.linspace(0, 2*np.pi, 100)
r = 0.5
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.fill(x, y, 'k')  # 검은색 원

# 꼬리 부분 (곡선)
t = np.linspace(0, 1, 50)
tail_x = 0.1 * np.sin(3 * np.pi * t)  # 약간 꼬이는 느낌
tail_y = -0.5 * t - 0.05
ax.plot(tail_x, tail_y, 'k', linewidth=4)

ax.set_aspect('equal')
ax.axis('off')

st.pyplot(fig)
