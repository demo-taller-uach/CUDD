import time
import streamlit as st

st.set_page_config(page_title="Matrix Terminal", layout="centered")

MATRIX_MESSAGE = [
    "💤 Wake up, Neo... 😎",
    "🤖 The Matrix has you... 🫵",
    "➡️ Follow the white rabbit 🐇",
    "🚪 Knock, knock, Neo. 🫱💊"
]

def matrix_stream():
    line_placeholder = st.empty()  # solo para la línea activa

    for line in MATRIX_MESSAGE:
        current_line = ""
        for char in line:
            current_line += char
            line_placeholder.write(current_line)
            time.sleep(0.05)

        # Cursor parpadeante
        for _ in range(3):
            line_placeholder.write(current_line + "█")
            time.sleep(0.3)
            line_placeholder.write(current_line + " ")
            time.sleep(0.3)

        # Opcional: breve pausa antes de la siguiente línea
        time.sleep(0.4)

matrix_stream()
