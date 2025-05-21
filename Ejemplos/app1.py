# 02_entrada_texto.py
import streamlit as st

nombre = st.text_input("¿Cuál es tu nombre?")
if nombre:
    st.write(f"Hola, {nombre} 👋")
