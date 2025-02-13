import streamlit as st
from revolut import Revolut

# Configurazione dell'API Revolut (DA CONFIGURARE)
REVOLUT_PHONE = "+393486067862"  # Inserisci il tuo numero di telefono
REVOLUT_PIN = "210198"  # Inserisci il PIN (usa un metodo più sicuro!)

def get_revolut_balance():
    try:
        client = Revolut(REVOLUT_PHONE, REVOLUT_PIN)
        balance = client.get_balance()
        return balance
    except Exception as e:
        st.error(f"Errore nel recupero del saldo: {e}")
        return None

# Interfaccia Streamlit
st.title("Dashboard Finanziaria Revolut")

# Recupero saldo
saldo = get_revolut_balance()
if saldo is not None:
    st.subheader("Il tuo saldo attuale:")
    st.write(f"**€ {saldo:,.2f}**")
else:
    st.warning("Impossibile recuperare il saldo. Verifica le credenziali e riprova.")

st.markdown("---")
st.markdown("App sviluppata con ❤️ usando Streamlit")
