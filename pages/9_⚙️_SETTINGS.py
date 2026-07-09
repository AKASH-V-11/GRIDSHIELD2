
import streamlit as st

st.set_page_config(
    page_title="⚙️ GRIDSHIELD Settings",
    page_icon="⚙️",
    layout="wide"
)

# ==========================================================
# INITIALIZE SETTINGS
# ==========================================================

defaults = {

    "theme":"🌑 Dark Control Room",

    "refresh":"10 Seconds",

    "email_alerts":True,

    "desktop_alerts":True,

    "sms_alerts":False,

    "ai_threshold":90,

    "auto_dispatch":True,

    "auto_restore":True,

    "simulation_speed":"Normal",

    "maintenance":False,

    "two_factor":True,

    "session_timeout":30

}

for key,value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================================================
# PAGE STYLE
# ==========================================================

st.markdown("""

<style>

.block-container{

    padding-top:1rem;

}

.title{

    font-size:42px;

    font-weight:800;

    color:#00E5FF;

}

.subtitle{

    color:#CCCCCC;

    font-size:17px;

}

.card{

    background:#121212;

    border:1px solid #333;

    border-radius:15px;

    padding:18px;

    margin-bottom:20px;

}

</style>

""",unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================
st.divider()
st.markdown("""

<div class="title">
⚙️GRIDSHIELD SYSTEM SETTINGS⚙️

</div>

<div class="subtitle">
National Intelligent Power Grid Control Platform

</div>

""",unsafe_allow_html=True)

st.divider()

# ==========================================================
# 🖥 APPEARANCE
# ==========================================================

st.subheader("🖥 Appearance")

left,right = st.columns(2)

with left:

    theme = st.selectbox(

        "Dashboard Theme",

        [

            "🌑 Dark Control Room",

            "🔵 Blue Energy",

            "🟢 Green Grid",

            "⚫ Midnight Black"

        ],

        index=[

            "🌑 Dark Control Room",

            "🔵 Blue Energy",

            "🟢 Green Grid",

            "⚫ Midnight Black"

        ].index(st.session_state.theme)

    )

with right:

    refresh = st.selectbox(

        "Auto Refresh",

        [

            "Off",

            "5 Seconds",

            "10 Seconds",

            "30 Seconds",

            "60 Seconds"

        ],

        index=[

            "Off",

            "5 Seconds",

            "10 Seconds",

            "30 Seconds",

            "60 Seconds"

        ].index(st.session_state.refresh)

    )

st.divider()
# ==========================================================
# 🔔 NOTIFICATIONS
# ==========================================================

st.subheader("🔔 Notifications")

left, right = st.columns(2)

with left:

    email_alerts = st.toggle(
        "📧 Email Alerts",
        value=st.session_state.email_alerts
    )

    desktop_alerts = st.toggle(
        "🖥 Desktop Notifications",
        value=st.session_state.desktop_alerts
    )

with right:

    sms_alerts = st.toggle(
        "📱 SMS Alerts",
        value=st.session_state.sms_alerts
    )

    emergency_popup = st.toggle(
        "🚨 Emergency Popup Alerts",
        value=True
    )

st.divider()

# ==========================================================
# 🤖 AI AUTOMATION
# ==========================================================

st.subheader("🤖 AI Automation")

left, right = st.columns(2)

with left:

    ai_threshold = st.slider(

        "AI Confidence Threshold (%)",

        50,

        100,

        st.session_state.ai_threshold

    )

    auto_dispatch = st.toggle(

        "🚑 Automatic Team Dispatch",

        value=st.session_state.auto_dispatch

    )

with right:

    auto_restore = st.toggle(

        "⚡ Automatic Grid Restoration",

        value=st.session_state.auto_restore

    )

    predictive_ai = st.toggle(

        "🧠 Predictive Fault Detection",

        value=True

    )

st.divider()

# ==========================================================
# ⚡ SIMULATION
# ==========================================================

st.subheader("⚡ Simulation")

left, right = st.columns(2)

with left:

    simulation_speed = st.select_slider(

        "Simulation Speed",

        options=[

            "Very Slow",

            "Slow",

            "Normal",

            "Fast",

            "Ultra Fast"

        ],

        value=st.session_state.simulation_speed

    )

with right:

    maintenance = st.toggle(

        "🛠 Maintenance Mode",

        value=st.session_state.maintenance

    )

    sound = st.toggle(

        "🔊 Alarm Sound",

        value=True

    )

st.divider()
# ==========================================================
# 🔐 SECURITY
# ==========================================================

st.subheader("🔐 Security")

left, right = st.columns(2)

with left:

    two_factor = st.toggle(

        "🔑 Two-Factor Authentication",

        value=st.session_state.two_factor

    )

    login_alert = st.toggle(

        "📧 Login Alert",

        value=True

    )

with right:

    session_timeout = st.slider(

        "Session Timeout (Minutes)",

        5,

        120,

        st.session_state.session_timeout

    )

    auto_logout = st.toggle(

        "🚪 Auto Logout",

        value=False

    )

st.divider()

# ==========================================================
# 💾 SAVE SETTINGS
# ==========================================================

st.subheader("💾 Save Configuration")

save_col, reset_col = st.columns(2)

with save_col:

    if st.button(

        "💾 Save Settings",

        use_container_width=True

    ):

        st.session_state.theme = theme

        st.session_state.refresh = refresh

        st.session_state.email_alerts = email_alerts

        st.session_state.desktop_alerts = desktop_alerts

        st.session_state.sms_alerts = sms_alerts

        st.session_state.ai_threshold = ai_threshold

        st.session_state.auto_dispatch = auto_dispatch

        st.session_state.auto_restore = auto_restore

        st.session_state.simulation_speed = simulation_speed

        st.session_state.maintenance = maintenance

        st.session_state.two_factor = two_factor

        st.session_state.session_timeout = session_timeout

        st.success("✅ Settings saved successfully!")

with reset_col:

    if st.button(

        "🔄 Reset to Default",

        use_container_width=True

    ):

        st.session_state.theme = "🌑 Dark Control Room"

        st.session_state.refresh = "10 Seconds"

        st.session_state.email_alerts = True

        st.session_state.desktop_alerts = True

        st.session_state.sms_alerts = False

        st.session_state.ai_threshold = 90

        st.session_state.auto_dispatch = True

        st.session_state.auto_restore = True

        st.session_state.simulation_speed = "Normal"

        st.session_state.maintenance = False

        st.session_state.two_factor = True

        st.session_state.session_timeout = 30

        st.success("✅ Default settings restored!")

st.divider()
# ==========================================================
# 📋 CURRENT CONFIGURATION
# ==========================================================

st.subheader("📋 Current Configuration")

c1, c2 = st.columns(2)

with c1:

    st.info(f"""
🎨 Theme

{st.session_state.theme}

━━━━━━━━━━━━━━━━━━

🔄 Auto Refresh

{st.session_state.refresh}

━━━━━━━━━━━━━━━━━━

🤖 AI Threshold

{st.session_state.ai_threshold}%

━━━━━━━━━━━━━━━━━━

⚡ Simulation

{st.session_state.simulation_speed}

━━━━━━━━━━━━━━━━━━

🔐 Two-Factor Authentication

{"Enabled ✅" if st.session_state.two_factor else "Disabled ❌"}
""")

with c2:

    st.info(f"""
🚑 Auto Dispatch

{"Enabled ✅" if st.session_state.auto_dispatch else "Disabled ❌"}

━━━━━━━━━━━━━━━━━━

⚡ Auto Restoration

{"Enabled ✅" if st.session_state.auto_restore else "Disabled ❌"}

━━━━━━━━━━━━━━━━━━

📧 Email Alerts

{"Enabled ✅" if st.session_state.email_alerts else "Disabled ❌"}

━━━━━━━━━━━━━━━━━━

🖥 Desktop Alerts

{"Enabled ✅" if st.session_state.desktop_alerts else "Disabled ❌"}

━━━━━━━━━━━━━━━━━━

🛠 Maintenance Mode

{"Enabled ✅" if st.session_state.maintenance else "Disabled ❌"}
""")

st.divider()

# ==========================================================
# ℹ️ SYSTEM INFORMATION
# ==========================================================

st.subheader("ℹ️ System Information")

i1, i2, i3, i4 = st.columns(4)

with i1:

    st.metric(
        "⚙️ Version",
        "v4.0"
    )

with i2:

    st.metric(
        "🤖 AI Engine",
        "GRID AI"
    )

with i3:

    st.metric(
        "📡 SCADA",
        "ONLINE"
    )

with i4:

    st.metric(
        "🟢 System",
        "HEALTHY"
    )

st.markdown("---")

st.success("""
🟢 GRIDSHIELD Control Platform is operating normally.

All monitoring services, AI modules and command systems are available.
""")

st.divider()
# ==========================================================
# 🛰 SYSTEM STATUS
# ==========================================================

st.subheader("🛰 GRIDSHIELD System Status")

s1, s2, s3 = st.columns(3)

with s1:

    st.success("""
🟢 AI Engine

ONLINE
""")

with s2:

    st.success("""
⚡ Grid Monitoring

ACTIVE
""")

with s3:

    st.success("""
🛡 Security Layer

PROTECTED
""")

st.divider()

# ==========================================================
# 🇮🇳 PLATFORM INFORMATION
# ==========================================================

st.subheader("🇮🇳 Platform Information")

st.info("""

GRIDSHIELD is an AI-powered National Intelligent Power Grid
Monitoring & Decision Support Platform designed for
real-time grid visualization, SCADA monitoring,
fault simulation, AI-assisted emergency response,
incident reporting and smart analytics.

""")

st.divider()

# ==========================================================
# 👨‍💻 DEVELOPER INFORMATION
# ==========================================================

st.subheader("👨‍💻 Developer")

left, right = st.columns([1,2])

with left:

    st.metric(
        "Version",
        "4.0"
    )

    st.metric(
        "Platform",
        "Streamlit"
    )

with right:

    st.success("""

🇮🇳 GRIDSHIELD

National Intelligent Power Grid Command Platform

Developed by

AKASH.V

Artificial Intelligence • Smart Grid • SCADA • Analytics

""")

st.divider()

# ==========================================================
# ⏰ LIVE SYSTEM CLOCK
# ==========================================================

import time

st.subheader("⏰ System Time")

st.code(

    time.strftime("%d-%m-%Y   |   %H:%M:%S"),

    language="text"

)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.success(
"""
⚡ GRIDSHIELD SETTINGS PANEL READY

All configuration modules are loaded successfully.
"""
)

st.caption(
"GRIDSHIELD V2.0 | National Intelligent Power Grid Command Platform"
)

st.caption(
"⚡ Developed by AKASH.V - Inspiring Greatness ⚡"
)