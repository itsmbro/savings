import streamlit as st
import random

st.set_page_config(page_title="Scoreggiometro 3000 💨", layout="centered")

st.title("💨 Scoreggiometro 3000")
st.write("Misura l'intensità della puzza... scientificamente! 😷")

if st.button("Analizza la scoreggia 💨"):
    score = random.randint(0, 100)
    
    st.write(f"**Intensità della puzza:** {score}/100")

    if score < 30:
        st.success("Puzza leggera 🌸 – si può sopravvivere.")
    elif score < 70:
        st.warning("Puzza media 🧀 – non proprio una passeggiata.")
    else:
        st.error("PUZZA TOSSICA ☠️ – evacuare immediatamente!")

    # Barra di "intensità"
    st.progress(score)
    
    # Emoji bonus
    st.write("Livello visivo della puzza:")
    if score < 30:
        st.write("😌")
    elif score < 70:
        st.write("🤢")
    else:
        st.write("💀")

else:
    st.write("Premi il bottone per iniziare l'analisi... se hai coraggio 😏")
