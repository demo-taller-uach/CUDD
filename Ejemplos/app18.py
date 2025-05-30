import streamlit as st
from openai import OpenAI

# Título
st.title("💬 Chatbot con contexto local (desde archivo.txt)")

# Cargar clave desde secretos
openai_api_key = st.secrets["api_key"]
client = OpenAI(api_key=openai_api_key)

# Leer contenido del archivo.txt
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        contexto_local = f.read()
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'archivo.txt'. Asegúrate de que esté en el mismo directorio que 'app.py'.")
    st.stop()

# Entrada del usuario
prompt = st.chat_input("Haz tu pregunta sobre modelos GPT...")
if prompt is None:
    st.stop()

# Mostrar entrada del usuario
with st.chat_message("user", avatar="🦖"):
    st.markdown(prompt)

# Llamada al modelo con contexto desde archivo.txt
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"Usa el siguiente contexto para responder preguntas sobre modelos GPT:\n\n{contexto_local}"},
        {"role": "user", "content": prompt}
    ],
    max_tokens=800,
    temperature=0,
)

# Mostrar respuesta
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
    st.write(respuesta)
