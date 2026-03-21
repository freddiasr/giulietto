import streamlit as st
from player_manager import PlayerManager

player_manager = PlayerManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

st.title("Crea nuovo giocatore")

with st.form("Inserisci i dati richiesti"):
    nome = st.text_input("Nome")
    nickname = st.text_input("Nickname")
    emoji = st.text_input("Emoji")

    submit = st.form_submit_button("Crea giocatore")

if submit:
    if player_manager.create_player(nome, nickname, emoji):
        st.write(f"Giocatore creato:")
        st.write(f"Nome: {nome}")
        st.write(f"Nickname: {nickname}")
        st.write(f"Emoji: {emoji}")

