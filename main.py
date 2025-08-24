import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title("기상청 표 일기 기호 (왼쪽 상단 배치)")

weather = st.selectbox("일기 선택", ["비", "눈", "뇌우", "안개", "가랑비", "소나기", "진눈깨비", "소낙눈"])

fig, ax = plt.subplots(figsize=(3,3))
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect("equal")
ax.axis("off")

# 중심 동그라미 (운량용)
circle = plt.Circle((0.5,0.4),0.13,edgecolor="black",facecolor="white", linewidth=1)
ax.add_patch(circle)

# 일기 기호 기준 좌표
base_x, base_y = 0.24, 0.5

# === 일기 기호 ===
if weather == "비":
    ax.plot(base_x, base_y, "o", color="black", markersize=5)

elif weather == "눈":
    size = 0.02
    # X자
    ax.plot([base_x-size, base_x+size], [base_y-size, base_y+size], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size, base_y-size], color="black", linewidth=1)
    # X 중점 수평선
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y, base_y], color="black", linewidth=1)

elif weather == "뇌우":
    # 좌우반전 ㄱ자
    x = [base_x-0.03, base_x-0.03, base_x+0.03, base_x+0.02, base_x+0.03]
    y = [base_y-0.06, base_y, base_y, base_y-0.03, base_y-0.06]
    ax.plot(x, y, color="black", linewidth=1)
    x = [base_x+0.02, base_x+0.03, base_x+0.03]
    y = [base_y-0.05, base_y-0.06, base_y-0.047]
    ax.plot(x, y, color="black", linewidth=1)


elif weather == "안개":
    # 가로줄 세 개
    for dy in [0, -0.02, -0.04]:
        ax.plot([base_x-0.03, base_x+0.03], [base_y+dy, base_y+dy], color="black", linewidth=1)

elif weather == "가랑비":
    ax.plot([base_x+0.013, base_x],
            [base_y-0.01, base_y-0.03], 
            color="black", linewidth=1)
    # 위에 점
    ax.plot(base_x, base_y, "o", color="black", markersize=4.5)

elif weather == "소나기":
    # 역삼각형 (왼쪽, 오른쪽, 아래)
    ax.plot([base_x-0.03, base_x+0.03, base_x, base_x-0.03],
            [base_y-0.04, base_y-0.04, base_y-0.09, base_y-0.04],
            color="black", linewidth=1)
    # 위에 점
    ax.plot(base_x, base_y, "o", color="black", markersize=4.5)

elif weather == "소낙눈":
    # 역삼각형 (왼쪽, 오른쪽, 아래)
    ax.plot([base_x-0.03, base_x+0.03, base_x, base_x-0.03],
            [base_y-0.04, base_y-0.04, base_y-0.09, base_y-0.04],
            color="black", linewidth=1)
    size = 0.015
    # X자
    ax.plot([base_x-size, base_x+size], [base_y-size, base_y+size], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size, base_y-size], color="black", linewidth=1)
    # X 중점 수평선
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y, base_y], color="black", linewidth=1)

elif weather == "진눈깨비":
    # 위에 점
    ax.plot(base_x, base_y, "o", color="black", markersize=4.5)
    size = 0.015
    # X자
    ax.plot([base_x-size, base_x+size], [base_y-size-0.05, base_y+size-0.05], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size-0.05, base_y-size-0.05], color="black", linewidth=1)
    # X 중점 수평선
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y-0.05, base_y-0.05], color="black", linewidth=1)

# 풍향 선택
direction = st.selectbox("풍향 선택", ["북", "남", "동", "서", "북동", "북서", "남동", "남서"])

# 중심 동그라미 좌표와 반지름
cx, cy = 0.5, 0.4
r = 0.13

# 풍향에 따라 단위 벡터 설정
import math
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

# 시작점: 풍향 방향 끝, 동그라미 바깥으로 반지름만큼 이동
start_x = cx + dx * r
start_y = cy + dy * r

# 끝점: 동그라미 중심
end_x = cx
end_y = cy

# 선 그리기
fig, ax = plt.subplots(figsize=(3,3))
ax.plot([start_x, end_x], [start_y, end_y], color="black", linewidth=1.2)



st.pyplot(fig)
