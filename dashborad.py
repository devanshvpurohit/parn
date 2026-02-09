import streamlit as st
import pandas as pd
import datetime
import json
from streamlit.runtime.scriptrunner import get_script_run_ctx
import plotly.express as px

st.set_page_config("ESP32 AQI Monitor", layout="wide")

# -------- DATA STORAGE --------
if "data" not in st.session_state:
    st.session_state.data = []

# -------- AQI LOGIC --------
def estimate_aqi(mq):
    if mq < 200:
        return "Good"
    elif mq < 400:
        return "Moderate"
    elif mq < 600:
        return "Unhealthy"
    else:
        return "Hazardous"

# -------- RECEIVE ESP32 DATA --------
ctx = get_script_run_ctx()
if ctx and ctx.request and ctx.request.method == "POST":
    payload = json.loads(ctx.request.body.decode())
    payload["time"] = datetime.datetime.now()
    payload["aqi"] = estimate_aqi(payload["mq135"])
    st.session_state.data.append(payload)

# -------- DASHBOARD --------
st.title("🌫️ ESP32 Air Quality Dashboard")

df = pd.DataFrame(st.session_state.data)

if df.empty:
    st.info("Waiting for data from ESP32 AP...")
    st.stop()

df["time"] = pd.to_datetime(df["time"])

# KPIs
c1, c2, c3, c4 = st.columns(4)
c1.metric("🌡 Temp (°C)", f"{df.temperature.iloc[-1]:.1f}")
c2.metric("💧 Humidity (%)", f"{df.humidity.iloc[-1]:.1f}")
c3.metric("🧪 MQ135", int(df.mq135.iloc[-1]))
c4.metric("📊 AQI", df.aqi.iloc[-1])

# Charts
st.subheader("📈 Trends")
st.plotly_chart(px.line(df, x="time", y="mq135", title="MQ135"), use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(px.line(df, x="time", y="temperature", title="Temperature"), use_container_width=True)
with col2:
    st.plotly_chart(px.line(df, x="time", y="humidity", title="Humidity"), use_container_width=True)

with st.expander("📄 Raw Data"):
    st.dataframe(df.tail(20))
