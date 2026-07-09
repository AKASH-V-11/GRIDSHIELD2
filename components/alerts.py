import streamlit as st
from data.grid_data import grid_data

def show_alerts():

    st.subheader("🚨 National Alert Centre")

    if grid_data["faults"] == 0:

        st.success("🟢 NATIONAL GRID STATUS : NORMAL")

        st.info("No active faults detected.")

    else:

        st.error(f"🔴 {grid_data['faults']} ACTIVE FAULT(S) DETECTED")

        st.warning("Emergency teams have been notified.")