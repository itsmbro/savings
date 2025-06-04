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

def invia_sequenza_comandi():
    send_command("forward")
    st.info("Comando AVANTI inviato")
    time.sleep(2)

    send_command("homing")
    st.info("Comando HOMING inviato")
    time.sleep(10)

    send_command("loop")
    st.info("Comando LOOP iniziato")
    time.sleep(10)

    send_command("stop")
    st.info("Comando LOOP interrotto")


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

if st.button("▶️ Avvia Sequenza"):
    invia_sequenza_comandi()
    st.success("Sequenza completata")

# 🔥 Invio temperatura
st.subheader("🧪 Imposta Temperatura")
temp_value = st.number_input("Inserisci la temperatura", min_value=0, max_value=300, step=1)

if st.button("Invia Temperatura"):
    send_command("set_temperature", value=int(temp_value))
    st.success(f"Temperatura {int(temp_value)}°C inviata")
