import streamlit as st
import random
import time

st.set_page_config(page_title="Scoreggiometro 3000 💨", layout="centered")

st.title("💨 Scoreggiometro 3000")
st.write("Misura l'intensità della puzza... **scientificamente**! 😷🔬")

# 🔬 Introduzione scientifica fake
st.markdown("""
Benvenuto nel *Laboratorio Avanzato di Flatulenze Applicate™*.<br>
Qui, la tua scoreggia viene sottoposta ad analisi molecolare, quantistica e... olfattiva. 💨
""", unsafe_allow_html=True)

# 🧪 Analisi attivata
if st.button("Analizza la scoreggia 💨"):
    
    with st.spinner("📡 Rilevamento particelle di metano in corso..."):
        time.sleep(3)
    
    with st.spinner("🔬 Analisi del coefficiente di devastazione ambientale..."):
        time.sleep(3)
    
    with st.spinner("🧠 Consulto con l'Intelligenza Artificiale dell'odore..."):
        time.sleep(3)
    
    # 💩 Risultato finale
    score = random.randint(0, 100)
    st.write(f"**Intensità della puzza rilevata:** `{score}/100` 💨")

    # Commento scientifico serio-non-serio
    if score < 30:
        st.success("🧼 Classe: *Puzza Leggera™* – Effluvio sopportabile, potrebbe essere stato il gatto.")
    elif score < 70:
        st.warning("🧀 Classe: *Media Tossicità™* – Si consiglia l'apertura di finestre e preghiere silenziose.")
    else:
        st.error("☠️ Classe: *Nube Letale™* – Zona contaminata. Attivare piano di evacuazione d'emergenza.")

    # Barra dell’intensità
    st.progress(score)

    # Emoji bonus
    st.write("**Livello visivo della puzza:**")
    if score < 30:
        st.write("😌 – Lieve come una brezza primaverile.")
    elif score < 70:
        st.write("🤢 – L'effetto gorgonzola è in agguato.")
    else:
        st.write("💀 – Hai aperto un portale infernale.")

    # Titolo onorifico
    st.write("**Titolo conferito:**")
    if score < 30:
        st.balloons()
        st.write("🏅 *Aspirante Profumino* – Onorevole menzione per discrezione.")
    elif score < 70:
        st.write("🎖️ *Dottor Flatulenza* – Per risultati mediamente devastanti.")
    else:
        st.write("👑 *Signore delle Scoregge* – Il tuo regno puzza e tu sei il re.")

else:
    st.write("Premi il bottone per iniziare l'analisi... se hai coraggio 😏")
