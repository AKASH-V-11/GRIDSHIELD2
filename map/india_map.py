# ==========================================================
# GRIDSHIELD NATIONAL COMMAND MAP
# ==========================================================

import json
import pandas as pd
import streamlit as st
import folium

from folium import GeoJson
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium


# ==========================================================
# LOAD INDIA MAP GEOJSON
# ==========================================================

@st.cache_data
def load_geojson():

    with open(

        "map/india_states.geojson",

        "r",

        encoding="utf-8"

    ) as f:

        geo = json.load(f)

    return geo


# ==========================================================
# VALUE CLEANER
# ==========================================================

def clean_value(value):

    if isinstance(value, (int, float)):

        return float(value)


    return float(

        str(value)

        .replace("GW", "")

        .replace("MW", "")

        .replace("Hz", "")

        .replace("kV", "")

        .replace("%", "")

        .strip()

    )
    # ==========================================================
# COLOR ENGINE
# ==========================================================

def state_color(status):

    if status == "GREEN":

        return "#00C853"


    elif status == "YELLOW":

        return "#FFD600"


    elif status == "RED":

        return "#D50000"


    else:

        return "#9E9E9E"



# ==========================================================
# MAIN FUNCTION
# ==========================================================

def show_india_map(state_data):


    df = pd.DataFrame(state_data)


    india = load_geojson()



    # ======================================================
    # CREATE INDIA MAP
    # ======================================================

    india_map = folium.Map(

        location=[22.8, 79.0],

        zoom_start=5,

        tiles="CartoDB Positron",

        control_scale=True

    )



    # ======================================================
    # DRAW STATES
    # ======================================================


    for feature in india["features"]:


        state_name = feature["properties"]["NAME_1"]


        row = df[df["state"] == state_name]



        if len(row) == 0:


            fill = "#BDBDBD"

            health = "N/A"

            generation = "N/A"

            demand = "N/A"

            frequency = "N/A"

            voltage = "N/A"

            status = "UNKNOWN"



        else:


            row = row.iloc[0]


            fill = state_color(row["status"])


            health = row["health"]

            generation = row["generation"]

            demand = row["demand"]

            frequency = row["frequency"]

            voltage = row["voltage"]

            status = row["status"]



        GeoJson(


            feature,


            style_function=lambda x, color=fill: {


                "fillColor": color,

                "color": "white",

                "weight": 1.5,

                "fillOpacity": 0.75

            },


            tooltip=GeoJsonTooltip(


                fields=["NAME_1"],


                aliases=["State :"],


                sticky=True


            )


        ).add_to(india_map)
            # ======================================================
    # STATE GRID MARKERS
    # ======================================================


    for _, row in df.iterrows():


        popup = f"""

        <b>🇮🇳 {row['state']}</b><br><br>

        ⚡ Grid Status : {row['status']}<br>

        ❤️ Grid Health : {row['health']}%<br>

        🏭 Generation : {row['generation']} GW<br>

        🔌 Demand : {row['demand']} GW<br>

        📡 Frequency : {row['frequency']} Hz<br>

        ⚙ Voltage : {row['voltage']} kV

        """



        folium.CircleMarker(


            location=[

                row["lat"],

                row["lon"]

            ],


            radius=8,


            color="white",


            weight=2,


            fill=True,


            fill_color=state_color(

                row["status"]

            ),


            fill_opacity=1,


            popup=folium.Popup(

                popup,

                max_width=350

            ),


            tooltip=row["state"]


        ).add_to(india_map)





    # ======================================================
    # DISPLAY MAP
    # ======================================================


    map_data = st_folium(


        india_map,


        width=None,


        height=700,


        returned_objects=[

            "last_clicked"

        ]

    )
        # ======================================================
    # NATIONAL GRID STATUS
    # ======================================================


    st.markdown("### 🇮🇳 National Grid Status")


    green = len(

        df[df["status"] == "GREEN"]

    )


    yellow = len(

        df[df["status"] == "YELLOW"]

    )


    red = len(

        df[df["status"] == "RED"]

    )



    c1, c2, c3 = st.columns(3)



    with c1:

        st.success(

            f"🟢 Healthy States : {green}"

        )


    with c2:

        st.warning(

            f"🟡 Warning States : {yellow}"

        )


    with c3:

        st.error(

            f"🔴 Emergency States : {red}"

        )



    st.markdown("---")



    # ======================================================
    # STATE SELECTOR
    # ======================================================


    selected = st.selectbox(


        "🗺 Select State",


        sorted(

            df["state"].tolist()

        )


    )



    state = df[

        df["state"] == selected

    ].iloc[0]



    st.subheader(

        f"⚡ {selected} Grid Report"

    )



    a, b, c = st.columns(3)



    a.metric(

        "❤️ Grid Health",

        f"{state['health']} %"

    )


    b.metric(

        "🏭 Generation",

        f"{state['generation']} GW"

    )


    c.metric(

        "🔌 Demand",

        f"{state['demand']} GW"

    )



    d, e, f = st.columns(3)



    d.metric(

        "📡 Frequency",

        f"{state['frequency']} Hz"

    )


    e.metric(

        "⚙ Voltage",

        f"{state['voltage']} kV"

    )


    f.metric(

        "🚦 Status",

        state["status"]

    )



    # ======================================================
    # STATUS MESSAGE
    # ======================================================


    if state["status"] == "GREEN":


        st.success(

            "🟢 Grid Stable — Normal Operations"

        )


    elif state["status"] == "YELLOW":


        st.warning(

            "🟡 Grid Under Observation — Monitoring Required"

        )


    else:


        st.error(

            "🔴 Emergency Condition — Response Required"

        )
            # ======================================================
    # AI GRID ANALYSIS
    # ======================================================


    st.markdown("---")

    st.subheader("🤖 AI Grid Analysis")


    if state["status"] == "GREEN":


        st.success("""

🧠 AI Assessment

✅ Grid is stable

✅ No overload detected

✅ Generation meets demand

✅ Preventive monitoring active

""")


    elif state["status"] == "YELLOW":


        st.warning("""

🧠 AI Assessment

⚠ Load imbalance detected

⚠ Increase monitoring

⚠ Prepare reserve generation

⚠ Dispatch standby engineers

""")


    else:


        st.error("""

🧠 AI Assessment

🚨 Critical grid condition

🚨 Activate emergency backup

🚨 Notify control centre

🚨 Immediate response required

""")



    # ======================================================
    # LIVE GRID PARAMETERS
    # ======================================================


    st.markdown("---")

    st.subheader("📈 Live Grid Parameters")



    health_value = clean_value(

        state["health"]

    )


    generation_value = clean_value(

        state["generation"]

    )


    demand_value = clean_value(

        state["demand"]

    )


    frequency_value = clean_value(

        state["frequency"]

    )


    voltage_value = clean_value(

        state["voltage"]

    )



    st.progress(

        min(health_value / 100, 1.0)

    )

    st.write(

        f"❤️ Grid Health : {state['health']} %"

    )



    st.progress(

        min(generation_value / 50, 1.0)

    )

    st.write(

        f"🏭 Generation : {state['generation']} GW"

    )



    st.progress(

        min(demand_value / 50, 1.0)

    )

    st.write(

        f"🔌 Demand : {state['demand']} GW"

    )



    st.progress(

        min(frequency_value / 50.5, 1.0)

    )

    st.write(

        f"📡 Frequency : {state['frequency']} Hz"

    )



    st.progress(

        min(voltage_value / 450, 1.0)

    )

    st.write(

        f"⚙ Voltage : {state['voltage']} kV"

    )



    # ======================================================
    # NATIONAL STATISTICS
    # ======================================================


    st.markdown("---")

    st.subheader("📊 National Grid Statistics")



    total_states = len(df)


    healthy = len(

        df[df["status"]=="GREEN"]

    )


    warning = len(

        df[df["status"]=="YELLOW"]

    )


    emergency = len(

        df[df["status"]=="RED"]

    )



    c1,c2,c3,c4 = st.columns(4)



    c1.metric(

        "🇮🇳 States",

        total_states

    )


    c2.metric(

        "🟢 Healthy",

        healthy

    )


    c3.metric(

        "🟡 Warning",

        warning

    )


    c4.metric(

        "🔴 Emergency",

        emergency

    )



    # ======================================================
    # EMERGENCY RECOMMENDATION
    # ======================================================


    st.markdown("---")

    st.subheader("🚨 Emergency Recommendation")



    if emergency > 0:


        st.error("""

🚨 AI Recommendation

• Activate emergency protocol

• Deploy response teams

• Restore critical corridors

• Prioritize essential services

""")


    elif warning > 0:


        st.warning("""

⚠ AI Recommendation

• Monitor load continuously

• Prepare backup generation

• Increase surveillance

""")


    else:


        st.success("""

✅ AI Recommendation

• National Grid Stable

• Normal operation maintained

• Preventive monitoring active

""")



    # ======================================================
    # FOOTER
    # ======================================================


    st.markdown("---")

    st.success(

        "✅ GRIDSHIELD National Monitoring Engine Online"

    )

    st.caption(

        "⚡ GRIDSHIELD — National Intelligent Power Grid Command System"

    )