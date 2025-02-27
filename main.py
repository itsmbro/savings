import streamlit as st
import openai
import json
import os
import base64
import requests
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import re

# Configurazione delle API
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Configurazione GitHub
GITHUB_USER = "itsmbro"
GITHUB_REPO = "savings"
GITHUB_BRANCH = "main"
GITHUB_FILE_PATH = "financial_data.json"

# Funzione per caricare financial_data.json da GitHub
def load_financial_data():
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{GITHUB_FILE_PATH}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        # JSON iniziale con le variabili finanziarie
        financial_data = {
            "obiettivo": 10000,
            "scadenza": "2025-09-01",
            "saldo": 600,
            "versamento_mensile": 0
        }
        save_financial_data(financial_data)
        return financial_data

# Funzione per salvare financial_data.json su GitHub
def save_financial_data(financial_data):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {
        "Authorization": f"token {st.secrets['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    sha = response.json().get("sha") if response.status_code == 200 else None

    json_data = json.dumps(financial_data, ensure_ascii=False, indent=4)
    json_base64 = base64.b64encode(json_data.encode()).decode()

    data = {
        "message": "Aggiornamento financial_data.json",
        "content": json_base64,
        "branch": GITHUB_BRANCH
    }

    if sha:
        data["sha"] = sha  

    response = requests.put(url, headers=headers, json=data)
    if response.status_code not in [200, 201]:
        st.error(f"Errore aggiornamento GitHub: {response.json()}")

# Genera il prompt iniziale con il contesto
def generate_initial_prompt(financial_data):
    oggi = datetime.date.today()
    return (
        "Sei il mio consulente finanziario. Aiutami a gestire il mio obiettivo economico.\n"
        "Il mio obiettivo economico è quello di risparmiare una certa somma di denaro entro una data di scadenza.\n"
        "Gestiamo un file JSON in Python che contiene le mie informazioni finanziarie.\n"
        "Il JSON attuale con le informazioni finanziarie è il seguente:\n\n"
        "00000000\n"
        f"{json.dumps(financial_data, ensure_ascii=False, indent=4)}\n"
        "00000000\n\n"
        "Puoi aggiornare il JSON quando necessario, senza aggiungere nuove informazioni inutili. Quando vuoi aggiornare il file JSON, devi farlo seguendo il formato ESATTO come te l'ho riportato io (nota gli zeri).\n"
        f"ogni volta che ti dico di aggiornare qualsiasi cosa, come ad esempio l'obiettivo, il saldo, o la scadenza, usa la semplice matematica di base per ricalcolare tutto. (ad esempio, se ti chiedo di aggiornare il saldo, va ricalcolato tutto, non solo il saldo... così per tutti i campi). Se devi fare conti con le date, considera che oggi è {oggi}. Infine, non è necessario che nella risposta scrivi ogni volta tutti i ragionamenti che fai, sii conciso nello scrivere i tuoi ragionamenti. "
    )

# Funzione per aggiornare financial_data.json dalle risposte di ChatGPT
def update_financial_data_from_response(response_text, financial_data):
    match = re.search(r'00000000\n(.*?)\n00000000', response_text, re.DOTALL)
    if match:
        try:
            new_data = json.loads(match.group(1))
            financial_data.update(new_data)
            save_financial_data(financial_data)
            return response_text.replace(match.group(0), "").strip()
        except json.JSONDecodeError:
            pass  
    return response_text

# Carichiamo il JSON da GitHub
financial_data = load_financial_data()
initial_prompt = generate_initial_prompt(financial_data)

# Inizializza la sessione della chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": initial_prompt}]

# Mostra la cronologia dei messaggi
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input utente
if user_input := st.chat_input("Sono il tuo coach finanziario💰... "):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Richiesta a ChatGPT
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
            temperature=0.7
        )
        bot_response = response["choices"][0]["message"]["content"]

        # Aggiorna financial_data.json se necessario
        updated_response = update_financial_data_from_response(bot_response, financial_data)

        # Mostra la risposta nella chat
        with st.chat_message("assistant"):
            st.markdown(updated_response)

        # Salva il messaggio nella sessione
        st.session_state.messages.append({"role": "assistant", "content": updated_response})

    except Exception as e:
        st.error(f"Errore nella comunicazione con OpenAI: {str(e)}")

# Grafico a torta per mostrare quanto manca per raggiungere l'obiettivo
def mostra_grafico_torta(obiettivo, saldo):
    progresso = saldo / obiettivo * 100
    restante = 100 - progresso

    fig = go.Figure(data=[go.Pie(labels=["Raggiunto", "Mancante"], values=[progresso, restante], hole=0.3)])
    fig.update_layout(title="Progresso Versamento Obiettivo")
    st.plotly_chart(fig)

# Mostra la dashboard con obiettivo, saldo e versamento consigliato
st.title("📊Dashboard Finanziaria📊")
st.subheader(f"🎯Obiettivo Economico: {financial_data['obiettivo']} €")
st.subheader(f"💰Saldo Attuale: {financial_data['saldo']} €")
st.subheader(f"Versamento mensile: {financial_data['versamento_mensile']} €")
st.subheader(f"📅Scadenza: {financial_data['scadenza']}")

# Mostra il grafico a torta
mostra_grafico_torta(financial_data['obiettivo'], financial_data['saldo'])
