import streamlit as st

st.title("Ejemplo de Slider")

# Widget: slider
numero = st.slider("Selecciona un número", min_value=0, max_value=100, value=50)

st.write("El número seleccionado es:", numero)
