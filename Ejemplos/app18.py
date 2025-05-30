import streamlit as st
from openai import OpenAI

# Título y descripción
st.title("💬 Chatbot con contexto local")

# Carga la clave de API desde los secretos
openai_api_key = st.secrets["api_key"] 

# Crea un cliente de OpenAI
client = OpenAI(api_key=openai_api_key)

# Lee el contenido del archivo local
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        contexto_local = f.read()
except FileNotFoundError:
    st.error("No se encontró el archivo 'archivo.txt'. Asegúrate de que esté en el mismo directorio.")
    st.stop()

# Entrada del usuario
prompt = st.chat_input("Escribe tu mensaje:")
if prompt is None:
    st.stop()

# Mostrar mensaje del usuario
with st.chat_message("user"):
    st.markdown(prompt)

# Llamada al modelo con el contexto incluido
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"Usa el siguiente contexto como referencia para responder: \n\n{contexto_local}"},
        {"role": "user", "content": prompt}
    ],
    max_tokens=800,
    temperature=0,
)

# Mostrar respuesta del asistente
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
    st.write(respuesta)
