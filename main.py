import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🌠 항성과 행성의 통과에 따른 광원 밝기 변화")

# 시뮬레이션 설정
total_time = 10  # 총 시뮬레이션 시간
time_steps = 1000
times = np.linspace(0, total_time, time_steps)

# 사용자 입력
star_radius = st.slider("항성 반지름", 0.1, 0.5, 0.3)
planet_radius = st.slider("행성 반지름", 0.02, 0.2, 0.1)
orbit_radius = st.slider("행성 궤도 반지름", 1.0, 2.0, 1.5)
star_orbit_speed = st.slider("항성의 속도", 0.0, 0.5, 0.1)
planet_orbit_speed = st.slider("행성의 공전 속도", 1.0, 5.0, 2.0)

# 광원의 위치
source_x = 0.0
source_y = 0.0

# 밝기 시뮬레이션
brightness = []

for t in times:
    # 항성 위치
    star_x = star_orbit_speed * (t - total_time/2)
    star_y = 0

    # 행성 위치 (항성을 중심으로 원형 궤도)
    angle = planet_orbit_speed * t
    planet_x = star_x + orbit_radius * np.cos(angle)
    planet_y = star_y + orbit_radius * np.sin(angle)

    def is_blocking(x_obj, y_obj, radius_obj):
        dist = np.sqrt((x_obj - source_x)**2 + (y_obj - source_y)**2)
        return dist < radius_obj

    # 광원 가림 여부 계산
    blocked = 0
    if is_blocking(star_x, star_y, star_radius):
        blocked += (star_radius)**2
    if is_blocking(planet_x, planet_y, planet_radius):
        blocked += (planet_radius)**2

    # 밝기 계산: 원래 밝기 1에서 가려진 면적만큼 감소
    total_brightness = 1 - blocked
    brightness.append(total_brightness)

# 그래프 출력
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(times, brightness, color='orange')
ax.set_xlabel("시간")
ax.set_ylabel("광원의 밝기")
ax.set_title("💫 트랜짓(light curve) 시뮬레이션")
st.pyplot(fig)
