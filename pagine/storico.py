import streamlit as st
from game_manager import GameManager
from player_manager import PlayerManager

st.title("Storico Partite")

game_manager = GameManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
player_manager = PlayerManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

for game in game_manager.games_played():
    st.write(f"**Partita Numero {game['game_nr']}**")
    game_data = game_manager.get_game_data(game["game_nr"])
    for player in game_data:
        player_nickname = player_manager.get_player_nickname(player["player_id"])
        rank = player["final_rank"]
        vite_donate = player["lives_donated_total"]
        vite_ricevute = player["lives_received_total"]
        st.write(f"**{player_nickname}**")
        st.write(f"Posizione: {rank}")
        st.write(f"Vite donate: {vite_donate}")
        st.write(f"Vite ricevute: {vite_ricevute}")

