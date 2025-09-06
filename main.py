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
temperature = st.number_input("기온 입력 (℃)", value=20, step=1)
temperature = int(temperature)

# --- 풍속 선택 ---
wind_speed = st.selectbox("풍속 선택", [0,1,2,5,7,10,12,25,27])

# --- 운량 선택 ---
cloudiness = st.slider("운량 선택 (0~10)", 0, 10, 0, step=1)

# --- Figure 생성 ---
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-0.3,1.3)
ax.set_ylim(-1.3,1.3)
ax.set_aspect("equal")
ax.axis("off")

# 중심 동그라미 좌표
cx, cy = 0.5, 0.4
r = 0.13

# 기본 동그라미
circle = plt.Circle((cx, cy), r, edgecolor="black", facecolor="white", linewidth=1)
ax.add_patch(circle)

# --- 운량별 내부 모양 ---
if cloudiness == 1:
    ax.plot([cx, cx], [cy - r*0.7, cy + r*0.7], color="black", linewidth=1.2)

elif cloudiness in [2,3]:
    wedge = patches.Wedge((cx, cy), r, 0, 90, facecolor="black", edgecolor="none")
    ax.add_patch(wedge)

elif cloudiness == 4:
    wedge = patches.Wedge((cx, cy), r, 0, 90, facecolor="black", edgecolor="none")
    ax.add_patch(wedge)
    ax.plot([cx, cx], [cy - r, cy + r], color="black", linewidth=1)

elif cloudiness == 5:
    wedge1 = patches.Wedge((cx, cy), r, 0, 90, facecolor="black", edgecolor="none")
    wedge2 = patches.Wedge((cx, cy), r, 270, 360, facecolor="black", edgecolor="none")
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)
    ax.plot([cx, cx], [cy - r, cy + r], color="white", linewidth=0.5)

elif cloudiness == 6:
    wedge1 = patches.Wedge((cx, cy), r, 0, 90, facecolor="black", edgecolor="none")
    wedge2 = patches.Wedge((cx, cy), r, 270, 360, facecolor="black", edgecolor="none")
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)
    ax.plot([cx, cx], [cy - r, cy + r], color="white", linewidth=0.5)
    ax.plot([cx - r, cx + r], [cy, cy], color="black", linewidth=1)

elif cloudiness in [7,8]:
    wedge1 = patches.Wedge((cx, cy), r, 0, 90, facecolor="black", edgecolor="none")
    wedge2 = patches.Wedge((cx, cy), r, 270, 360, facecolor="black", edgecolor="none")
    wedge3 = patches.Wedge((cx, cy), r, 180, 270, facecolor="black", edgecolor="none")
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)
    ax.add_patch(wedge3)
    ax.plot([cx - r, cx + r], [cy, cy], color="black", linewidth=1.)

elif cloudiness == 9:
    circle2 = plt.Circle((cx, cy), r, edgecolor="black", facecolor="black", linewidth=1)
    ax.add_patch(circle2)
    ax.plot([cx, cx], [cy - r, cy + r], color="white", linewidth=0.5)

elif cloudiness == 10:
    circle2 = plt.Circle((cx, cy), r, edgecolor="black", facecolor="black", linewidth=1)
    ax.add_patch(circle2)

# --- 일기 기호 기준 좌표 ---
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

# --- 풍향 직선 ---
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
start_x = cx + dx * r
start_y = cy + dy * r
line_length = 0.5
end_x = cx + dx * (r + line_length)
end_y = cy + dy * (r + line_length)

# --- 보조 함수 ---
perp_x, perp_y = dy, -dx

def point_at(t):
    return (start_x + (end_x - start_x) * t, start_y + (end_y - start_y) * t)

def draw_perp_from(point, length):
    px, py = point
    ax.plot([px, px + perp_x * length], [py, py + perp_y * length], color="black", linewidth=1.2)

def draw_flag_at_end(end_pt, base_along, width):
    ex, ey = end_pt
    right_angle_x, right_angle_y = ex, ey
    base_x_line = ex - dx * base_along
    base_y_line = ey - dy * base_along
    perp_end_x = ex + perp_x * width
    perp_end_y = ey + perp_y * width
    tri = patches.Polygon([[right_angle_x, right_angle_y],
                           [base_x_line, base_y_line],
                           [perp_end_x, perp_end_y]],
                          closed=True, edgecolor="black", facecolor="black", linewidth=1)
    ax.add_patch(tri)

# --- 풍속 장식 ---
if wind_speed != 0:
    ax.plot([start_x, end_x], [start_y, end_y], color="black", linewidth=1.2)

if wind_speed == 2:
    p = point_at(0.85)
    draw_perp_from(p, 0.06)
elif wind_speed == 5:
    p = point_at(1)
    draw_perp_from(p, 0.12)
elif wind_speed == 7:
    draw_perp_from(point_at(0.85), 0.06)
    draw_perp_from(point_at(1), 0.12)
elif wind_speed == 10:
    draw_perp_from(point_at(0.85), 0.12)
    draw_perp_from(point_at(1), 0.12)
elif wind_speed == 12:
    draw_perp_from(point_at(0.7), 0.06)
    draw_perp_from(point_at(0.85), 0.12)
    draw_perp_from(point_at(1), 0.12)
elif wind_speed == 25:
    draw_flag_at_end((end_x, end_y), 0.08, 0.1)
elif wind_speed == 27:
    draw_flag_at_end((end_x, end_y), 0.08, 0.1)
    draw_perp_from(point_at(0.8), 0.06)

# --- 기온 표시 ---
ax.text(base_x, base_y+0.05, f"{int(temperature)}", fontsize=8, ha="center", va="bottom")

st.pyplot(fig)
