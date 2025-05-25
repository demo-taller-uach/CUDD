# tipos de mensajes 📢 
import streamlit as st

st.set_page_config(page_title="Ejemplo de Mensajes", layout="centered")

st.title("📢 Ejemplo de Mensajes en Streamlit")

st.write("""
Streamlit proporciona funciones para mostrar diferentes tipos de mensajes útiles en una app web.
Aquí puedes ver cómo se ven los diferentes estilos:
""")

# Mensaje de éxito
st.success("✅ ¡Operación completada con éxito!")

# Mensaje informativo
st.info("ℹ️ Este es un mensaje informativo, útil para explicar detalles.")

# Mensaje de advertencia
st.warning("⚠️ Este es un mensaje de advertencia. Algo puede necesitar tu atención.")

# Mensaje de error
st.error("🚨 Ha ocurrido un error. Por favor, verifica los datos ingresados.")

st.divider()

st.subheader("🧪 ¿Cuándo usar cada tipo de mensaje?")
st.markdown("""
- **Success**: cuando una operación ha salido bien.
- **Info**: para comunicar algo neutral o adicional al usuario.
- **Warning**: para advertir de posibles problemas o decisiones que requieren cuidado.
- **Error**: para indicar que algo ha fallado y necesita atención inmediata.
""")
