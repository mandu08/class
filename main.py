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

# --- 풍속 선택 (추가) ---
wind_speed = st.selectbox("풍속 선택", [0,1,2,5,7,10,12,25,27])

# --- Figure 생성 ---
fig, ax = plt.subplots(figsize=(6,6)) # 화면 크게
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

# === 일기 기호 === (원본 그대로)
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

# --------------- 풍속에 따른 장식 그리기 ---------------
# helper: point along line at fraction t (0=start at circle edge, 1=end)
def point_at(t):
    return (start_x + (end_x - start_x) * t, start_y + (end_y - start_y) * t)

# perpendicular "right" relative to (dx,dy) when looking outward from center:
# right_perp = (dy, -dx)
perp_x, perp_y = dy, -dx  # already unit if (dx,dy) is unit

# draw main line for speeds != 0 and for speed==1 at least the main line
if wind_speed != 0:
    ax.plot([start_x, end_x], [start_y, end_y], color="black", linewidth=1.2)

# small perpendicular (single-sided) drawn from base point towards right_perp
def draw_perp_from(point, length):
    px, py = point
    ax.plot([px, px + perp_x * length], [py, py + perp_y * length], color="black", linewidth=1.2)

# centered small perpendicular (if needed) - not used per spec but available
def draw_perp_centered(point, length):
    px, py = point
    ax.plot([px - perp_x*length/2, px + perp_x*length/2],
            [py - perp_y*length/2, py + perp_y*length/2],
            color="black", linewidth=1.2)

# flag drawing at end: triangular flag that sticks to the RIGHT side of the line tip
def draw_flag_at_end(end_pt, base_along, width):
    # end_pt: tip point (end_x,end_y)
    ex, ey = end_pt
    # point back along the line to create flag base
    back_x = ex - dx * base_along
    back_y = ey - dy * base_along
    # third point offset to the right (perp)
    right_x = back_x + perp_x * width
    right_y = back_y + perp_y * width
    # triangle points: end_pt (tip at outside), back point, right offset
    tri = patches.Polygon([[ex, ey], [back_x, back_y], [right_x, right_y]],
                          closed=True, edgecolor="black", facecolor="black", linewidth=1)
    ax.add_patch(tri)

# Now implement wind_speed cases
if wind_speed == 0:
    # no additional drawing (no main line either)
    pass

elif wind_speed == 1:
    # just the main line (already drawn)
    pass

elif wind_speed == 2:
    # a short perpendicular a little before the end (e.g., t=0.85), pointing to right
    p = point_at(0.85)
    draw_perp_from(p, length=0.06)   # small length

elif wind_speed == 5:
    # longer perpendicular near the end (t=0.92)
    p = point_at(1)
    draw_perp_from(p, length=0.12)   # longer

elif wind_speed == 7:
    # combine 2 and 5: small perp (t=0.85) + long perp (t=0.92)
    p1 = point_at(0.85)
    p2 = point_at(1)
    draw_perp_from(p1, length=0.06)
    draw_perp_from(p2, length=0.12)

elif wind_speed == 10:
    # 5's shape plus at 2's position add 5-sized perpendicular
    # That is: long at t=0.92 (like 5) AND another long at t=0.85
    p1 = point_at(0.85)
    p2 = point_at(1)
    draw_perp_from(p1, length=0.12)  # add long at 2's position
    draw_perp_from(p2, length=0.12)  # original long

elif wind_speed == 12:
    # 10's shape plus an extra long perpendicular slightly before the 2-position
    # we add third at t=0.80
    p_pre = point_at(0.7)
    p1 = point_at(0.85)
    p2 = point_at(1)
    draw_perp_from(p_pre, length=0.06)
    draw_perp_from(p1, length=0.12)
    draw_perp_from(p2, length=0.12)

elif wind_speed == 25:
    # main line + flag at the very end
    end_pt = (end_x, end_y)
    draw_flag_at_end(end_pt, base_along=0.08, width=0.06)

elif wind_speed == 27:
    # flag at end + small perpendicular like in 2 (t=0.85)
    end_pt = (end_x, end_y)
    draw_flag_at_end(end_pt, base_along=0.08, width=0.06)
    p = point_at(0.8)
    draw_perp_from(p, length=0.06)

# === 기온 표시 (일기 기호 위쪽) ===
ax.text(base_x, base_y+0.05, f"{int(temperature)}", fontsize=8, ha="center", va="bottom")

st.pyplot(fig)
