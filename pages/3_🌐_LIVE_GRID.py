

import streamlit as st
import time

from utils.grid_engine import initialize

initialize()

st.set_page_config(
    page_title="⚡ Live Grid Network",
    page_icon="⚡",
    layout="wide"
)

# ==========================================================
# PAGE STYLE
# ==========================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.main-title{
    font-size:42px;
    font-weight:800;
    color:#00E5FF;
}

.sub-title{
    font-size:18px;
    color:#D9D9D9;
}

.banner{
    background:linear-gradient(90deg,#0B1F3A,#123C69,#0B1F3A);
    padding:18px;
    border-radius:12px;
    border:1px solid #00E5FF;
    text-align:center;
    font-size:20px;
    font-weight:bold;
    color:white;
    box-shadow:0px 0px 15px #0099ff;
}

.section{
    background:#111827;
    padding:18px;
    border-radius:12px;
    border:1px solid #2A4D69;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
"""
st.divider()
<div class="main-title">
🌐GRIDSHIELD LIVE GRID NETWORK🌐

</div>

<div class="sub-title">

National Real-Time Power Grid Monitoring & Operational Awareness System

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# LIVE STATUS BANNER
# ==========================================================

status = st.session_state.grid_status

if status == "NORMAL":

    color = "🟢"

elif status == "WARNING":

    color = "🟡"

else:

    color = "🔴"

current_time = time.strftime("%d-%m-%Y  |  %H:%M:%S")

st.markdown(f"""
<div class="banner">

{color} NATIONAL GRID STATUS : <b>{status}</b>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

🛰 LIVE MONITORING ACTIVE

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

🕒 {current_time}

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# LIVE KPI BAR
# ==========================================================

k1, k2, k3, k4, k5, k6 = st.columns(6)

with k1:

    st.metric(
        "⚡ Generation",
        f"{st.session_state.generation} GW"
    )

with k2:

    st.metric(
        "🔋 Demand",
        f"{st.session_state.demand} GW"
    )

with k3:

    st.metric(
        "📡 Frequency",
        f"{st.session_state.frequency} Hz"
    )

with k4:

    st.metric(
        "🔌 Voltage",
        f"{st.session_state.voltage} kV"
    )

with k5:

    st.metric(
        "🟢 Grid Health",
        f"{st.session_state.health}%"
    )

with k6:

    st.metric(
        "🚨 Active Fault",
        st.session_state.fault
    )

st.markdown("---")
# ==========================================================
# LIVE NATIONAL GRID NETWORK
# ==========================================================

st.header("🛰 LIVE NATIONAL POWER FLOW")

fault = st.session_state.fault

plant = "🟢"
stepup = "🟢"
line765 = "🟢"
regional = "🟢"
substation = "🟢"
distribution = "🟢"
consumer = "🟢"

if fault == "Generator Failure":
    plant = "🔴"

elif fault == "Transformer Failure":
    stepup = "🔴"

elif fault == "Transmission Line Failure":
    line765 = "🔴"

elif fault == "Substation Fire":
    substation = "🔴"

elif fault == "Grid Overload":
    distribution = "🟡"

elif fault == "Lightning Strike":
    line765 = "🟡"


st.markdown(f"""

```text

                        🇮🇳 NATIONAL POWER GRID

{plant}  POWER GENERATION STATION
            │
            ▼
{stepup}  765 kV STEP-UP TRANSFORMER
            │
═══════════════════════════════════════════════════════
{line765} 765 kV NATIONAL TRANSMISSION CORRIDOR
═══════════════════════════════════════════════════════
            │
            ▼
{regional} REGIONAL LOAD DISPATCH CENTRE
            │
            ▼
{substation} STATE GRID SUBSTATION
            │
            ▼
{distribution} DISTRIBUTION TRANSFORMER
            │
═══════════════════════════════════════════════════════
🏠 Domestic      🏥 Hospital      🏭 Industry
═══════════════════════════════════════════════════════
            │
            ▼
{consumer} POWER SUPPLY TO CONSUMERS

```

""")

st.markdown("---")


# ==========================================================
# COMPONENT STATUS
# ==========================================================

st.subheader("⚙ LIVE COMPONENT STATUS")

c1, c2, c3, c4 = st.columns(4)

with c1:

    if plant == "🟢":
        st.success("🏭 Generation Plant\n\nONLINE")
    else:
        st.error("🏭 Generation Plant\n\nFAULT")

with c2:

    if line765 == "🟢":
        st.success("⚡ Transmission\n\nHEALTHY")
    elif line765 == "🟡":
        st.warning("⚡ Transmission\n\nWARNING")
    else:
        st.error("⚡ Transmission\n\nFAILED")

with c3:

    if substation == "🟢":
        st.success("🏢 Substation\n\nONLINE")
    else:
        st.error("🏢 Substation\n\nFAULT")

with c4:

    if distribution == "🟢":
        st.success("🏘 Distribution\n\nNORMAL")
    elif distribution == "🟡":
        st.warning("🏘 Distribution\n\nOVERLOAD")
    else:
        st.error("🏘 Distribution\n\nFAILED")

st.markdown("---")
# ==========================================================
# 📍 LIVE FAULT LOCALIZATION CENTER
# ==========================================================

st.header("📍 LIVE FAULT LOCALIZATION")

FAULT_DATABASE = {

    "Transformer Failure": {
        "state": "Tamil Nadu",
        "district": "Salem",
        "substation": "Salem 400 kV GIS",
        "feeder": "South Feeder-04",
        "equipment": "Transformer T-2",
        "gps": "11.6643° N, 78.1460° E",
        "severity": "🔴 CRITICAL",
        "affected": "43,812 Consumers",
        "restore": "21 Minutes",
        "reason": "Transformer Oil Insulation Breakdown"
    },

    "Transmission Line Failure": {
        "state": "Karnataka",
        "district": "Ballari",
        "substation": "Ballari 765 kV",
        "feeder": "North Corridor-02",
        "equipment": "765 kV Transmission Line",
        "gps": "15.1394° N, 76.9214° E",
        "severity": "🔴 CRITICAL",
        "affected": "118,000 Consumers",
        "restore": "42 Minutes",
        "reason": "Tower Conductor Snap"
    },

    "Generator Failure": {
        "state": "Gujarat",
        "district": "Mundra",
        "substation": "Mundra Thermal Station",
        "feeder": "Generator Unit-03",
        "equipment": "Steam Turbine",
        "gps": "22.8390° N, 69.7216° E",
        "severity": "🟠 HIGH",
        "affected": "86,000 Consumers",
        "restore": "36 Minutes",
        "reason": "Turbine Protection Trip"
    },

    "Substation Fire": {
        "state": "Delhi",
        "district": "Rohini",
        "substation": "Rohini 220 kV",
        "feeder": "Sector-18",
        "equipment": "Control Panel",
        "gps": "28.7495° N, 77.0565° E",
        "severity": "🔴 CRITICAL",
        "affected": "51,200 Consumers",
        "restore": "58 Minutes",
        "reason": "Cable Insulation Fire"
    },

    "Lightning Strike": {
        "state": "Kerala",
        "district": "Idukki",
        "substation": "Idukki Hydro Station",
        "feeder": "Hydro Line-07",
        "equipment": "Transmission Tower",
        "gps": "9.8490° N, 76.9700° E",
        "severity": "🟡 MEDIUM",
        "affected": "18,100 Consumers",
        "restore": "14 Minutes",
        "reason": "Lightning-Induced Flashover"
    },

    "Grid Overload": {
        "state": "Maharashtra",
        "district": "Mumbai",
        "substation": "BKC Grid Station",
        "feeder": "Commercial Zone-05",
        "equipment": "Distribution Transformer",
        "gps": "19.0670° N, 72.8690° E",
        "severity": "🟠 HIGH",
        "affected": "67,500 Consumers",
        "restore": "19 Minutes",
        "reason": "Peak Demand Exceeded"
    }

}

info = FAULT_DATABASE.get(
    st.session_state.fault,
    None
)

if info:

    left, right = st.columns([2, 1])

    with left:

        st.error(f"🚨 ACTIVE EVENT : {st.session_state.fault}")

        st.write(f"**📍 State :** {info['state']}")
        st.write(f"**🏙 District :** {info['district']}")
        st.write(f"**🏢 Substation :** {info['substation']}")
        st.write(f"**🔌 Feeder :** {info['feeder']}")
        st.write(f"**⚙ Equipment :** {info['equipment']}")
        st.write(f"**🛰 GPS :** {info['gps']}")

    with right:

        st.metric(
            "⚠ Severity",
            info["severity"]
        )

        st.metric(
            "👥 Consumers",
            info["affected"]
        )

        st.metric(
            "🕒 ETA",
            info["restore"]
        )

        st.metric(
            "🧠 Root Cause",
            info["reason"]
        )

else:

    st.success("🟢 No active fault detected across the National Grid.")

st.markdown("---")
# ==========================================================
# ⚡ LIVE POWER FLOW & RESTORATION MONITOR
# ==========================================================

st.header("⚡ LIVE POWER FLOW & GRID RESTORATION")

left, right = st.columns([1.4, 1])

# ==========================================================
# POWER FLOW
# ==========================================================

with left:

    generation = st.session_state.generation
    demand = st.session_state.demand

    transmission = round(generation * 0.985, 2)
    substation_power = round(transmission * 0.992, 2)
    distribution_power = round(substation_power * 0.988, 2)
    consumer_power = round(min(distribution_power, demand), 2)

    loss = round(generation - consumer_power, 2)

    st.subheader("🔄 NATIONAL POWER FLOW")

    st.metric("🏭 Generation", f"{generation} GW")

    st.progress(1.00)

    st.markdown("⬇")

    st.metric("⚡ Transmission Network", f"{transmission} GW")

    st.progress(transmission / generation)

    st.markdown("⬇")

    st.metric("🏢 State Substations", f"{substation_power} GW")

    st.progress(substation_power / generation)

    st.markdown("⬇")

    st.metric("🏘 Distribution", f"{distribution_power} GW")

    st.progress(distribution_power / generation)

    st.markdown("⬇")

    st.metric("👥 Consumer Supply", f"{consumer_power} GW")

    st.progress(consumer_power / generation)

    st.error(f"♻ Transmission Loss : {loss} GW")

# ==========================================================
# RESTORATION STATUS
# ==========================================================

with right:

    st.subheader("🔧 LIVE RESTORATION STATUS")

    if st.session_state.fault == "No Fault":

        st.success("🟢 Grid Operating Normally")

        st.progress(1.0)

    else:

        st.write("🚨 Fault Detection")
        st.progress(1.0)

        st.write("⚡ Fault Isolation")
        st.progress(0.95)

        st.write("🚑 Crew Dispatch")
        st.progress(0.82)

        st.write("🛠 Equipment Repair")
        st.progress(0.58)

        st.write("🔄 Grid Synchronization")
        st.progress(0.34)

        st.write("🏠 Power Restoration")
        st.progress(0.18)

        st.warning("⏳ Restoration in Progress")

st.markdown("---")


# ==========================================================
# 🔄 FAULT PROPAGATION TIMELINE
# ==========================================================

st.header("🕒 LIVE FAULT PROPAGATION")

if st.session_state.fault == "No Fault":

    st.success("🟢 No disturbance detected across the National Grid.")

else:

    st.code(f"""
08:14:06  🛰 AI Sensor detected abnormal behaviour

08:14:10  ⚠ {st.session_state.fault}

08:14:18  ⚡ Protection Relay Activated

08:14:24  🔌 Circuit Breaker Opened

08:14:41  🚨 Incident Sent to Command Centre

08:15:05  🤖 AI Root Cause Identified

08:15:29  🚑 Emergency Crew Dispatched

08:16:02  🔄 Backup Transmission Activated

08:17:18  ⚡ Partial Supply Restored

08:19:42  🟢 Grid Stabilization In Progress
""")

st.markdown("---")
# ==========================================================
# ⚙ LIVE EQUIPMENT HEALTH + MINI INDIA STATUS
# ==========================================================

st.header("⚙ NATIONAL GRID EQUIPMENT HEALTH")

l1, l2 = st.columns([1.3, 1])

# ==========================================================
# EQUIPMENT HEALTH
# ==========================================================

with l1:

    transformer = 97
    transmission = 95
    substation = 96
    distribution = 94
    breakers = 99
    relays = 98
    scada = 100
    communication = 97

    if st.session_state.fault == "Transformer Failure":
        transformer = 41

    elif st.session_state.fault == "Transmission Line Failure":
        transmission = 36

    elif st.session_state.fault == "Generator Failure":
        transformer = 78

    elif st.session_state.fault == "Substation Fire":
        substation = 29

    elif st.session_state.fault == "Lightning Strike":
        transmission = 69

    elif st.session_state.fault == "Grid Overload":
        distribution = 63

    st.write("### ⚡ Transformer Fleet")
    st.progress(transformer/100)
    st.write(f"Health : **{transformer}%**")

    st.write("### ⚡ Transmission Network")
    st.progress(transmission/100)
    st.write(f"Health : **{transmission}%**")

    st.write("### 🏢 Substations")
    st.progress(substation/100)
    st.write(f"Health : **{substation}%**")

    st.write("### 🏘 Distribution Network")
    st.progress(distribution/100)
    st.write(f"Health : **{distribution}%**")

    st.write("### ⚙ Circuit Breakers")
    st.progress(breakers/100)
    st.write(f"Health : **{breakers}%**")

    st.write("### 📡 Protection Relays")
    st.progress(relays/100)
    st.write(f"Health : **{relays}%**")

    st.write("### 💻 SCADA Servers")
    st.progress(scada/100)
    st.write(f"Health : **{scada}%**")

    st.write("### 🌐 Communication Network")
    st.progress(communication/100)
    st.write(f"Health : **{communication}%**")


# ==========================================================
# MINI INDIA GRID STATUS
# ==========================================================

with l2:

    st.subheader("🇮🇳 NATIONAL STATUS OVERVIEW")

    st.info("""
🟢 Northern Region      Stable

🟢 Western Region       Stable

🟡 Southern Region      Load Rising

🟢 Eastern Region       Normal

🟢 North Eastern        Stable
""")

    st.markdown("---")

    st.subheader("📡 LIVE OPERATIONAL STATUS")

    st.success("🟢 Thermal Plants : ONLINE")

    st.success("🟢 Hydro Plants : ONLINE")

    st.success("🟢 Solar Parks : ONLINE")

    st.success("🟢 Wind Farms : ONLINE")

    st.success("🟢 Nuclear Stations : ONLINE")

    if st.session_state.fault != "No Fault":

        st.error(f"🔴 Active Incident : {st.session_state.fault}")

    else:

        st.success("🟢 No Active National Fault")

    st.markdown("---")

    st.subheader("🌦 WEATHER IMPACT")

    if st.session_state.fault == "Lightning Strike":

        st.warning("""
⛈ Severe Thunderstorm

⚡ High Lightning Activity

💨 Wind : 48 km/h

🌧 Heavy Rainfall

Risk Level : HIGH
""")

    else:

        st.success("""
☀ Weather Stable

🌡 Temperature : 31°C

💨 Wind : 11 km/h

🌤 Grid Weather Risk : LOW
""")

st.markdown("---")

st.success("🛰 GRIDSHIELD LIVE GRID MONITORING ENGINE ONLINE")

st.caption(
    "⚡ GRIDSHIELD V2.0 | National Real-Time Grid Operations Centre | Developed by AKASH.V"
)