import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

st.title("정식 일기도 기호 생성기 (WMO Station Model)")

# === 사용자 입력 ===
weather = st.selectbox("일기", ["맑음", "비", "눈", "뇌우", "안개", "가랑비", "소나기"])
cloud = st.slider("운량 (0~9)", 0, 9, 0)
wind_speed = st.selectbox("풍속 (m/s)", [0, 2, 5, 7, 12, 25, 27])
wind_dir = st.slider("풍향 (도)", 0, 360, 90)
pressure = st.number_input("기압 (hPa)", value=1013.0)
pressure_change = st.number_input("기압 변화량 (hPa)", value=0.0)

# === 그림판 준비 ===
fig, ax = plt.subplots(figsize=(5,5))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.axis("off")

# === 운량 (0~9 단계) ===
circle = plt.Circle((0,0), 1, edgecolor="black", facecolor="white")
ax.add_patch(circle)
if cloud > 0:
    theta = (cloud/9) * 360
    wedge = mpatches.Wedge((0,0), 1, 90, 90+theta, facecolor="black")
    ax.add_patch(wedge)

# === 풍향 & 풍속 ===
if wind_speed > 0:
    rad = np.deg2rad(wind_dir)
    x_end, y_end = np.cos(rad)*2, np.sin(rad)*2
    ax.plot([0, x_end], [0, y_end], color="black")
    # 풍속에 따른 깃발
    if wind_speed >= 25:
        ax.plot([x_end, x_end-0.3], [y_end, y_end+0.3], color="black")

# === 기압 & 변화량 ===
ax.text(2.2, 1, f"{pressure:.1f}", fontsize=10, ha="left")
ax.text(2.2, -1, f"{pressure_change:+.1f}", fontsize=10, ha="left")

# === 일기 기호 (정식 형태 재현) ===
if weather == "비":  # 점 2~3개
    ax.plot([0.5,0.7],[0.5,0.3],"o",color="black")
elif weather == "눈":  # ❄: 십자 + 대각선
    ax.plot([0.5,0.5],[0.2,0.8],color="black")
    ax.plot([0.2,0.8],[0.5,0.5],color="black")
    ax.plot([0.3,0.7],[0.3,0.7],color="black")
    ax.plot([0.3,0.7],[0.7,0.3],color="black")
elif weather == "뇌우":  # 번개 지그재그
    ax.plot([0.4,0.6,0.5,0.7],[0.8,0.5,0.5,0.2],color="black")
elif weather == "안개":  # 평행선
    for y in [0.2,0.4,0.6]:
        ax.plot([0.3,0.7],[y,y],color="black")
elif weather == "가랑비":  # 짧은 빗줄기
    for x in [0.4,0.5,0.6]:
        ax.plot([x,x-0.1],[0.6,0.4],color="black")
elif weather == "소나기":  # 원 + 빗줄기
    ax.add_patch(plt.Circle((0.55,0.55),0.2,fill=False,color="black"))
    ax.plot([0.55,0.45],[0.35,0.15],color="black")

st.pyplot(fig)
