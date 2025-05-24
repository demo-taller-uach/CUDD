import streamlit as st
import datetime

st.title("Ejemplo de fecha")

# Widget: date_input
fecha = st.date_input("Selecciona una fecha", value=datetime.date.today())

st.write("La fecha seleccionada es:", fecha)
