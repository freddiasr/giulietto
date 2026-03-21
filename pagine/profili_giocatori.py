import streamlit as st

st.title("Profili Giocatori")
st.write("In questa pagina potrai creare nuovi giocatori o modificare il profilo degli esistenti")

st.markdown("""
<style>
.card-link,
.card-link:link,
.card-link:focus,
.card-link:visited,
.card-link:hover,
.card-link:active {
    text-decoration: none !important;
    color: inherit !important;
    -webkit-text-decoration: none !important;
}

.card {
    background: linear-gradient(145deg, #1f5f3a, #174a2c);
    padding: 26px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 6px 16px rgba(0,0,0,0.25),
        inset 0 1px 0 rgba(255,255,255,0.05);

    color: #f3f7f4;
    text-align: center;

    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow:
        0 10px 24px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.06);
}

.card h3 {
    margin: 6px 0 10px 0;
    font-weight: 600;
}

.card p {
    opacity: 0.9;
    font-size: 0.95rem;
    margin-bottom: 18px;
}

.card .cta-btn {
    display: inline-block;
    padding: 10px 18px;
    border-radius: 10px;

    background: #3fbf7f;
    color: #083d24;

    font-weight: 600;
    text-decoration: none;

    transition: all 0.2s ease;
}

.card .cta-btn:hover {
    background: #5ed69a;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <a class="card-link" href="/crea_giocatore" target="_self">
        <div class="card">
            <h3>🫥 Crea Giocatore</h3>
            <p>Dovrai inserire nome, nickname ed emoji.</p>
            <div class="cta-btn">INSERISCI</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a class="card-link" href="/modifica_giocatori" target="_self">
        <div class="card">
            <h3>✍️ Modifica Giocatore</h3>
            <p>Modifica giocatori esistenti, potrai cambiare nickname e emoji</p>
            <div class="cta-btn">MODIFICA</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>👤 Vedi Giocatori</h3>
        <p>Visualizza tutti i giocatori</p>
        <a class="cta-btn">VISUALIZZA</a>
    </div>
    """, unsafe_allow_html=True)