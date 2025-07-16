import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def gravitational_lens_effect():
    # 렌즈 질량 위치
    lens_x, lens_y = 0.0, 0.0
    # 렌즈의 질량 (빛 휘어짐 정도 결정)
    mass = st.slider("중력 렌즈 질량", 0.1, 10.0, 2.0)

    # 이미지 설정
    size = 500
    x = np.linspace(-2, 2, size)
    y = np.linspace(-2, 2, size)
    X, Y = np.meshgrid(x, y)

    # 광원 설정 (은하 모양)
    source_x, source_y = st.slider("광원 위치 (X)", -1.0, 1.0, 0.7), st.slider("광원 위치 (Y)", -1.0, 1.0, 0.0)
    source_radius = 0.3
    source_intensity = np.exp(-((X - source_x)**2 + (Y - source_y)**2) / (2 * source_radius**2))

    # 렌즈에 의한 휘어짐 계산 (단순 모델)
    dx = X - lens_x
    dy = Y - lens_y
    r_squared = dx**2 + dy**2 + 1e-4  # 0으로 나눔 방지
    deflection_x = mass * dx / r_squared
    deflection_y = mass * dy / r_squared

    # 렌즈에 의해 휘어진 좌표
    lensed_X = X - deflection_x
    lensed_Y = Y - deflection_y

    # 렌즈 효과 반영한 이미지 생성
    lensed_image = np.exp(-((lensed_X - source_x)**2 + (lensed_Y - source_y)**2) / (2 * source_radius**2))

    # 시각화
    fig, ax = plt.subplots(figsize=(6,6))
    ax.imshow(lensed_image, extent=[-2,2,-2,2], origin='lower', cmap='plasma')
    ax.set_title("중력 렌즈 효과 시뮬레이션")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    st.pyplot(fig)

st.title("🌀 중력 렌즈 효과 시뮬레이션")
gravitational_lens_effect()
