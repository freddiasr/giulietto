import streamlit as st
from streamlit import dialog

from player_manager import PlayerManager

player_manager = PlayerManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

st.title("Scegli il profilo da modificare")

@st.dialog("Modifica Profilo")
def modifica_profilo(id_db):
    with st.form("Inserisci i nuovi dati"):
        nickname = st.text_input("Nickname")
        emoji = st.text_input("Emoji")

        submit = st.form_submit_button("CONFERMA")

        if submit:
            if player_manager.modify_player(id_db, nickname, emoji):
                st.write(f"Giocatore modificato")

player_list = player_manager.available_players()

for player in player_list:
    st.write(f"Nome: {player["name"]} - Nickname: {player['nickname']} - Emoji: {player['emoji']}")
    if st.button("MODIFICA", key=player["id"]):
        modifica_profilo(player["id"])




