import streamlit as st
from game_manager import GameManager
from player_manager import PlayerManager

st.set_page_config(page_title="Storico Partite", layout="wide")

st.title("Storico Partite")

game_manager = GameManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
player_manager = PlayerManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# CSS più compatto + testo ridotto
st.markdown("""
<style>
.game-wrapper {
    background: #e8f5e9;
    border: 1px solid #81c784;
    border-left: 6px solid #2e7d32;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 20px;
}

.player-wrapper {
    background: white;
    border: 1px solid #c8e6c9;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}

.player-name {
    font-size: 16px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 6px;
}

.small-text {
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

for game in game_manager.games_played():
    game_nr = game["game_nr"]
    game_data = game_manager.get_game_data(game_nr)

    # 🔥 ORDINA PER POSIZIONE
    game_data = sorted(game_data, key=lambda x: x["final_rank"])

    st.markdown('<div class="game-wrapper">', unsafe_allow_html=True)
    st.markdown(f"### Partita Numero {game_nr}")

    cols = st.columns(2)

    for i, player in enumerate(game_data):
        player_nickname = player_manager.get_player_nickname(player["player_id"])
        player_emoji = player_manager.get_player_emoji(player["player_id"])

        with cols[i % 2]:
            st.markdown('<div class="player-wrapper">', unsafe_allow_html=True)

            # Nome più compatto
            st.markdown(
                f'<div class="player-name">{player_nickname} {player_emoji}</div>',
                unsafe_allow_html=True
            )

            # Metriche più piccole (usiamo colonne strette)
            c1, c2, c3 = st.columns(3)
            c1.metric("Pos", player["final_rank"])
            c2.metric("Donate", player["lives_donated_total"])
            c3.metric("Ricevute", player["lives_received_total"])

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)