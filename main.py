import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Streamlit 제목
st.title("일기 기호 생성기 (Station Model)")

# 사용자 입력 받기
weather = st.selectbox("일기 선택", ["맑음", "비", "눈", "뇌우", "안개", "가랑비", "소나기"])
cloud = st.slider("운량 (0~9)", 0, 9, 0)
wind_speed = st.selectbox("풍속 (m/s)", [0, 2, 5, 7, 12, 25, 27])
wind_dir = st.slider("풍향 (도)", 0, 360, 90)
pressure = st.number_input("기압 (hPa)", value=1013)
pressure_change = st.number_input("기압 변화량", value=0)

# matplotlib으로 기호 그리기
fig, ax = plt.subplots(figsize=(4,4))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis("off")

# 운량: 원 안 채우기 (0=맑음, 9=흐림)
circle = plt.Circle((0,0), 0.5, fill=False, color="black")
ax.add_artist(circle)
if cloud > 0:
    theta = (cloud/9) * 360
    wedge = plt.matplotlib.patches.Wedge((0,0), 0.5, 90, 90+theta, facecolor="black")
    ax.add_patch(wedge)

# 풍향 & 풍속 (풍향: 바람 불어오는 방향, 풍속: 깃발 개수)
if wind_speed > 0:
    rad = np.deg2rad(wind_dir)
    x_end, y_end = np.cos(rad), np.sin(rad)
    ax.plot([0, x_end], [0, y_end], color="black")
    # 풍속 깃발 표시 (단순화)
    if wind_speed >= 25:
        ax.plot([x_end, x_end-0.2], [y_end, y_end+0.2], color="black")

# 기압 표시
ax.text(0.7, 0.3, f"{pressure:.1f}", fontsize=10)

# 기압 변화량 표시
ax.text(0.7, -0.3, f"{pressure_change:+.1f}", fontsize=10)

# 일기 기호 (간단 예: 비=점, 눈=*, 뇌우=번개)
if weather == "비":
    ax.plot([0.2,0.3],[0.2,0.1],"o",color="blue")
elif weather == "눈":
    ax.text(0.2,0.2,"*",fontsize=15,color="blue")
elif weather == "뇌우":
    ax.text(0.2,0.2,"⚡",fontsize=15,color="orange")
elif weather == "안개":
    ax.text(0.2,0.2,"〰",fontsize=15,color="gray")
elif weather == "가랑비":
    ax.text(0.2,0.2,"···",fontsize=15,color="blue")
elif weather == "소나기":
    ax.text(0.2,0.2,"//",fontsize=15,color="blue")

st.pyplot(fig)
