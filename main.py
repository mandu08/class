import streamlit as st
import matplotlib.pyplot as plt

st.title("기상청 표 일기 기호 (왼쪽 상단 배치)")

weather = st.selectbox("일기 선택", ["비", "뇌우", "가랑비"])

fig, ax = plt.subplots(figsize=(3,3))
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect("equal")
ax.axis("off")

# 중심 동그라미 (운량용) - 반지름 0.1, 위치 아래로 이동
circle = plt.Circle((0.5,0.45),0.1,edgecolor="black",facecolor="white", linewidth=1.5)
ax.add_patch(circle)

# 좌상단 기준 위치 → 9시 방향 (동그라미 왼쪽)
base_x, base_y = 0.4, 0.45

# === 일기 기호 ===
if weather == "비":
    # 점 하나
    ax.plot(base_x, base_y, "o", color="black", markersize=8)

elif weather == "뇌우":
    # 번개 지그재그
    x = [base_x, base_x+0.05, base_x-0.02, base_x+0.07]
    y = [base_y, base_y-0.07, base_y-0.07, base_y-0.15]
    ax.plot(x, y, color="black", linewidth=2)

elif weather == "가랑비":
    # 짧은 대각선 3개
    for dx in [0.0, 0.05, 0.1]:
        ax.plot([base_x+dx, base_x+dx-0.05],
                [base_y, base_y-0.1],
                color="black", linewidth=1.5)

st.pyplot(fig)
