import streamlit as st
from player_manager import PlayerManager
from game_manager import GameManager
from datetime import date

player_manager = PlayerManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
game_manager = GameManager(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
player_list = player_manager.available_players()

st.title("Benvenuti in una nuova partita")

# Inizializza session state
if "step" not in st.session_state:
    st.session_state.step = 1

if "nr_giocatori" not in st.session_state:
    st.session_state.nr_giocatori = 0

if "game_data" not in st.session_state:
    st.session_state.game_data = []

if "game_nr" not in st.session_state:
    st.session_state.game_nr = game_manager.new_game_nr()


def create_player_data(id_partita, giocatore, posizione, vite_donate, vite_ricevute):
    return {
        "game_id": id_partita,
        "player_id": giocatore,
        "final_rank": posizione,
        "lives_donated_total": vite_donate,
        "lives_received_total": vite_ricevute,
    }


def reset_partita():
    st.session_state.step = 1
    st.session_state.nr_giocatori = 0
    st.session_state.game_data = []
    st.session_state.game_nr = game_manager.new_game_nr()


# STEP 1: numero giocatori
if st.session_state.step == 1:
    with st.form("numero_giocatori_form"):
        nr_giocatori = st.number_input("Numero di giocatori", min_value=1, step=1)
        submit_nr = st.form_submit_button("CONFERMA")

        if submit_nr:
            st.session_state.nr_giocatori = nr_giocatori
            st.session_state.step = 2
            st.rerun()


# STEP 2: inserimento dati giocatori
elif st.session_state.step == 2:
    st.write(
        f"Giocatori inseriti: {len(st.session_state.game_data)} / {st.session_state.nr_giocatori}"
    )

    with st.form("dati_giocatore_form"):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            scelta = st.selectbox(
                "Scegli Giocatore",
                player_list,
                format_func=lambda x: x["name"]
            )
        with col2:
            posizione = st.number_input("Posizione finale", min_value=1, step=1)
        with col3:
            vite_donate = st.number_input("Vite donate", min_value=0, step=1)
        with col4:
            vite_ricevute = st.number_input("Vite ricevute", min_value=0, step=1)

        submit_player = st.form_submit_button("AGGIUNGI GIOCATORE")

        if submit_player:
            st.session_state.game_data.append(
                create_player_data(
                    st.session_state.game_nr,
                    scelta["id"],
                    posizione,
                    vite_donate,
                    vite_ricevute
                )
            )

            if len(st.session_state.game_data) >= st.session_state.nr_giocatori:
                st.session_state.step = 3

            st.rerun()

    if st.session_state.game_data:
        st.subheader("Giocatori già inseriti")
        for i, player in enumerate(st.session_state.game_data, start=1):
            nome = next(
                (p["name"] for p in player_list if p["id"] == player["player_id"]),
                "Sconosciuto"
            )
            st.write(
                f"{i}. {nome} - Posizione: {player['final_rank']}, "
                f"Vite donate: {player['lives_donated_total']}, "
                f"Vite ricevute: {player['lives_received_total']}"
            )


# STEP 3: note e salvataggio finale
elif st.session_state.step == 3:
    with st.form("note_partita_form"):
        note_partita = st.text_input("Note Partita")
        submit_save = st.form_submit_button("SALVA PARTITA")

        if submit_save:
            game_date = str(date.today())

            game_manager.new_game(st.session_state.game_nr, game_date)

            if note_partita:
                game_manager.new_note(st.session_state.game_nr, note_partita)

            for player in st.session_state.game_data:
                game_manager.new_game_player_data(
                    player["game_id"],
                    player["player_id"],
                    player["final_rank"],
                    player["lives_donated_total"],
                    player["lives_received_total"]
                )

            st.success("Partita salvata correttamente!")
            reset_partita()
            st.rerun()