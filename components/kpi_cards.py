import streamlit as st
from data.grid_data import grid_data

def show_kpi_cards():

    st.subheader("📊 National Grid Overview")

    row1 = st.columns(4)

    with row1[0]:
        st.metric("⚡ Generation", f"{grid_data['generation']} GW")

    with row1[1]:
        st.metric("🔋 Demand", f"{grid_data['demand']} GW")

    with row1[2]:
        st.metric("🏭 Power Stations", grid_data["stations"])

    with row1[3]:
        st.metric("🏢 Substations", grid_data["substations"])

    row2 = st.columns(4)

    with row2[0]:
        st.metric("👥 Consumers", grid_data["consumers"])

    with row2[1]:
        st.metric("🟢 Grid Health", grid_data["grid_health"])

    with row2[2]:
        st.metric("⚡ Frequency", grid_data["frequency"])

    with row2[3]:
        st.metric("🚨 Active Faults", grid_data["faults"])