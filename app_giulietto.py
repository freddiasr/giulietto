import streamlit as st

st.set_page_config(
    page_title="Gioco di Giulietto",
    layout="wide",
    page_icon="🎮"
)

homepage = st.Page(page="pagine/homepage.py", title="Home", icon="🏠")
nuova_partita = st.Page(page="pagine/nuova_partita.py", title="Nuova Partita", icon="🃏")
profili_giocatori = st.Page(page="pagine/profili_giocatori.py", title="Profili Giocatori", icon="👤")
statistiche = st.Page(page="pagine/statistiche.py", title="Statistiche", icon="📊")
storico = st.Page(page="pagine/storico.py", title="Storico Partite", icon="📖")
crea_giocatore = st.Page(page="pagine/crea_giocatore.py", visibility="hidden")
modifica_giocatori = st.Page(page="pagine/modifica_giocatori.py", visibility="hidden")

navigation = st.navigation(
    [homepage, nuova_partita, profili_giocatori, statistiche, storico, crea_giocatore, modifica_giocatori],
    position="top"
)

navigation.run()