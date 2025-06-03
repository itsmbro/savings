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

def send_command(action):
    topic = f"{USERNAME}/{ASSET_ID}/{COMMAND_PATH}"
    payload = {
        "ts": int(time.time() * 1000),
        "command": action
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
