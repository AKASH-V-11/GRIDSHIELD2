import streamlit as st
import pandas as pd
import numpy as np
import random
import time

from utils.grid_engine import initialize

initialize()

st.set_page_config(
    page_title="📊 GRIDSHIELD National Analytics",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.title{
    font-size:42px;
    font-weight:900;
    color:#00E5FF;
}

.subtitle{
    font-size:18px;
    color:#BBBBBB;
}

.card{
    background:#111111;
    padding:20px;
    border-radius:15px;
    border:1px solid #333;
}

.banner{
    background:linear-gradient(90deg,#001F3F,#003566,#001F3F);
    padding:18px;
    border-radius:15px;
    text-align:center;
    font-size:22px;
    font-weight:bold;
    color:white;
    border:2px solid cyan;
    box-shadow:0px 0px 15px cyan;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
st.divider() 
<div class="title">
📊 NATIONAL ANALYTICS CENTER 📊

</div>

<div class="subtitle">

AI Powered Power Grid Intelligence • Predictive Analytics • National Insights

</div>
""", unsafe_allow_html=True)

st.write("")

# ============================================================
# LIVE STATUS
# ============================================================

if st.session_state.grid_status == "STABLE":

    emoji = "🟢"

elif st.session_state.grid_status == "WARNING":

    emoji = "🟡"

else:

    emoji = "🔴"

st.markdown(f"""
<div class="banner">

{emoji} GRID STATUS : {st.session_state.grid_status}

&nbsp;&nbsp;&nbsp;&nbsp;

📅 {time.strftime("%d-%m-%Y")}

&nbsp;&nbsp;&nbsp;&nbsp;

🕒 {time.strftime("%H:%M:%S")}

</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================================
# NATIONAL KPIs
# ============================================================

a,b,c,d,e,f = st.columns(6)

with a:
    st.metric(
        "⚡ Generation",
        f"{st.session_state.generation} GW"
    )

with b:
    st.metric(
        "🔋 Demand",
        f"{st.session_state.demand} GW"
    )

with c:
    st.metric(
        "📡 Frequency",
        f"{st.session_state.frequency} Hz"
    )

with d:
    st.metric(
        "🔌 Voltage",
        f"{st.session_state.voltage} kV"
    )

with e:
    st.metric(
        "💚 Grid Health",
        f"{st.session_state.health}%"
    )

with f:
    st.metric(
        "🚨 Active Fault",
        st.session_state.fault
    )

st.divider()
# ============================================================
# 🇮🇳 EXECUTIVE PERFORMANCE DASHBOARD
# ============================================================

st.header("📊 NATIONAL EXECUTIVE PERFORMANCE DASHBOARD 📊")

generation = st.session_state.generation
demand = st.session_state.demand
health = st.session_state.health
frequency = st.session_state.frequency
voltage = st.session_state.voltage

reserve = round(generation - demand,2)

efficiency = round(
((generation/max(demand,1))*100),
2
)

stability = round(
(
(health*0.55)
+
((frequency/50)*100)*0.25
+
((voltage/400)*100)*0.20
),
2
)

x1,x2,x3 = st.columns(3)

with x1:

    st.metric(
        "⚡ Reserve Capacity",
        f"{reserve} GW"
    )

    st.metric(
        "📊 Grid Efficiency",
        f"{efficiency}%"
    )

with x2:

    st.metric(
        "🧠 Stability Index",
        f"{stability}%"
    )

    st.metric(
        "🌍 Carbon Saved",
        f"{random.randint(2200,5800)} tCO₂"
    )

with x3:

    st.metric(
        "💰 Operational Savings",
        f"₹{random.randint(120,580)} Cr"
    )

    st.metric(
        "🏭 Active Stations",
        f"{random.randint(620,760)}"
    )

st.divider()

# ============================================================
# 🛰 LIVE GRID STATUS
# ============================================================

st.header("🛰 LIVE GRID STATUS")

left,right = st.columns([2,1])

with left:

    if health >= 96:

        st.success("""
🟢 NATIONAL GRID OPERATING NORMALLY

✔ Frequency Stable

✔ Voltage Stable

✔ Generation Meets Demand

✔ AI Monitoring Active

✔ No Cascading Risk Detected
""")

    elif health >=85:

        st.warning("""
🟡 NATIONAL GRID UNDER OBSERVATION

✔ Minor Oscillations Detected

✔ AI Preventive Actions Enabled

✔ Regional Monitoring Increased
""")

    else:

        st.error("""
🔴 NATIONAL GRID ALERT

✔ Emergency Protocol Active

✔ Grid Restoration Underway

✔ AI Emergency Control Enabled
""")

with right:

    st.metric(
        "⚡ Grid Frequency",
        f"{frequency} Hz"
    )

    st.metric(
        "🔌 Voltage Level",
        f"{voltage} kV"
    )

    st.metric(
        "❤️ Health",
        f"{health}%"
    )

st.divider()

# ============================================================
# 📈 NATIONAL POWER MIX
# ============================================================

st.header("📈 NATIONAL POWER GENERATION MIX")

mix = pd.DataFrame({

    "Source":[
        "Thermal",
        "Hydro",
        "Solar",
        "Wind",
        "Nuclear"
    ],

    "GW":[
        210,
        82,
        63,
        44,
        61
    ]

})

st.bar_chart(
    mix,
    x="Source",
    y="GW",
    use_container_width=True
)

st.divider()
# ============================================================
# 🇮🇳 STATE GRID PERFORMANCE RANKING
# ============================================================

st.header("STATE GRIDS PERFORMANCE RANKING")

states = pd.DataFrame({

    "State":[
        "Tamil Nadu",
        "Karnataka",
        "Maharashtra",
        "Gujarat",
        "Kerala",
        "Telangana",
        "Andhra Pradesh",
        "Rajasthan",
        "Odisha",
        "Punjab",
        "Haryana",
        "Delhi",
        "Uttar Pradesh",
        "West Bengal",
        "Assam"
    ],

    "Grid Health":[
        99,
        98,
        97,
        97,
        96,
        96,
        95,
        95,
        94,
        94,
        93,
        93,
        92,
        91,
        90
    ],

    "Availability (%)":[
        99.8,
        99.6,
        99.5,
        99.4,
        99.3,
        99.2,
        99.0,
        98.9,
        98.8,
        98.7,
        98.5,
        98.3,
        98.1,
        97.8,
        97.5
    ]

})

left,right = st.columns([1.3,1])

with left:

    st.dataframe(
        states,
        hide_index=True,
        use_container_width=True
    )

with right:

    st.bar_chart(
        states,
        x="State",
        y="Grid Health",
        use_container_width=True
    )

st.divider()

# ============================================================
# 🤖 AI FAILURE PREDICTION
# ============================================================

st.header("🤖 AI FAILURE PREDICTION ENGINE")

prediction = pd.DataFrame({

    "Equipment":[
        "Transformer",
        "Transmission Line",
        "Generator",
        "Circuit Breaker",
        "Busbar",
        "Battery Bank",
        "Solar Farm",
        "Wind Farm"
    ],

    "Failure Risk (%)":[
        18,
        9,
        27,
        13,
        16,
        11,
        6,
        8
    ]

})

left,right = st.columns([1.2,1])

with left:

    st.dataframe(
        prediction,
        hide_index=True,
        use_container_width=True
    )

with right:

    st.bar_chart(
        prediction,
        x="Equipment",
        y="Failure Risk (%)",
        use_container_width=True
    )

st.divider()

# ============================================================
# ⚠ NATIONAL RISK MATRIX
# ============================================================

st.header("⚠ NATIONAL RISK MATRIX")

r1,r2,r3,r4 = st.columns(4)

with r1:

    st.metric(
        "🔴 Critical Assets",
        random.randint(2,7)
    )

with r2:

    st.metric(
        "🟠 High Risk Assets",
        random.randint(12,22)
    )

with r3:

    st.metric(
        "🟡 Medium Risk Assets",
        random.randint(40,75)
    )

with r4:

    st.metric(
        "🟢 Healthy Assets",
        random.randint(320,420)
    )

st.progress(0.91)

st.info(
"""
🛰 AI has completed nationwide asset risk analysis.

No cascading blackout pattern detected.

Continuous monitoring remains active across the National Grid.
"""
)

st.divider()
# ============================================================
# 🌍 RENEWABLE ENERGY INTELLIGENCE CENTER
# ============================================================

st.header("🌍 RENEWABLE ENERGY INTELLIGENCE CENTER")

renewable = pd.DataFrame({

    "Source":[
        "Solar",
        "Wind",
        "Hydro",
        "Biomass",
        "Small Hydro"
    ],

    "Generation (GW)":[
        82,
        61,
        48,
        16,
        9
    ]

})

left,right = st.columns([1.2,1])

with left:

    st.dataframe(
        renewable,
        hide_index=True,
        use_container_width=True
    )

with right:

    st.bar_chart(
        renewable,
        x="Source",
        y="Generation (GW)",
        use_container_width=True
    )

st.divider()

# ============================================================
# 📈 NEXT 24-HOUR DEMAND FORECAST
# ============================================================

st.header("📈 AI 24-HOUR LOAD FORECAST")

hours = [f"{h}:00" for h in range(24)]

forecast = pd.DataFrame({

    "Hour":hours,

    "Forecast Demand (GW)":[
        random.randint(410,480)
        for _ in range(24)
    ]

})

st.line_chart(
    forecast,
    x="Hour",
    y="Forecast Demand (GW)",
    use_container_width=True
)

peak = forecast["Forecast Demand (GW)"].max()

st.success(
    f"⚡ Predicted Peak Demand : {peak} GW"
)

st.divider()

# ============================================================
# 🛰 REGIONAL POWER FLOW ANALYSIS
# ============================================================

st.header("🛰 REGIONAL POWER FLOW ANALYSIS")

flow = pd.DataFrame({

    "Region":[
        "Northern",
        "Southern",
        "Eastern",
        "Western",
        "North Eastern"
    ],

    "Import (GW)":[
        22,
        18,
        14,
        16,
        5
    ],

    "Export (GW)":[
        18,
        26,
        12,
        19,
        4
    ]

})

st.dataframe(
    flow,
    hide_index=True,
    use_container_width=True
)

st.divider()

# ============================================================
# 💰 NATIONAL GRID FINANCIAL ANALYTICS
# ============================================================

st.header("💰 NATIONAL GRID FINANCIAL ANALYTICS")

f1,f2,f3,f4 = st.columns(4)

with f1:

    st.metric(
        "💵 Revenue Today",
        f"₹ {random.randint(820,980)} Cr"
    )

with f2:

    st.metric(
        "🛠 Maintenance Cost",
        f"₹ {random.randint(90,170)} Cr"
    )

with f3:

    st.metric(
        "⚡ Energy Trading",
        f"₹ {random.randint(180,320)} Cr"
    )

with f4:

    st.metric(
        "📈 Net Savings",
        f"₹ {random.randint(350,520)} Cr"
    )

st.divider()

# ============================================================
# 🤖 AI OPERATIONAL INTELLIGENCE
# ============================================================

st.header("🤖 AI OPERATIONAL INTELLIGENCE")

left,right = st.columns([2,1])

with left:

    st.info("""

🧠 GRIDSHIELD AI OBSERVATIONS

✅ National load distribution optimized

✅ Reserve generation sufficient

✅ Renewable generation stable

✅ Grid inertia maintained

✅ Voltage profile within permissible limits

✅ Inter-regional transfer secure

✅ AI recommends no preventive shutdown

""")

with right:

    st.metric(
        "🎯 Prediction Accuracy",
        "99.82%"
    )

    st.metric(
        "⚡ Optimization Score",
        "98.94%"
    )

    st.metric(
        "🛰 AI Decisions",
        random.randint(8500,12000)
    )

st.divider()
# ============================================================
# 🏆 NATIONAL GRID PERFORMANCE SCORECARD
# ============================================================

st.header("🏆 NATIONAL GRID PERFORMANCE SCORECARD")

score = round(
(
(st.session_state.health * 0.45)
+
((st.session_state.frequency / 50) * 100 * 0.25)
+
((st.session_state.voltage / 400) * 100 * 0.30)
),
2
)

grade = "A+"

if score < 98:
    grade = "A"

if score < 94:
    grade = "B+"

if score < 90:
    grade = "B"

if score < 85:
    grade = "C"

a,b,c = st.columns(3)

with a:

    st.metric(
        "🏅 National Score",
        f"{score}%"
    )

with b:

    st.metric(
        "⭐ Performance Grade",
        grade
    )

with c:

    st.metric(
        "🧠 AI Reliability",
        "99.93%"
    )

st.divider()

# ============================================================
# 🌦 WEATHER IMPACT MONITOR
# ============================================================

st.header("🌦 WEATHER IMPACT MONITOR")

weather = pd.DataFrame({

    "Region":[
        "North",
        "South",
        "East",
        "West",
        "North-East"
    ],

    "Weather":[
        "Clear",
        "Cloudy",
        "Rain",
        "Sunny",
        "Thunderstorm"
    ],

    "Risk":[
        "Low",
        "Low",
        "Medium",
        "Low",
        "High"
    ]

})

st.dataframe(
    weather,
    hide_index=True,
    use_container_width=True
)

st.divider()

# ============================================================
# ⚠ BLACKOUT PROBABILITY
# ============================================================

st.header("⚠ NATIONAL BLACKOUT RISK")

risk = max(
1,
round((100 - st.session_state.health) / 4,1)
)

st.metric(
    "🚨 Cascading Blackout Probability",
    f"{risk}%"
)

st.progress(
    min(risk/100,1.0)
)

if risk < 5:

    st.success(
        "🟢 National Grid is operating with very low blackout risk."
    )

elif risk < 15:

    st.warning(
        "🟡 Grid remains stable but continuous monitoring is advised."
    )

else:

    st.error(
        "🔴 Elevated system risk detected."
    )

st.divider()

# ============================================================
# 🏅 BEST PERFORMING STATES
# ============================================================

st.header("🏅 TOP PERFORMING STATES")

leaderboard = pd.DataFrame({

    "Rank":[1,2,3,4,5],

    "State":[
        "Tamil Nadu",
        "Karnataka",
        "Gujarat",
        "Maharashtra",
        "Kerala"
    ],

    "Score":[
        99.2,
        98.9,
        98.6,
        98.2,
        97.8
    ]

})

st.dataframe(
    leaderboard,
    hide_index=True,
    use_container_width=True
)

st.divider()

# ============================================================
# 📄 AI EXECUTIVE SUMMARY
# ============================================================

st.header("📄 AI EXECUTIVE SUMMARY")

summary = f"""
GRIDSHIELD NATIONAL ANALYTICS REPORT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Grid Status :
{st.session_state.grid_status}

Generation :
{st.session_state.generation} GW

Demand :
{st.session_state.demand} GW

Grid Health :
{st.session_state.health}%

Frequency :
{st.session_state.frequency} Hz

Voltage :
{st.session_state.voltage} kV

Active Fault :
{st.session_state.fault}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI ASSESSMENT

• National grid operating within acceptable limits.

• Reserve capacity is continuously monitored.

• Renewable contribution remains stable.

• No abnormal nationwide oscillation detected.

• Predictive AI recommends continued monitoring.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Generated by GRIDSHIELD AI Analytics Engine
"""

st.code(summary, language="text")

st.download_button(
    "📥 Download Executive Summary",
    summary,
    file_name="GRIDSHIELD_Executive_Summary.txt",
    mime="text/plain"
)

st.divider()

# ============================================================
# 🚀 SYSTEM STATUS
# ============================================================

st.success("""
🇮🇳 GRIDSHIELD NATIONAL ANALYTICS CENTER ONLINE

✅ AI Analytics Engine Active

✅ Predictive Intelligence Running

✅ National Grid Monitoring Enabled

✅ Executive Reporting Available

✅ Decision Support System Operational
""")

st.caption(
"GRIDSHIELD V2.0 | National Analytics & Intelligence Platform | Developed by AKASH V"
)