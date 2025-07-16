import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🪐 항성 + 행성의 움직임 및 광원 위치 시각화")

# 설정 파라미터
st.sidebar.header("🧭 시뮬레이션 설정")
star_radius = st.sidebar.slider("항성 반지름", 0.1, 0.5, 0.3)
planet_radius = st.sidebar.slider("행성 반지름", 0.05, 0.2, 0.08)
orbit_radius = st.sidebar.slider("행성 궤도 반지름", 0.5, 1.5, 1.0)
star_speed = st.sidebar.slider("항성의 이동 속도", 0.0, 0.2, 0.05)
time = st.slider("시간", 0.0, 10.0, 5.0)

# 천체 위치 계산
source_x, source_y = 0.0, 0.0  # 광원은 고정
star_x = star_speed * (time - 5.0)
star_y = 0.0
planet_angle = 2 * np.pi * time / 2.0  # 공전 주기 고정 (대략 2초로 가정)
planet_x = star_x + orbit_radius * np.cos(planet_angle)
planet_y = star_y + orbit_radius * np.sin(planet_angle)

# 시각화
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# 광원
ax.plot(source_x, source_y, marker='*', markersize=20, color='gold', label='광원 (배경별)')

# 항성
star_circle = plt.Circle((star_x, star_y), star_radius, color='orange', alpha=0.8, label='항성')
ax.add_patch(star_circle)

# 행성
planet_circle = plt.Circle((planet_x, planet_y), planet_radius, color='blue', alpha=0.6, label='행성')
ax.add_patch(planet_circle)

# 궤도 경로 (시각적 보조용)
orbit_path = plt.Circle((star_x, star_y), orbit_radius, color='gray', linestyle='--', fill=False)
ax.add_patch(orbit_path)

# 레이블 및 범례
ax.set_title(f"시간 = {time:.1f}")
ax.legend(loc='upper right')
st.pyplot(fig)
