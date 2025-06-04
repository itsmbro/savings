import streamlit as st
import paho.mqtt.client as mqtt
import ssl
import json
import time

# --- Config MQTT ---
BROKER_URL = "mqtt.servitly-sandbox.com"
PORT = 8883
USERNAME = "eutron"
PASSWORD = "Mmlklklk12"
ASSET_ID = "EUTRON"
COMMAND_PATH = "measures"

def send_command(action, value = None):
    topic = f"{USERNAME}/{ASSET_ID}/{COMMAND_PATH}"
    payload = {
        "ts": int(time.time() * 1000),
        "command": action, 
        "value": value
    }

    client = mqtt.Client(client_id=f"{USERNAME}_WEB")
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2)
    client.connect(BROKER_URL, PORT)
    client.loop_start()
    client.publish(topic, json.dumps(payload))
    client.loop_stop()
    client.disconnect()




# --- Streamlit UI ---
st.set_page_config(page_title="Motor Control", layout="centered")
st.title("📟 ISM2 Remote Control")


if st.button("⬆️ AVANTI"):
    send_command("forward")
    st.success("Comando AVANTI inviato")

if st.button("⬇️ INDIETRO"):
    send_command("backward")
    st.success("Comando INDIETRO inviato")

if st.button("🏠 HOMING"):
    send_command("homing")
    st.success("Comando HOMING inviato")

if st.button("Start Loop"):
    send_command("loop")
    st.success("Comando HOMING inviato")

if st.button("Stop Loop"):
    send_command("stop")
    st.success("Comando HOMING inviato")



# 🔥 Invio temperatura
st.subheader("🧪 Imposta Temperatura")
temp_value = st.number_input("Inserisci la temperatura", min_value=0, max_value=300, step=1)

if st.button("Invia Temperatura"):
    send_command("set_temperature", value=int(temp_value))
    st.success(f"Temperatura {int(temp_value)}°C inviata")

# 🔁 Sequenza di comandi personalizzata
st.subheader("▶️ Sequenza Automatica")

wait_forward = st.number_input("⏱️ Pausa dopo AVANTI (secondi)", min_value=0, max_value=60, value=2)
wait_homing = st.number_input("⏱️ Pausa dopo HOMING (secondi)", min_value=0, max_value=60, value=10)
wait_loop   = st.number_input("⏱️ Pausa dopo START LOOP (secondi)", min_value=0, max_value=60, value=10)

log_box = st.empty()

def invia_sequenza_comandi_dinamica():
    log = []

    send_command("forward")
    log.append("🚀 AVANTI inviato")
    log_box.info("\n".join(log))
    time.sleep(wait_forward)

    send_command("homing")
    log.append("🏠 HOMING inviato")
    log_box.info("\n".join(log))
    time.sleep(wait_homing)

    send_command("loop")
    log.append("🔁 START LOOP inviato")
    log_box.info("\n".join(log))
    time.sleep(wait_loop)

    send_command("stop")
    log.append("⏹️ STOP LOOP inviato")
    log_box.info("\n".join(log))

    st.success("✅ Sequenza completata con successo")

if st.button("▶️ Avvia Sequenza Personalizzata"):
    invia_sequenza_comandi_dinamica()
