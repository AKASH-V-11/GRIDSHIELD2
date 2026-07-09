import streamlit as st
import pandas as pd
from data.grid_data import grid_data

def show_state_status():

    st.subheader("🗺️ State Grid Status")

    rows = []

    for state in grid_data["states"]:

        rows.append({

            "State": state["name"],

            "Generation (GW)": state["generation"],

            "Demand (GW)": state["demand"],

            "Status": state["status"],

            "Faults": state["faults"]

        })

    df = pd.DataFrame(rows)

    st.dataframe(df, use_container_width=True, hide_index=True)