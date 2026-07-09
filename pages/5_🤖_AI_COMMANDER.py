

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.grid_engine import initialize
from data.ai_database import AI_DATABASE

initialize()

st.set_page_config(
    page_title="🤖 AI COMMAND CENTER 🤖",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖GRIDSHIELD'S AI COMMAND CENTER🤖")
st.subheader("National Artificial Intelligence Decision & Prediction Engine")

st.success("🟢 AI Core Online | SCADA Connected | Prediction Engine Active")

st.divider()

# ==========================================================
# AI SYSTEM STATUS
# ==========================================================

st.header("🧠 NATIONAL AI STATUS")

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    st.metric(
        "AI Engine",
        "ONLINE"
    )

with c2:
    st.metric(
        "SCADA",
        "CONNECTED"
    )

with c3:
    st.metric(
        "Grid Nodes",
        "36"
    )

with c4:
    st.metric(
        "Prediction",
        "ACTIVE"
    )

with c5:
    st.metric(
        "AI Accuracy",
        "99.84%"
    )

with c6:
    st.metric(
        "Cyber Shield",
        "SECURE"
    )

st.divider()

# ==========================================================
# NO ACTIVE FAULT
# ==========================================================

if not st.session_state.fault_active:

    left, right = st.columns([2,1])

    with left:

        st.success("🟢 NATIONAL GRID OPERATING NORMALLY")

        st.info("""
The GRIDSHIELD AI continuously monitors

• Power Generation

• Power Demand

• Frequency Stability

• Voltage Stability

• Transformer Health

• Substation Status

• SCADA Telemetry

• Relay Operations

• Renewable Integration

• Transmission Corridors

• Weather Conditions

• Load Forecast

• Equipment Health

• Cyber Security Events

• Cascading Failure Prediction

• National Grid Stability
""")

    with right:

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=99.82,

            title={"text":"AI Confidence"},

            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"green"},
                "steps":[
                    {"range":[0,60],"color":"red"},
                    {"range":[60,85],"color":"orange"},
                    {"range":[85,100],"color":"green"}
                ]
            }

        ))

        fig.update_layout(height=330)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    st.header("📈 NATIONAL AI OVERVIEW")

    x1,x2,x3,x4 = st.columns(4)

    with x1:
        st.metric(
            "Grid Stability",
            "99.3%"
        )

    with x2:
        st.metric(
            "Prediction Accuracy",
            "98.91%"
        )

    with x3:
        st.metric(
            "Healthy States",
            "36"
        )

    with x4:
        st.metric(
            "Emergency States",
            "0"
        )

    st.divider()

    chart = pd.DataFrame({

        "Parameter":[

            "Generation",
            "Demand",
            "Voltage",
            "Frequency",
            "Grid Health"

        ],

        "Score":[

            97,
            95,
            98,
            99,
            99

        ]

    })

    fig = px.bar(

        chart,

        x="Parameter",

        y="Score",

        color="Score",

        text="Score",

        color_continuous_scale="Turbo"

    )

    fig.update_layout(
        height=430
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success("🤖 AI Monitoring Active Across India")

    st.stop()

# ==========================================================
# ACTIVE INCIDENT
# ==========================================================

fault = st.session_state.fault

details = AI_DATABASE.get(fault)

if details is None:

    st.error("AI DATABASE ERROR")

    st.stop()

st.error(f"🚨 ACTIVE INCIDENT : {fault}")

st.divider()
# ==========================================================
# 🚨 AI INCIDENT OVERVIEW
# ==========================================================

st.header("🚨 AI INCIDENT OVERVIEW")

a, b, c, d, e, f = st.columns(6)

with a:
    st.metric(
        "Severity",
        details["severity"]
    )

with b:
    st.metric(
        "Priority",
        details["priority"]
    )

with c:
    st.metric(
        "Consumers",
        details["affected"]
    )

with d:
    st.metric(
        "ETA",
        details["eta"]
    )

with e:
    st.metric(
        "AI Confidence",
        "99.81%"
    )

with f:
    st.metric(
        "Mission Status",
        "ACTIVE"
    )

st.divider()

# ==========================================================
# LIVE GRID PARAMETERS
# ==========================================================

st.header("⚡ LIVE NATIONAL GRID")

g1, g2, g3, g4, g5 = st.columns(5)

with g1:
    st.metric(
        "Generation",
        f"{st.session_state.generation} GW"
    )

with g2:
    st.metric(
        "Demand",
        f"{st.session_state.demand} GW"
    )

with g3:
    st.metric(
        "Frequency",
        f"{st.session_state.frequency} Hz"
    )

with g4:
    st.metric(
        "Voltage",
        f"{st.session_state.voltage} kV"
    )

with g5:
    st.metric(
        "Grid Health",
        f"{st.session_state.health}%"
    )

st.divider()

# ==========================================================
# AI CONFIDENCE GAUGE
# ==========================================================

left, right = st.columns([1,1])

with left:

    confidence = go.Figure(go.Indicator(

        mode="gauge+number",

        value=99.81,

        title={"text":"AI Confidence"},

        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"green"},
            "steps":[
                {"range":[0,60],"color":"red"},
                {"range":[60,85],"color":"orange"},
                {"range":[85,100],"color":"green"}
            ]
        }

    ))

    confidence.update_layout(height=340)

    st.plotly_chart(
        confidence,
        use_container_width=True
    )

with right:

    risk = min(
        max(
            (100 - st.session_state.health)
            + abs(st.session_state.generation - st.session_state.demand) * 5,
            5
        ),
        100
    )

    risk_fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=risk,

        title={"text":"National Risk Index"},

        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"crimson"},
            "steps":[
                {"range":[0,35],"color":"green"},
                {"range":[35,70],"color":"yellow"},
                {"range":[70,100],"color":"red"}
            ]
        }

    ))

    risk_fig.update_layout(height=340)

    st.plotly_chart(
        risk_fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# AI ROOT CAUSE
# ==========================================================

st.header("🧠 AI ROOT CAUSE ANALYSIS")

st.info(details["cause"])

st.code(f"""
SCADA Sensor Trigger
        │
        ▼
Relay Protection Activated
        │
        ▼
Voltage / Frequency Deviation
        │
        ▼
Fault Identified

➡ {fault}

        │
        ▼
AI Root Cause Analysis Completed

Confidence : 99.81%
""")

st.divider()

# ==========================================================
# AI FAULT PROBABILITY
# ==========================================================

st.header("📊 AI FAULT PROBABILITY")

probability = pd.DataFrame({

    "Fault":[
        fault,
        "Transformer Failure",
        "Transmission Failure",
        "Generator Failure",
        "Relay Failure",
        "Lightning Strike"
    ],

    "Probability":[
        99,
        87,
        78,
        64,
        31,
        12
    ]

})

fig = px.bar(

    probability,

    x="Fault",

    y="Probability",

    color="Probability",

    text="Probability",

    color_continuous_scale="Turbo"

)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()
# ==========================================================
# 🔮 AI PREDICTION & CASCADING FAILURE ENGINE
# ==========================================================

st.header("🔮 AI PREDICTION ENGINE")

left, right = st.columns([1.3,1])

with left:

    st.subheader("🧠 AI Decision Tree")

    st.code(f"""
🛰 SENSOR NETWORK
        │
        ▼
⚡ SCADA TELEMETRY
        │
        ▼
🛡 PROTECTION RELAYS
        │
        ▼
🚨 {fault.upper()}
        │
        ▼
🤖 AI ROOT CAUSE
        │
        ▼
📍 ISOLATION STRATEGY
        │
        ▼
🚑 AUTO DISPATCH
        │
        ▼
🔄 RESTORATION
""")

with right:

    st.subheader("📈 Prediction Confidence")

    confidence = pd.DataFrame({

        "Module":[

            "Fault Detection",
            "Root Cause",
            "Dispatch",
            "Restoration",
            "Recovery"

        ],

        "Confidence":[

            99.9,
            99.3,
            98.8,
            97.6,
            96.8

        ]

    })

    fig = px.bar(

        confidence,

        x="Confidence",

        y="Module",

        orientation="h",

        color="Confidence",

        text="Confidence",

        color_continuous_scale="Viridis"

    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# 🌍 CASCADING FAILURE VISUAL
# ==========================================================

st.header("🌍 CASCADING FAILURE SIMULATION")

if fault == "No Fault":

    st.success("🟢 No cascading failures predicted.")

else:

    st.error(f"""

🚨 ACTIVE EVENT

{fault}

        │

        ▼

⚡ Voltage Instability

        │

        ▼

🔌 Transmission Overload

        │

        ▼

🏭 Generation Reduction

        │

        ▼

🏥 Essential Loads Shifted

        │

        ▼

🚨 POSSIBLE CASCADE TO ADJACENT STATES

""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Current State",
        details["location"]
    )

with col2:
    st.metric(
        "Risk Radius",
        "185 km"
    )

with col3:
    st.metric(
        "Neighbour States",
        "3"
    )

with col4:
    st.metric(
        "Spread Probability",
        "81%"
    )

st.divider()

# ==========================================================
# 📊 AI IMPACT VISUAL
# ==========================================================

st.header("📊 NATIONAL IMPACT")

impact = pd.DataFrame({

    "Category":[

        "Power Loss",
        "Economic",
        "Consumers",
        "Equipment",
        "Environment"

    ],

    "Impact":[

        92,
        81,
        74,
        67,
        58

    ]

})

fig = px.treemap(

    impact,

    path=["Category"],

    values="Impact",

    color="Impact",

    color_continuous_scale="Turbo"

)

fig.update_layout(height=520)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# 👥 POPULATION IMPACT
# ==========================================================

st.header("👥 CONSUMER IMPACT")

x1,x2,x3,x4,x5 = st.columns(5)

with x1:
    st.metric(
        "People",
        "3,42,000"
    )

with x2:
    st.metric(
        "Hospitals",
        "24"
    )

with x3:
    st.metric(
        "Industries",
        "69"
    )

with x4:
    st.metric(
        "Railway Stations",
        "18"
    )

with x5:
    st.metric(
        "Airports",
        "2"
    )

pie = pd.DataFrame({

    "Sector":[

        "Residential",
        "Industrial",
        "Commercial",
        "Hospitals",
        "Transport"

    ],

    "Share":[

        42,
        28,
        15,
        8,
        7

    ]

})

fig = px.pie(

    pie,

    values="Share",

    names="Sector",

    hole=0.55,

    color_discrete_sequence=px.colors.qualitative.Bold

)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# 🚦 LIVE AI STATUS BOARD
# ==========================================================

st.header("🚦 LIVE AI STATUS BOARD")

status = pd.DataFrame({

    "System":[

        "SCADA",
        "Telemetry",
        "Relay Network",
        "Transformer AI",
        "Drone Feed",
        "Dispatch",
        "Weather AI",
        "Cyber Security",
        "Satellite Link",
        "Backup Grid"

    ],

    "Status":[

        "🟢 ONLINE",
        "🟢 ONLINE",
        "🟢 ONLINE",
        "🟡 WARNING",
        "🟢 READY",
        "🟢 READY",
        "🟢 ACTIVE",
        "🟢 SECURE",
        "🟢 ACTIVE",
        "🟢 AVAILABLE"

    ]

})

st.dataframe(
    status,
    use_container_width=True,
    hide_index=True
)

st.divider()
# ==========================================================
# 💰 NATIONAL ECONOMIC IMPACT CENTER
# ==========================================================

st.header("💰 NATIONAL ECONOMIC IMPACT")

money = getattr(st.session_state, "money_loss", 0)
energy = getattr(st.session_state, "energy_loss", 0)
people = getattr(st.session_state, "people_affected", 0)

delay15 = round(money * 1.35, 1)
delay30 = round(money * 1.80, 1)
delay60 = round(money * 2.75, 1)

a,b,c,d = st.columns(4)

with a:
    st.metric(
        "💸 Current Loss",
        f"₹ {money} Cr"
    )

with b:
    st.metric(
        "⏳ +15 Min",
        f"₹ {delay15} Cr"
    )

with c:
    st.metric(
        "⌛ +30 Min",
        f"₹ {delay30} Cr"
    )

with d:
    st.metric(
        "🚨 +1 Hour",
        f"₹ {delay60} Cr"
    )

loss = pd.DataFrame({

    "Time":[
        "Current",
        "15 Min",
        "30 Min",
        "60 Min"
    ],

    "Loss":[
        money,
        delay15,
        delay30,
        delay60
    ]

})

fig = px.line(

    loss,

    x="Time",

    y="Loss",

    markers=True,

    color_discrete_sequence=["red"]

)

fig.update_layout(height=420)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# ⚡ NATIONAL RESTORATION STATUS
# ==========================================================

st.header("⚡ AI RESTORATION ENGINE")

restore = pd.DataFrame({

    "Stage":[

        "Detection",
        "Isolation",
        "Diagnosis",
        "Dispatch",
        "Repair",
        "Testing",
        "Synchronization",
        "Grid Restore"

    ],

    "Progress":[

        100,
        100,
        100,
        92,
        71,
        46,
        18,
        5

    ]

})

fig = px.bar(

    restore,

    x="Stage",

    y="Progress",

    text="Progress",

    color="Progress",

    color_continuous_scale="Turbo"

)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

for _, row in restore.iterrows():

    st.write(f"**{row['Stage']}**")

    st.progress(row["Progress"]/100)

st.divider()

# ==========================================================
# 🌦 WEATHER INTELLIGENCE
# ==========================================================

st.header("🌦 AI WEATHER INTELLIGENCE")

weather = pd.DataFrame({

    "Parameter":[

        "Temperature",
        "Humidity",
        "Wind",
        "Rain",
        "Lightning",
        "Cyclone"

    ],

    "Value":[

        34,
        61,
        24,
        42,
        63,
        8

    ]

})

fig = px.bar_polar(

    weather,

    r="Value",

    theta="Parameter",

    color="Value",

    color_continuous_scale="Turbo"

)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info(f"""

🌡 Temperature : 34°C

💧 Humidity : 61%

🌧 Rain Probability : 42%

⚡ Lightning Risk : 63%

🌪 Cyclone Risk : LOW

🛰 Weather Impact on {fault}

Moderate

""")

st.divider()

# ==========================================================
# 🚁 AI DISPATCH CENTER
# ==========================================================

st.header("🚁 NATIONAL DISPATCH STATUS")

dispatch = pd.DataFrame({

    "Unit":[

        "Engineers",
        "Fire Unit",
        "Drone",
        "Ambulance",
        "Police",
        "Spare Transformer",
        "Repair Vehicle",
        "Control Officer"

    ],

    "Status":[

        "🟢 DEPLOYED",
        "🟢 READY",
        "🟢 AIRBORNE",
        "🟢 READY",
        "🟢 ALERT",
        "🟡 MOVING",
        "🟢 MOVING",
        "🟢 ACTIVE"

    ]

})

st.dataframe(

    dispatch,

    use_container_width=True,

    hide_index=True

)

st.divider()

# ==========================================================
# 📈 NATIONAL DECISION REPORT
# ==========================================================

st.header("📜 EXECUTIVE AI DECISION")

st.success(f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 GRIDSHIELD AI COMMAND REPORT

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Incident

{fault}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Location

{details['location']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Severity

{details['severity']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Priority

{details['priority']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Consumers

{details['affected']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Estimated Restoration

{details['eta']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI Confidence

99.81%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mission

READY FOR NATIONAL DISPATCH

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recommended Action

{details['recommendation'][0]}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

""")

st.divider()

st.success("🤖 GRIDSHIELD NATIONAL AI COMMAND CENTER ONLINE")

st.caption(
    "⚡ GRIDSHIELD AI ENGINE V2.0 | Developed by AKASH.V – Inspiring Greatness"
)