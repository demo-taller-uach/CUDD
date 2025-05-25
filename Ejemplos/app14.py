import streamlit as st
import random

st.set_page_config(page_title="Chat Positivo", layout="centered")
st.title("Chatbot Positivo :+1:")

# Lista de mensajes positivos y con un toque de sabiduría
MENSAJES_POSITIVOS = [
    "Eres más fuerte de lo que piensas 💪",
    "A veces lo mejor que puedes hacer es respirar y continuar 🌿",
    "Cada día es una nueva oportunidad 🌅",
    "Lo estás haciendo bien, incluso si no lo ves ahora mismo ✨",
    "Tu valor no depende de lo que logres, sino de quién eres 💖",
    "Las pequeñas victorias también cuentan 🎯",
    "Confía en tu proceso. Todo toma tiempo ⏳",
    "Tu presencia es un regalo para este mundo 🎁",
    "Nunca es tarde para empezar de nuevo 🔄",
    "Sigue adelante. Incluso los pasos pequeños te acercan a tu meta 🚶‍♂️",
    "Estás haciendo lo mejor que puedes, y eso es suficiente 💫"
]

# Entrada del usuario
user_input = st.chat_input("¿Qué te gustaría compartir hoy?")

if user_input:
    st.chat_message("user").write(user_input)
    respuesta = random.choice(MENSAJES_POSITIVOS)
    st.chat_message("assistant").write(respuesta)
