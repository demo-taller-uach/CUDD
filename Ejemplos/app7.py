import streamlit as st
import pandas as pd

st.title("Ejemplo de carga de archivos")

# Widget: file_uploader
archivo = st.file_uploader("Sube un archivo CSV", type="csv")

if archivo:
    df = pd.read_csv(archivo)
    st.dataframe(df)
