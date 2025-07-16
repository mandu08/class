import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🌌 항성과 행성의 통과에 따른 광원 밝기 변화 및 위치 시각화")

# ⚙️ 시뮬레이션 설정
st.sidebar.header("🛠 시뮬레이션 파라미터")
star_radius = st.sidebar.slider("항성 반지름", 0.1, 0.5, 0.3)
planet_radius = st.sidebar.slider("행성 반지름", 0.05, 0.2, 0.08)
orbit_radius = st.sidebar.slider("행성 궤도 반지름", 0.5, 1.5, 1.0)
star_speed = st.sidebar.slider("항성의 이동 속도", 0.01, 0.2, 0.05)
planet_orbit_speed = st.sidebar.slider("행성 공전 속도", 1.0, 10.0, 5.0)

# ⏱ 시뮬레이션 시간 설정
total_time = 10
time_steps = 500
times = np.linspace(0, total_time, time_steps)

# 🌟 광원 고정 위치
source_x, source_y = 0.0, 0.0

# 📉 밝기 변화 계산
brightness = []
star_positions = []
planet_positions = []

for t in times:
    # 항성 이동 (광원 앞을 통과)
    star_x = star_speed * (t - total_time / 2)
    star_y = 0

    # 행성 공전 위치
    angle = planet_orbit_speed * t
    planet_x = star_x + orbit_radius * np.cos(angle)
    planet_y = star_y + orbit_radius * np.sin(angle)

    star_positions.append((star_x, star_y))
    planet_positions.append((planet_x, planet_y))

    def is_blocking(obj_x, obj_y, radius):
        dist = np.sqrt((obj_x - source_x)**2 + (obj_y - source_y)**2)
        return dist < radius

    # 광원 차폐 면적 계산
    blocked_area = 0
    if is_blocking(star_x, star_y, star_radius):
        blocked_area += star_radius**2
    if is_blocking(planet_x, planet_y, planet_radius):
        blocked_area += planet_radius**2

    brightness.append(1 - blocked_area)

# 📈 밝기 그래프 시각화
fig1, ax1 = plt.subplots(figsize=(8,4))
ax1.plot(times, brightness, color="crimson")
ax1.set_xlabel("시간")
ax1.set_ylabel("밝기")
ax1.set_title("💡 광원의 밝기 변화 (light curve)")
st.pyplot(fig1)

# 🪐 천체 위치 시각화 (현재 시간 선택)
st.subheader("🔭 현재 시점의 천체 배열 시각화")
selected_index = st.slider("시간 인덱스 선택", 0, time_steps - 1, time_steps // 2)
star_x, star_y = star_positions[selected_index]
planet_x, planet_y = planet_positions[selected_index]

fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')

# 광원
ax2.plot(source_x, source_y, marker='*', markersize=20, color='gold', label='광원')

# 항성
star_circle = plt.Circle((star_x, star_y), star_radius, color='orange', alpha=0.8, label='항성')
ax2.add_patch(star_circle)

# 행성
planet_circle = plt.Circle((planet_x, planet_y), planet_radius, color='blue', alpha=0.6, label='행성')
ax2.add_patch(planet_circle)

# 궤도 경로 표시
orbit_path = plt.Circle((star_x, star_y), orbit_radius, color='gray', linestyle='--', fill=False)
ax2.add_patch(orbit_path)

ax2.set_title(f"시간 = {times[selected_index]:.2f}")
ax2.legend()
st.pyplot(fig2)
