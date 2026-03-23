import streamlit as st

st.title("🎮 Linux Challenge - NDG I")

score = 0

st.header("Nivel 1: Listar archivos ocultos")

respuesta = st.text_input("Escribe el comando:")

if respuesta:
    if "ls" in respuesta and "-a" in respuesta:
        st.success("✅ Correcto!")
        score += 1
    else:
        st.error("❌ Intenta de nuevo")

st.write(f"Puntuación: {score}")
