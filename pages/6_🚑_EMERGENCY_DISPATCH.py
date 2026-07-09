

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

from utils.grid_engine import (
    initialize,
    next_mission_step,
    reset_grid
)

from data.ai_database import AI_DATABASE

# ==========================================================
# INITIALIZE GRIDSHIELD
# ==========================================================

initialize()

st.set_page_config(
    page_title="🚑 GRIDSHIELD Emergency Dispatch",
    page_icon="🚑",
    layout="wide"
)

# ==========================================================
# SAFE SESSION VARIABLES
# ==========================================================

defaults = {

    "mission_progress":0,
    "fault_active":False,
    "dispatch_status":"STANDBY",
    "repair_stage":"Waiting",
    "crew_status":"Idle",
    "vehicle_status":"Available",
    "drone_status":"Ready",
    "mission_log":[]
}

for key,value in defaults.items():

    if key not in st.session_state:

        st.session_state[key]=value

# ==========================================================
# HEADER
# ==========================================================

st.title("🚑 GRIDSHIELD'S NATIONAL EMERGENCY DISPATCH CENTER 🚨")
st.subheader("National Intelligent Emergency Response & Restoration System")

st.success("🛰 Dispatch Server Online | GPS Connected | AI Synchronization Active")

st.divider()

# ==========================================================
# NO ACTIVE INCIDENT
# ==========================================================

if not st.session_state.fault_active:

    left,right = st.columns([2,1])

    with left:

        st.success("🟢 NATIONAL GRID SAFE")

        st.info("""
No active emergency detected.

All emergency response units remain on standby.

The dispatch engine is continuously monitoring:

• National Load Dispatch Centres

• Regional Teams

• Emergency Vehicles

• Drone Fleet

• Fire Units

• Medical Units

• SCADA Events

• AI Predictions
""")

    with right:

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=100,

            title={"text":"Dispatch Readiness"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"green"}

            }

        ))

        fig.update_layout(height=330)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    ready = pd.DataFrame({

        "Unit":[

            "Engineers",
            "Emergency Vehicles",
            "Drone Fleet",
            "Fire Team",
            "Medical Team",
            "Police Escort"

        ],

        "Status":[

            "🟢 READY",
            "🟢 READY",
            "🟢 READY",
            "🟢 READY",
            "🟢 READY",
            "🟢 READY"

        ]

    })

    st.dataframe(

        ready,

        use_container_width=True,

        hide_index=True

    )

    st.stop()

# ==========================================================
# ACTIVE INCIDENT
# ==========================================================

fault = st.session_state.fault

details = AI_DATABASE[fault]

st.error(f"🚨 ACTIVE INCIDENT : {fault}")

st.divider()
# ==========================================================
# 🚨 NATIONAL DISPATCH COMMAND DASHBOARD
# ==========================================================

st.header("🚨 NATIONAL DISPATCH COMMAND DASHBOARD 🚨")

m1, m2, m3, m4, m5, m6 = st.columns(6)

with m1:
    st.metric(
        "🚨 Severity",
        details["severity"]
    )

with m2:
    st.metric(
        "📍 Location",
        details["location"]
    )

with m3:
    st.metric(
        "👥 Consumers",
        details["affected"]
    )

with m4:
    st.metric(
        "⏱ ETA",
        details["eta"]
    )

with m5:
    st.metric(
        "🎯 Priority",
        details["priority"]
    )

with m6:
    st.metric(
        "🤖 AI",
        "READY"
    )

st.divider()

# ==========================================================
# 🚑 LIVE RESPONSE RESOURCES
# ==========================================================

st.header("🚑 LIVE RESPONSE RESOURCES")

resources = pd.DataFrame({

    "Resource":[

        "👷 Engineers",
        "🚑 Emergency Vehicles",
        "🚒 Fire Units",
        "🚁 Drones",
        "🚓 Police Escort",
        "🏥 Medical Team",
        "⚡ Spare Transformer",
        "🔌 Cable Repair Unit"

    ],

    "Available":[

        48,
        16,
        8,
        12,
        14,
        9,
        6,
        10

    ],

    "Assigned":[

        18,
        5,
        2,
        3,
        2,
        1,
        1,
        2

    ],

    "Status":[

        "🟢 ACTIVE",
        "🟢 MOVING",
        "🟢 READY",
        "🛰 AIRBORNE",
        "🟢 READY",
        "🟢 READY",
        "🟡 RESERVED",
        "🟢 READY"

    ]

})

st.dataframe(
    resources,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# 📊 LIVE RESOURCE UTILIZATION
# ==========================================================

st.header("📊 RESOURCE UTILIZATION")

fig = px.bar(

    resources,

    x="Resource",

    y="Assigned",

    color="Assigned",

    text="Assigned",

    color_continuous_scale="Turbo"

)

fig.update_layout(
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# 🛰 GPS MISSION STATUS
# ==========================================================

st.header("🛰 LIVE GPS TRACKING")

left, right = st.columns([2,1])

with left:

    st.code(f"""

🏢 NATIONAL COMMAND CENTER
            │
            ▼
🚑 RESPONSE TEAM DISPATCHED
            │
═══════════════════════════════════════
🛰 GPS TRACKING ACTIVE
═══════════════════════════════════════
            │
            ▼
📍 INCIDENT LOCATION

{details['location']}

            │
            ▼
🔧 REPAIR TEAM
            │
            ▼
⚡ GRID RESTORATION

""")

with right:

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=96,

        title={"text":"Mission Readiness"},

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"green"},

            "steps":[

                {"range":[0,40],"color":"red"},

                {"range":[40,75],"color":"orange"},

                {"range":[75,100],"color":"green"}

            ]

        }

    ))

    fig.update_layout(height=340)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# 🚦 NATIONAL COMMAND STATUS
# ==========================================================

st.header("🚦 COMMAND STATUS")

status = pd.DataFrame({

    "System":[

        "AI Commander",
        "SCADA",
        "Satellite",
        "Drone Feed",
        "GPS",
        "Fire Unit",
        "Medical",
        "Police",
        "Repair Crew",
        "Power Backup"

    ],

    "Status":[

        "🟢 ONLINE",
        "🟢 ONLINE",
        "🟢 CONNECTED",
        "🛰 LIVE",
        "📍 TRACKING",
        "🚒 READY",
        "🏥 READY",
        "🚓 READY",
        "👷 DEPLOYED",
        "⚡ ACTIVE"

    ]

})

st.dataframe(
    status,
    use_container_width=True,
    hide_index=True
)

st.divider()
# ==========================================================
# 🚚 LIVE MISSION COMMAND CENTER
# ==========================================================

st.header("🚚 LIVE MISSION COMMAND CENTER")

progress = st.session_state.mission_progress

# ==========================================================
# MISSION STATUS ENGINE
# ==========================================================

if progress == 0:

    stage = "🟡 Awaiting Dispatch"

elif progress == 10:

    stage = "📞 Dispatch Order Issued"

elif progress == 20:

    stage = "🚑 Team Mobilized"

elif progress == 30:

    stage = "🚁 Drone Surveillance Started"

elif progress == 40:

    stage = "🚚 Emergency Vehicles En Route"

elif progress == 50:

    stage = "📡 GPS Tracking Active"

elif progress == 60:

    stage = "📍 Team Reached Incident"

elif progress == 70:

    stage = "⚠ Area Secured"

elif progress == 80:

    stage = "🛠 Repair Work Started"

elif progress == 90:

    stage = "⚡ Grid Synchronization"

else:

    stage = "🟢 Mission Completed"

# ==========================================================
# LIVE STATUS
# ==========================================================

left, right = st.columns([2,1])

with left:

    st.subheader("🚨 Current Mission")

    st.info(stage)

    st.progress(progress / 100)

with right:

    st.metric(
        "Mission Progress",
        f"{progress}%"
    )

    st.metric(
        "Estimated Arrival",
        details["eta"]
    )

st.divider()

# ==========================================================
# LIVE MISSION TIMELINE
# ==========================================================

st.header("📜 LIVE OPERATION TIMELINE")

timeline = [

    (0,  "📞 Emergency Call Received"),
    (10, "🤖 AI Mission Generated"),
    (20, "🚑 Team Dispatched"),
    (30, "🚁 Drone Surveillance Started"),
    (40, "🚚 Vehicles Travelling"),
    (50, "📡 GPS Live Tracking"),
    (60, "📍 Crew Reached Location"),
    (70, "⚠ Site Safety Verification"),
    (80, "🔧 Equipment Repair"),
    (90, "⚡ Grid Synchronization"),
    (100,"🟢 National Grid Restored")

]

for value, text in timeline:

    if progress >= value:

        st.success(f"✅ {text}")

    else:

        st.info(f"⏳ {text}")

st.divider()

# ==========================================================
# 🚁 LIVE RESPONSE VISUAL
# ==========================================================

st.header("🚁 LIVE RESPONSE MOVEMENT")

if progress < 20:

    st.code("""
🏢 NATIONAL COMMAND
        │
        ▼
📞 DISPATCH ORDER
""")

elif progress < 40:

    st.code("""
🏢 COMMAND
        │
        ▼
🚑══════►
        │
🚁══════►
""")

elif progress < 60:

    st.code("""
🏢 COMMAND
        │
        ▼
🚑════════════►
🚁════════════►
📡 GPS ACTIVE
""")

elif progress < 80:

    st.code("""
🏢 COMMAND
        │
        ▼
📍 INCIDENT
👷👷👷
🚒🚑
⚠ SAFETY CHECK
""")

elif progress < 100:

    st.code("""
📍 INCIDENT

🔧 Repair Crew

⚡ Transformer

🛠 Cable Repair

🔌 Testing

⚡ Synchronizing...
""")

else:

    st.code("""
🟢 GRID RESTORED

⚡ Power Stable

🏥 Hospitals Restored

🏠 Consumers Online

🏭 Industries Online

🇮🇳 NATIONAL GRID NORMAL
""")

st.divider()

# ==========================================================
# 🎮 CONTROL PANEL
# ==========================================================

st.header("🎮 OPERATOR CONTROL PANEL")

c1, c2 = st.columns(2)

with c1:

    if progress < 100:

        if st.button(
            "▶ EXECUTE NEXT MISSION",
            use_container_width=True
        ):

            next_mission_step()

            st.rerun()

with c2:

    if progress == 100:

        if st.button(
            "🟢 COMPLETE RESTORATION",
            use_container_width=True
        ):

            reset_grid()

            st.balloons()

            st.success(
                "National Grid Successfully Restored."
            )

            st.rerun()

st.divider()
# ==========================================================
# 👷 LIVE CREW OPERATIONS CENTER
# ==========================================================

st.header("👷 LIVE CREW OPERATIONS CENTER")

progress = st.session_state.mission_progress

# ==========================================================
# CREW STATUS
# ==========================================================

if progress == 0:

    crew = "🟡 Waiting at Base"
    drone = "🛰 Ready"
    fire = "🟢 Standby"
    ambulance = "🟢 Standby"

elif progress <= 20:

    crew = "🚑 Mobilizing"
    drone = "🚁 Drone Launching"
    fire = "🚒 Moving"
    ambulance = "🚑 Moving"

elif progress <= 40:

    crew = "🚚 Travelling"
    drone = "🛰 Live Surveillance"
    fire = "🚒 En Route"
    ambulance = "🚑 Following"

elif progress <= 60:

    crew = "📍 Reached Incident"
    drone = "📡 Thermal Scan"
    fire = "🔥 Site Protection"
    ambulance = "🏥 Medical Ready"

elif progress <= 80:

    crew = "🔧 Repairing Grid"
    drone = "📷 Damage Inspection"
    fire = "🚒 Fire Monitoring"
    ambulance = "🏥 Emergency Support"

elif progress < 100:

    crew = "⚡ Grid Synchronization"
    drone = "📡 Final Inspection"
    fire = "🟢 Standby"
    ambulance = "🟢 Standby"

else:

    crew = "✅ Mission Completed"
    drone = "🛬 Returned"
    fire = "🏠 Returned"
    ambulance = "🏠 Returned"

# ==========================================================
# LIVE STATUS CARDS
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success(f"👷 Crew\n\n{crew}")

with c2:
    st.info(f"🚁 Drone\n\n{drone}")

with c3:
    st.warning(f"🚒 Fire Unit\n\n{fire}")

with c4:
    st.success(f"🚑 Medical\n\n{ambulance}")

st.divider()

# ==========================================================
# TEAM DEPLOYMENT
# ==========================================================

st.header("🚑 TEAM DEPLOYMENT")

deployment = pd.DataFrame({

    "Unit":[
        "Electrical Engineers",
        "Transmission Team",
        "Substation Team",
        "Fire Department",
        "Medical Team",
        "Drone Operators",
        "Police Escort",
        "Control Officers"
    ],

    "Personnel":[
        12,
        8,
        6,
        4,
        5,
        3,
        6,
        4
    ],

    "Status":[
        crew,
        crew,
        crew,
        fire,
        ambulance,
        drone,
        "🚓 Active",
        "🖥 Monitoring"
    ]

})

st.dataframe(
    deployment,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# 🚁 LIVE MISSION VISUAL
# ==========================================================

st.header("🚁 LIVE RESPONSE ANIMATION")

if progress < 20:

    st.code("""

🏢 COMMAND CENTER

        │

        ▼

🚑 Preparing...

👷 Waiting...

🛰 Drone Ready

""")

elif progress < 40:

    st.code("""

🏢 COMMAND

        │

🚑══════════►

🚒══════════►

🚁══════════►

📡 GPS ACTIVE

""")

elif progress < 60:

    st.code("""

🚑════════════════════►

🚒════════════════════►

🚁════════════════════►

📍 INCIDENT DETECTED

""")

elif progress < 80:

    st.code("""

📍 INCIDENT

👷👷👷👷

🔧 Transformer Repair

🚁 Live Camera

🚒 Protection Active

""")

elif progress < 100:

    st.code("""

⚡ RESTORATION

🔧 Grid Repair

⚙ Equipment Testing

🔌 Synchronizing

███████████░░░

""")

else:

    st.code("""

🇮🇳 NATIONAL GRID

██████████████

🟢 POWER RESTORED

🏠 Homes Online

🏥 Hospitals Online

🏭 Industries Online

🚁 Mission Complete

""")

st.divider()

# ==========================================================
# 📋 LIVE COMMAND LOG
# ==========================================================

st.header("📋 LIVE COMMAND LOG")

logs = []

if progress >= 0:
    logs.append("📞 Emergency received by National Control Center")

if progress >= 10:
    logs.append("🤖 AI Commander generated restoration strategy")

if progress >= 20:
    logs.append("🚑 Emergency response teams dispatched")

if progress >= 30:
    logs.append("🚁 Drone surveillance initiated")

if progress >= 40:
    logs.append("📡 GPS tracking enabled")

if progress >= 60:
    logs.append("📍 Incident site reached")

if progress >= 70:
    logs.append("⚠ Safety inspection completed")

if progress >= 80:
    logs.append("🔧 Grid repair in progress")

if progress >= 90:
    logs.append("⚡ Grid synchronization started")

if progress >= 100:
    logs.append("✅ National Grid fully restored")

for log in logs:
    st.success(log)

st.divider()
# ==========================================================
# 🗺️ NATIONAL INCIDENT & RESTORATION COMMAND MAP
# ==========================================================

st.header("🗺️ NATIONAL INCIDENT COMMAND MAP")

left, right = st.columns([2, 1])

with left:

    st.code(f"""

                           🇮🇳 INDIA

               Punjab        Haryana

                    🟢           🟢

      Rajasthan 🟢      Delhi 🟢

 Gujarat 🟢                         Uttar Pradesh 🟢

 Maharashtra 🟢                 Bihar 🟢

 Telangana 🟢      Chhattisgarh 🟢

 Karnataka 🟢      Odisha 🟢

 Kerala 🟢       Andhra Pradesh 🟢

                🔴 INCIDENT

           📍 {details['location']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚑 Response Team → Moving

🚁 Drone → Live

📡 GPS → Connected

🤖 AI → Monitoring

""")

with right:

    st.metric(
        "📍 Incident",
        details["location"]
    )

    st.metric(
        "🎯 Priority",
        details["priority"]
    )

    st.metric(
        "🚨 Severity",
        details["severity"]
    )

    st.metric(
        "🤖 AI Confidence",
        "99.92%"
    )

st.divider()

# ==========================================================
# 💰 RESTORATION COST MONITOR
# ==========================================================

st.header("💰 RESTORATION COST")

repair_cost = getattr(
    st.session_state,
    "repair_cost",
    48.75
)

energy_loss = getattr(
    st.session_state,
    "energy_loss",
    135.4
)

population = getattr(
    st.session_state,
    "people_affected",
    details["affected"]
)

a, b, c, d = st.columns(4)

with a:
    st.metric(
        "💸 Repair Cost",
        f"₹ {repair_cost:.2f} Cr"
    )

with b:
    st.metric(
        "⚡ Energy Loss",
        f"{energy_loss:.1f} MWh"
    )

with c:
    st.metric(
        "👥 Consumers",
        population
    )

with d:
    st.metric(
        "🏭 Industries",
        128
    )

st.divider()

# ==========================================================
# 📊 COST BREAKDOWN
# ==========================================================

st.header("📊 REPAIR COST BREAKDOWN")

cost_df = pd.DataFrame({

    "Component":[

        "Transmission",

        "Transformer",

        "Manpower",

        "Emergency Fleet",

        "Fuel",

        "Equipment"

    ],

    "Cost":[

        12,

        16,

        5,

        4,

        3,

        9

    ]

})

fig = px.pie(

    cost_df,

    names="Component",

    values="Cost",

    hole=0.45,

    color_discrete_sequence=px.colors.qualitative.Bold

)

fig.update_layout(height=480)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# ⚡ RESTORATION COUNTERS
# ==========================================================

st.header("⚡ LIVE RESTORATION STATUS")

restore = min(progress, 100)

homes = int(restore * 2500)
industries = int(restore * 18)
hospitals = min(int(restore / 5), 20)
substations = min(int(restore / 10), 10)

x1, x2, x3, x4 = st.columns(4)

with x1:
    st.metric(
        "🏠 Homes Restored",
        f"{homes:,}"
    )

with x2:
    st.metric(
        "🏭 Industries",
        industries
    )

with x3:
    st.metric(
        "🏥 Hospitals",
        hospitals
    )

with x4:
    st.metric(
        "⚡ Substations",
        substations
    )

st.divider()

# ==========================================================
# ⏱ RESTORATION COUNTDOWN
# ==========================================================

st.header("⏱ ESTIMATED RESTORATION")

remaining = max(0, 100 - progress)

st.progress(progress / 100)

st.info(
    f"Remaining Mission Progress : {remaining}%"
)

timeline = pd.DataFrame({

    "Phase":[

        "Detection",

        "Dispatch",

        "Travel",

        "Inspection",

        "Repair",

        "Testing",

        "Synchronization",

        "Completed"

    ],

    "Progress":[

        min(progress, 10),

        min(max(progress-10,0),10),

        min(max(progress-20,0),20),

        min(max(progress-40,0),20),

        min(max(progress-60,0),20),

        min(max(progress-80,0),10),

        min(max(progress-90,0),10),

        100 if progress==100 else 0

    ]

})

fig = px.bar(

    timeline,

    x="Phase",

    y="Progress",

    text="Progress",

    color="Progress",

    color_continuous_scale="Turbo"

)

fig.update_layout(height=420)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# 🎯 FINAL MISSION SUMMARY
# ==========================================================

st.header("🎯 MISSION SUMMARY")

if progress < 100:

    st.warning(f"""

Mission Status : ACTIVE

Incident : {fault}

Location : {details['location']}

Priority : {details['priority']}

Current Stage : {stage}

AI Monitoring : ACTIVE

Dispatch Center : ONLINE

""")

else:

    st.success(f"""

✅ NATIONAL GRID RESTORED

Incident : {fault}

Location : {details['location']}

Mission Result : SUCCESS

Consumers Restored : {population}

AI Verification : PASSED

Mission Closed Successfully

""")

st.divider()

st.success("🚑 GRIDSHIELD NATIONAL EMERGENCY DISPATCH CENTER ONLINE")

st.caption(
    "⚡ GRIDSHIELD Emergency Dispatch V2.0 | Developed by AKASH.V"
)