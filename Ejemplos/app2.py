# 03_operaciones_numeros.py
import streamlit as st

a = st.number_input("Ingresa un número", value=0)
b = st.number_input("Ingresa otro número", value=0)

st.write("Suma:", a + b)
st.write("Producto:", a * b)
