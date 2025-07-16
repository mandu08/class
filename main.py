import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 타이틀
st.title("🌌 광원 앞을 지나가는 항성 + 행성 → 밝기 변화 시뮬레이션")

# 파라미터 설정
st.sidebar.header("🔧 시뮬레이션 설정")
star_radius = st.sidebar.slider("항성 반지름", 0.1, 0.5, 0.3)
planet_radius = st.sidebar.slider("행성 반지름", 0.01, 0.2, 0.05)
planet_orbit_radius = st.sidebar.slider("행성 궤도 반지름", 0.5, 2.0, 1.0)
star_speed = st.sidebar.slider("항성 이동 속도", 0.0, 0.2, 0.05)
planet_orbit_speed = st.sidebar.slider("행성 공전 속도", 1.0, 10.0, 5.0)

# 시간 배열
time_steps = 1000
total_time = 10
times = np.linspace(0, total_time, time_steps)

# 광원 위치
source_x, source_y = 0.0, 0.0

# 밝기 계산 함수
brightness = []

for t in times:
    # 항성 위치: 직선 이동
    star_x = star_speed * (t - total_time / 2)
    star_y = 0

    # 행성 위치: 항성 중심 원형 궤도 공전
    angle = planet_orbit_speed * t
    planet_x = star_x + planet_orbit_radius * np.cos(angle)
    planet_y = star_y + planet_orbit_radius * np.sin(angle)

    # 차폐 여부 체크
    def is_blocking(obj_x, obj_y, radius):
        distance = np.sqrt((obj_x - source_x)**2 + (obj_y - source_y)**2)
        return distance < radius

    blocked_area = 0
    if is_blocking(star_x, star_y, star_radius):
        blocked_area += star_radius**2
    if is_blocking(planet_x, planet_y, planet_radius):
        blocked_area += planet_radius**2

    # 밝기 = 원래 밝기 1에서 차폐 면적만큼 감소
    brightness.append(1 - blocked_area)

# 그래프 출력
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(times, brightness, color="royalblue")
ax.set_xlabel("시간")
ax.set_ylabel("밝기")
ax.set_title("💫 관측 밝기(light curve)")
st.pyplot(fig)
