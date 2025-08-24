import streamlit as st

st.title("Streamlit에서 쉼표 모양 그리기")

# 쉼표 모양을 그리는 SVG 코드
# d 속성은 쉼표의 곡선과 점을 정의합니다.
svg_comma = """
<svg width="200" height="200" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M 50,20 Q 50,70 80,70 A 5,5 0 1 1 80,80 L 80,80 A 5,5 0 1 1 80,90 L 80,90 A 5,5 0 1 1 80,100" 
        stroke="black" stroke-width="2" fill="none"/>
  <circle cx="80" cy="100" r="5" fill="black"/>
</svg>
"""

# HTML 렌더링을 위해 `st.markdown`을 사용합니다.
st.markdown(svg_comma, unsafe_allow_html=True)
