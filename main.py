import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

st.title("기상청 표 일기 기호")

# --- 일기 선택 ---
weather = st.selectbox("일기 선택", ["비", "눈", "뇌우", "안개", "가랑비", "소나기", "진눈깨비", "소낙눈"])

# --- 풍향 선택 ---
direction = st.selectbox("풍향 선택", ["북", "북동", "동", "남동", "남", "남서", "서", "북서"])

# --- 기온 입력 ---
temperature = st.number_input("기온 입력 (℃)", value=20.0, step=0.1)

# --- Figure 생성 ---
fig, ax = plt.subplots(figsize=(6,6))  # 화면 크게
ax.set_xlim(-0.3,1.3)
ax.set_ylim(-1.3,1.3)  # 남쪽 확장
ax.set_aspect("equal")
ax.axis("off")

# 중심 동그라미 (운량용)
cx, cy = 0.5, 0.4
r = 0.13
circle = plt.Circle((cx, cy), r, edgecolor="black", facecolor="white", linewidth=1)
ax.add_patch(circle)

# 일기 기호 기준 좌표
base_x, base_y = 0.24, 0.5

# === 일기 기호 ===
if weather == "비":
    ax.plot(base_x, base_y, "o", color="black", markersize=5)

elif weather == "눈":
    size = 0.02
    ax.plot([base_x-size, base_x+size], [base_y-size, base_y+size], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size, base_y-size], color="black", linewidth=1)
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y, base_y], color="black", linewidth=1)

elif weather == "뇌우":
    x = [base_x-0.03, base_x-0.03, base_x+0.03, base_x+0.02, base_x+0.03]
    y = [base_y-0.06, base_y, base_y, base_y-0.03, base_y-0.06]
    ax.plot(x, y, color="black", linewidth=1)
    x = [base_x+0.02, base_x+0.03, base_x+0.031]
    y = [base_y-0.05, base_y-0.06, base_y-0.045]
    ax.plot(x, y, color="black", linewidth=1)

elif weather == "안개":
    for dy in [0, -0.02, -0.04]:
        ax.plot([base_x-0.03, base_x+0.03], [base_y+dy, base_y+dy], color="black", linewidth=1)

elif weather == "가랑비":
    ax.plot([base_x+0.013, base_x],
            [base_y-0.01, base_y-0.03], 
            color="black", linewidth=1)
    ax.plot(base_x, base_y, "o", color="black", markersize=4.5)

elif weather == "소나기":
    ax.plot([base_x-0.03, base_x+0.03, base_x, base_x-0.03],
            [base_y-0.04, base_y-0.04, base_y-0.09, base_y-0.04],
            color="black", linewidth=1)
    ax.plot(base_x, base_y, "o", color="black", markersize=4.5)

elif weather == "소낙눈":
    ax.plot([base_x-0.03, base_x+0.03, base_x, base_x-0.03],
            [base_y-0.04, base_y-0.04, base_y-0.09, base_y-0.04],
            color="black", linewidth=1)
    size = 0.015
    ax.plot([base_x-size, base_x+size], [base_y-size, base_y+size], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size, base_y-size], color="black", linewidth=1)
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y, base_y], color="black", linewidth=1)

elif weather == "진눈깨비":
    ax.plot(base_x, base_y, "o", color="black", markersize=4.5)
    size = 0.015
    ax.plot([base_x-size, base_x+size], [base_y-size-0.05, base_y+size-0.05], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size-0.05, base_y-size-0.05], color="black", linewidth=1)
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y-0.05, base_y-0.05], color="black", linewidth=1)

# === 풍향 직선 추가 (원의 테두리에서 바깥으로) ===
dir_map = {
    "북": (0, 1),
    "남": (0, -1),
    "동": (1, 0),
    "서": (-1, 0),
    "북동": (math.sqrt(2)/2, math.sqrt(2)/2),
    "북서": (-math.sqrt(2)/2, math.sqrt(2)/2),
    "남동": (math.sqrt(2)/2, -math.sqrt(2)/2),
    "남서": (-math.sqrt(2)/2, -math.sqrt(2)/2)
}

dx, dy = dir_map[direction]

# 시작점: 원 테두리
start_x = cx + dx * r
start_y = cy + dy * r

# 끝점: 테두리에서 바깥쪽으로 일정 길이 연장
line_length = 0.5
end_x = cx + dx * (r + line_length)
end_y = cy + dy * (r + line_length)

ax.plot([start_x, end_x], [start_y, end_y], color="black", linewidth=1.2)

# === 기온 표시 (일기 기호 위쪽) ===
ax.text(base_x, base_y+0.1, f"{temperature:.1f}℃", fontsize=12, ha="center", va="bottom")

st.pyplot(fig)
