import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.title("기상청 표 일기 기호 + 풍향 + 기온 표시")

# 일기 선택
weather = st.selectbox("일기 선택", ["비", "눈", "뇌우", "안개", "가랑비", "소나기"])

# 풍향 선택
direction = st.selectbox("풍향 선택", ["북", "동", "남", "서"])

# 기온 입력
temperature = st.number_input("기온 입력 (℃)", value=20.0, step=0.1)

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

# 중심 원 (운량용)
circle = plt.Circle((0.5, 0.5), 0.1, edgecolor="black", facecolor="white", linewidth=1.5)
ax.add_patch(circle)

# === 일기 기호 ===
base_x, base_y = 0.3, 0.65  # 원 왼쪽 위에 배치

if weather == "비":
    ax.plot(base_x, base_y, "o", color="black", markersize=8)

elif weather == "눈":
    # X자
    ax.plot([base_x-0.05, base_x+0.05], [base_y-0.05, base_y+0.05], color="black", linewidth=1.5)
    ax.plot([base_x-0.05, base_x+0.05], [base_y+0.05, base_y-0.05], color="black", linewidth=1.5)
    # 수평선
    ax.plot([base_x-0.06, base_x+0.06], [base_y, base_y], color="black", linewidth=1.5)

elif weather == "뇌우":
    # ㄱ자 좌우 반전 + 추가 직선 + 화살표
    x = [base_x, base_x-0.05, base_x+0.02, base_x-0.07]
    y = [base_y, base_y-0.07, base_y-0.07, base_y-0.15]
    ax.plot(x, y, color="black", linewidth=2)
    # 추가 대각선
    ax.plot([x[-1], x[-1]-0.05], [y[-1], y[-1]-0.05], color="black", linewidth=2)
    # 끝에 화살표
    ax.arrow(x[-1]-0.05, y[-1]-0.05, 0.03, -0.03,
             head_width=0.02, head_length=0.03, fc="black", ec="black")

elif weather == "안개":
    for i in range(3):
        ax.plot([base_x-0.07, base_x+0.07], [base_y-0.04*i, base_y-0.04*i], color="black", linewidth=1.5)

elif weather == "가랑비":
    ax.plot([base_x, base_x-0.05], [base_y, base_y-0.1], color="black", linewidth=1.5)

elif weather == "소나기":
    triangle = patches.Polygon([[base_x, base_y],
                                [base_x-0.07, base_y-0.12],
                                [base_x+0.07, base_y-0.12]],
                               closed=True, edgecolor="black", facecolor="none", linewidth=1.5)
    ax.add_patch(triangle)
    ax.plot(base_x, base_y+0.08, "o", color="black", markersize=6)

# === 풍향 표시 (원의 테두리에서 바깥으로 선) ===
angles = {"북": 90, "동": 0, "남": -90, "서": 180}
angle = np.deg2rad(angles[direction])

r_start = 0.1  # 원의 반지름
r_end = 0.6    # 바깥으로 뻗는 길이
x0, y0 = 0.5 + r_start * np.cos(angle), 0.5 + r_start * np.sin(angle)
x1, y1 = 0.5 + r_end * np.cos(angle), 0.5 + r_end * np.sin(angle)
ax.plot([x0, x1], [y0, y1], color="black", linewidth=2)

# === 기온 표시 (일기 위쪽에 숫자 출력) ===
ax.text(base_x, base_y+0.12, f"{temperature:.1f}℃", fontsize=12, ha="center", va="bottom")

st.pyplot(fig)
