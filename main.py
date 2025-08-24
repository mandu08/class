import streamlit as st
import matplotlib.pyplot as plt

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
base_x, base_y = 0.28, 0.5

# === 일기 기호 ===
if weather == "비":
    ax.plot(base_x, base_y, "o", color="black", markersize=7)

elif weather == "눈":
    size = 0.02
    # X자
    ax.plot([base_x-size, base_x+size], [base_y-size, base_y+size], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size, base_y-size], color="black", linewidth=1)
    # X 중점 수평선
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y, base_y], color="black", linewidth=1)

elif weather == "뇌우":
    # 좌우반전 ㄱ자
    x = [base_x, base_x-0.05, base_x+0.02, base_x-0.07]
    y = [base_y, base_y-0.07, base_y-0.07, base_y-0.15]
    ax.plot(x, y, color="black", linewidth=2)
    # 오른쪽 끝 대각선 왼쪽 아래
    x2 = [x[-1], x[-1]-0.03]
    y2 = [y[-1], y[-1]-0.03]
    ax.plot(x2, y2, color="black", linewidth=2)
    # 화살표: 끝점에서 오른쪽 아래
    ax.annotate("", xy=(x2[-1]+0.02, y2[-1]-0.02), xytext=(x2[-1], y2[-1]),
                arrowprops=dict(arrowstyle="->", color="black", lw=2))

elif weather == "안개":
    # 가로줄 세 개
    for dy in [0, -0.02, -0.04]:
        ax.plot([base_x-0.03, base_x+0.03], [base_y+dy, base_y+dy], color="black", linewidth=1)

elif weather == "가랑비":
    # 따옴표 모양 1개
    ax.plot([base_x, base_x-0.05],
            [base_y, base_y-0.1],
            color="black", linewidth=1.5)

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
    ax.plot([base_x-size, base_x+size], [base_y-size, base_y+size], color="black", linewidth=1)
    ax.plot([base_x-size, base_x+size], [base_y+size, base_y-size], color="black", linewidth=1)
    # X 중점 수평선
    ax.plot([base_x-size-0.005, base_x+size+0.005], [base_y, base_y], color="black", linewidth=1)


st.pyplot(fig)
