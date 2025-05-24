import streamlit as st
st.title("Ejemplo de Checkbox")

# Widget: checkbox
mostrar = st.checkbox("Mostrar mensaje secreto")

if mostrar:
    st.success("🎉 ¡Este es el mensaje secreto!")
