import streamlit as st
import plotly.graph_objects as go
from data.grid_data import grid_data

def show_grid_chart():

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Generation","Demand"],
        y=[
            grid_data["generation"],
            grid_data["demand"]
        ]
    ))

    fig.update_layout(

        title="⚡ National Grid Power",

        template="plotly_dark",

        height=400

    )

    st.plotly_chart(fig, use_container_width=True)