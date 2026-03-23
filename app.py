import streamlit as st
import pandas as pd

st.set_page_config(page_title="NDG Linux Game", layout="centered")

# ----------------------
# QUESTIONS
# ----------------------
questions = [
    {"q": "Comando para listar archivos", "a": "ls"},
    {"q": "Listar archivos ocultos", "a": "ls -a"},
    {"q": "Cambiar de directorio", "a": "cd"},
    {"q": "Mostrar ruta actual", "a": "pwd"},
    {"q": "Copiar archivos", "a": "cp"},
    {"q": "Mover archivos", "a": "mv"},
    {"q": "Eliminar archivos", "a": "rm"},
    {"q": "Buscar texto en archivos", "a": "grep"},
    {"q": "Cambiar permisos", "a": "chmod"},
    {"q": "Ver procesos", "a": "ps"},
    {"q": "Ver uso de disco", "a": "df"},
    {"q": "Ver memoria", "a": "free"},
]

# ----------------------
# SESSION STATE
# ----------------------
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.name = ""

# ----------------------
# TITLE
# ----------------------
st.title("🐧 NDG Linux I - Game Challenge")

# ----------------------
# PLAYER NAME
# ----------------------
if st.session_state.name == "":
    name = st.text_input("Ingresa tu nombre:")
    if st.button("Comenzar"):
        if name:
            st.session_state.name = name
            st.rerun()

# ----------------------
# GAME LOGIC
# ----------------------
else:
    if st.session_state.index < len(questions):
        q = questions[st.session_state.index]
        st.subheader(f"Pregunta {st.session_state.index + 1}")
        st.write(q["q"])

        answer = st.text_input("Tu respuesta:", key=st.session_state.index)

        if st.button("Responder"):
            if answer.strip().lower() == q["a"]:
                st.success("✅ Correcto")
                st.session_state.score += 10
            else:
                st.error(f"❌ Incorrecto. Respuesta: {q['a']}")

            st.session_state.index += 1
            st.rerun()

        st.write(f"Puntaje actual: {st.session_state.score}")

    else:
        st.success("🎉 Juego terminado")
        st.write(f"Jugador: {st.session_state.name}")
        st.write(f"Puntaje final: {st.session_state.score}")

        # Save scores
        try:
            df = pd.read_csv("scores.csv")
        except:
            df = pd.DataFrame(columns=["name", "score"])

        new_row = pd.DataFrame([[st.session_state.name, st.session_state.score]], columns=["name", "score"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv("scores.csv", index=False)

        # Ranking
        df = df.sort_values(by="score", ascending=False)

        st.subheader("🏆 Ranking")

        if len(df) > 0:
            st.write(f"🥇 1er lugar: {df.iloc[0]['name']} - {df.iloc[0]['score']}")
        if len(df) > 1:
            st.write(f"🥈 2do lugar: {df.iloc[1]['name']} - {df.iloc[1]['score']}")
        if len(df) > 2:
            st.write(f"🥉 3er lugar: {df.iloc[2]['name']} - {df.iloc[2]['score']}")

        st.dataframe(df)

        if st.button("Reiniciar"):
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.name = ""
            st.rerun()
