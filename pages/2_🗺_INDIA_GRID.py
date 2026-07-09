
import streamlit as st
import folium
from streamlit_folium import st_folium

from map.state_data import STATE_GRID_DATA


st.set_page_config(
    page_title="🇮🇳 India Grid",
    page_icon="⚡",
    layout="wide"
)


# ==========================
# VALUE CLEANER
# ==========================

def clean_value(value):

    return float(
        str(value)
        .replace("GW","")
        .replace("MW","")
        .replace("Hz","")
        .replace("kV","")
        .replace("%","")
        .strip()
    )


st.title("🗺 NATIONAL POWER GRID 🗺")
st.subheader("⚡National Intelligent Power Grid Monitoring System⚡")

st.divider()
# ==========================
# NATIONAL SUMMARY
# ==========================

green = len(
    [s for s in STATE_GRID_DATA if s["status"] == "GREEN"]
)

yellow = len(
    [s for s in STATE_GRID_DATA if s["status"] == "YELLOW"]
)

red = len(
    [s for s in STATE_GRID_DATA if s["status"] == "RED"]
)


c1, c2, c3 = st.columns(3)


with c1:
    st.success(f"🟢 Healthy States : {green}")


with c2:
    st.warning(f"🟡 Warning States : {yellow}")


with c3:
    st.error(f"🔴 Emergency States : {red}")


st.divider()



# ==========================
# INDIA NATIONAL GRID MAP
# ==========================

st.subheader("🗺️ INDIA NATIONAL GRID MAP 🗺️")


india_map = folium.Map(

    location=[22.8,79.0],

    zoom_start=5,

    tiles="CartoDB Positron",

    control_scale=True

)
# ==========================
# 🟢🟡🔴 STATE MARKERS
# ==========================

for state in STATE_GRID_DATA:


    if state["status"] == "GREEN":

        color = "green"
        icon = "ok-sign"


    elif state["status"] == "YELLOW":

        color = "orange"
        icon = "warning-sign"


    else:

        color = "red"
        icon = "remove-sign"



    popup = f"""

    <div style="width:280px;">

    <h4>🇮🇳 {state['state']}</h4>

    🟢 Grid Health : {state['health']}%<br>

    ⚡ Generation : {state['generation']} GW<br>

    🔋 Demand : {state['demand']} GW<br>

    📡 Frequency : {state['frequency']} Hz<br>

    🔌 Voltage : {state['voltage']} kV<br>

    🚦 Status : {state['status']}

    </div>

    """



    folium.Marker(

        location=[

            state["lat"],

            state["lon"]

        ],

        tooltip=state["state"],


        popup=folium.Popup(

            popup,

            max_width=350

        ),


        icon=folium.Icon(

            color=color,

            icon=icon

        )

    ).add_to(india_map)



st_folium(

    india_map,

    width=None,

    height=720

)


st.divider()
# ==========================
# ⚡ NATIONAL GRID DASHBOARD
# ==========================

st.header("⚡ NATIONAL GRID DASHBOARD")


total_generation = round(

    sum(
        clean_value(s["generation"])
        for s in STATE_GRID_DATA
    ),

    2

)


total_demand = round(

    sum(
        clean_value(s["demand"])
        for s in STATE_GRID_DATA
    ),

    2

)


avg_health = round(

    sum(
        clean_value(s["health"])
        for s in STATE_GRID_DATA
    )
    /
    len(STATE_GRID_DATA),

    2

)


avg_frequency = round(

    sum(
        clean_value(s["frequency"])
        for s in STATE_GRID_DATA
    )
    /
    len(STATE_GRID_DATA),

    2

)


avg_voltage = round(

    sum(
        clean_value(s["voltage"])
        for s in STATE_GRID_DATA
    )
    /
    len(STATE_GRID_DATA),

    2

)



c1, c2, c3, c4, c5 = st.columns(5)



with c1:

    st.metric(

        "⚡ Generation",

        f"{total_generation:.2f} GW"

    )



with c2:

    st.metric(

        "🔋 Demand",

        f"{total_demand:.2f} GW"

    )



with c3:

    st.metric(

        "🟢 Grid Health",

        f"{avg_health:.1f}%"

    )



with c4:

    st.metric(

        "📡 Frequency",

        f"{avg_frequency:.2f} Hz"

    )



with c5:

    st.metric(

        "🔌 Voltage",

        f"{avg_voltage:.0f} kV"

    )


st.divider()
# ==========================
# 🚨 LIVE NATIONAL ALERTS
# ==========================

st.header("🚨 NATIONAL GRID ALERTS")


red_states = [

    s for s in STATE_GRID_DATA

    if s["status"] == "RED"

]


yellow_states = [

    s for s in STATE_GRID_DATA

    if s["status"] == "YELLOW"

]


green_states = [

    s for s in STATE_GRID_DATA

    if s["status"] == "GREEN"

]



if len(red_states):

    st.error(
        f"🚨 {len(red_states)} State(s) are under EMERGENCY."
    )


elif len(yellow_states):

    st.warning(
        f"⚠ {len(yellow_states)} State(s) require monitoring."
    )


else:

    st.success(
        "✅ National Power Grid is Stable."
    )



st.divider()



# ==========================
# 🤖 AI COMMAND CENTER
# ==========================

st.header("🤖 AI GRID COMMAND CENTER")


if len(red_states):

    st.error("""

🚨 AI Recommendation

• Activate National Emergency Protocol

• Dispatch Central Grid Engineers

• Restore Critical Transmission Lines

• Prioritize Hospitals & Essential Services

• Enable Backup Generation

""")


elif len(yellow_states):

    st.warning("""

⚠ AI Recommendation

• Monitor Grid Load

• Increase Reserve Generation

• Dispatch Standby Teams

• Watch Frequency Stability

""")


else:

    st.success("""

✅ AI Recommendation

• Grid Stable

• Continue Preventive Monitoring

• No Critical Threat Detected

""")



st.divider()



# ==========================
# 📈 NATIONAL GRID HEALTH
# ==========================

st.header("📈 NATIONAL GRID HEALTH")


st.progress(

    avg_health / 100

)

st.write(

    f"Overall Grid Health : **{avg_health}%**"

)



st.progress(

    total_generation /

    (total_generation + 5)

)

st.write(

    f"National Generation : **{total_generation:.2f} GW**"

)



st.progress(

    total_demand /

    (total_generation + 5)

)

st.write(

    f"National Demand : **{total_demand:.2f} GW**"

)



st.divider()


st.success(
    "⚡ GRIDSHIELD National Grid Monitoring System Online 🗺"
)