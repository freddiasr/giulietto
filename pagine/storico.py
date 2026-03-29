import streamlit as st
from game_manager import GameManager
from player_manager import PlayerManager

st.set_page_config(page_title="Storico Partite", layout="wide")

st.title("Storico Partite")

game_manager = GameManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
player_manager = PlayerManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# 🎨 Stile compatto verde
st.markdown("""
<style>
.game-wrapper {
    background: #e8f5e9;
    border: 1px solid #81c784;
    border-left: 6px solid #2e7d32;
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 18px;
}

.player-wrapper {
    background: white;
    border: 1px solid #c8e6c9;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 8px;
}

.player-name {
    font-size: 18px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)


# 🥇 Funzione per medaglie
def get_medal(rank):
    if rank == 1:
        return "🥇"
    elif rank == 2:
        return "🥈"
    elif rank == 3:
        return "🥉"
    return ""


for game in game_manager.games_played():
    game_nr = game["game_nr"]
    game_data = game_manager.get_game_data(game_nr)

    # 🔥 Ordina classifica
    game_data = sorted(game_data, key=lambda x: x["final_rank"])

    st.markdown('<div class="game-wrapper">', unsafe_allow_html=True)
    st.markdown(f"### Partita Numero {game_nr}")

    for player in game_data:
        rank = player["final_rank"]
        medal = get_medal(rank)

        player_nickname = player_manager.get_player_nickname(player["player_id"])
        player_emoji = player_manager.get_player_emoji(player["player_id"]) if hasattr(player_manager, "get_player_emoji") else ""

        st.markdown('<div class="player-wrapper">', unsafe_allow_html=True)

        # 🏆 Nome con posizione + medaglia
        st.markdown(
            f'<div class="player-name">{medal} {rank}° - {player_nickname} {player_emoji}</div>',
            unsafe_allow_html=True
        )

        # 📊 Stat compatte
        c1, c2 = st.columns(2)
        c1.metric("Vite donate", player["lives_donated_total"])
        c2.metric("Vite ricevute", player["lives_received_total"])

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)