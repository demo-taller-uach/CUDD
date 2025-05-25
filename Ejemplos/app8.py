# Barco navegando
import streamlit as st
st.title("🚢 Barco animado navegando en Streamlit")
st.markdown("Relájate y observa cómo el barco se mueve sobre el horizonte...")

barco_html = """
<style>
@keyframes navegar {
  0%   { left: 0%; }
  50%  { left: 85%; transform: scaleX(1); }
  51%  { transform: scaleX(1); } /* voltea el barco */
  100% { left: 0%; }
}

.mar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 120px;
  background: linear-gradient(to top, #0077be, #00aaff);
  z-index: 1;
}

.barco {
  position: fixed;
  bottom: 80px;
  left: 0;
  font-size: 48px;
  animation: navegar 50s infinite linear;
  z-index: 2;
  user-select: none;
}
</style>

<div class="mar"></div>
<div class="barco">⛵</div>
"""

st.markdown(barco_html, unsafe_allow_html=True)
if st.button("click"):
    st.balloons()
