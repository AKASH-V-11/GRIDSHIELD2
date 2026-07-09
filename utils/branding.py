import streamlit as st
from pathlib import Path


# =====================================================
# PAGE CONFIG
# =====================================================

def configure_page(title="GRIDSHIELD"):

    st.set_page_config(
        page_title=title,
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )


# =====================================================
# GLOBAL CSS
# =====================================================

def load_css():

    st.markdown("""
<style>

html,
body,
[data-testid="stAppViewContainer"]{

    background:#0B1220;
}


/* HEADER */

.grid-title{

    font-size:44px;

    font-weight:900;

    color:#00E5FF;

    letter-spacing:2px;

    text-shadow:0px 0px 18px #00E5FF;

}


.grid-sub{

    color:#C5D5E4;

    font-size:18px;

}


.grid-banner{

    background:linear-gradient(
    90deg,
    #071A2E,
    #102D48,
    #071A2E);

    padding:18px;

    border-radius:16px;

    border:1px solid #00BFFF;

    box-shadow:0px 0px 18px rgba(0,191,255,.25);

}


/* CARD */

.info-card{

    background:#101826;

    padding:20px;

    border-radius:15px;

    border:1px solid #1F3C5A;

}


/* FOOTER */

.footer{

    text-align:center;

    color:#B0BEC5;

    padding-top:20px;

    font-size:15px;

}


/* COPYRIGHT */

.copy{

    color:#FFD54F;

    font-weight:bold;

}

</style>
""",
unsafe_allow_html=True)
    # =====================================================
# LOGO
# =====================================================

def show_logo(width=110):

    logo = Path("assets/logo.png")

    if logo.exists():

        st.image(str(logo), width=width)

    else:

        st.markdown(
            "<h1 style='font-size:70px;'>⚡</h1>",
            unsafe_allow_html=True
        )


# =====================================================
# MAIN HEADER
# =====================================================

def show_header():

    left, right = st.columns([1,5])

    with left:

        show_logo()

    with right:

        st.markdown("""

<div class="grid-banner">

<div class="grid-title">

⚡ GRIDSHIELD

</div>

<div class="grid-sub">

🇮🇳 National Intelligent Power Grid Command &
Decision Support Platform

</div>

<br>

<div style="color:#7FD8FF;font-size:15px;">

🛰 AI Monitoring &nbsp;&nbsp;|
&nbsp;&nbsp;⚡ Smart Grid Intelligence &nbsp;&nbsp;|
&nbsp;&nbsp;🚨 Fault Simulation &nbsp;&nbsp;|
&nbsp;&nbsp;📊 Real-Time Analytics

</div>

</div>

""",
unsafe_allow_html=True)

    st.markdown("")


# =====================================================
# PROJECT BANNER
# =====================================================

def project_banner():

    st.info("""

🇮🇳 **GRIDSHIELD** is an intelligent national power-grid
monitoring and decision support platform developed to
simulate real-world transmission, generation, distribution,
fault detection, emergency response and AI-assisted grid
operations.

⚡ Designed for engineering demonstration, research,
learning and smart-grid innovation.

""")
# =====================================================
# DEVELOPER PROFILE
# =====================================================

def developer_card():

    st.markdown("""

<div class="info-card">

<h2 style="color:#00E5FF;">

👨‍💻 Developer Profile

</h2>

<hr>

<h3 style="color:#FFD54F;">

AKASH. V

</h3>

<h4 style="color:#8FD8FF;">

⭐ Inspiring Greatness

</h4>

<b>🎓 Academic Background</b>

<br>

Electronics & Communication Engineering (ECE)

<br><br>

<b>📍 Location</b>

<br>

Hosur, Tamil Nadu, India 🇮🇳

<br><br>

<b>💡 Areas of Interest</b>

<ul>

<li>⚡ Smart Power Systems</li>

<li>🤖 Artificial Intelligence</li>

<li>🌐 Internet of Things (IoT)</li>

<li>📊 Data Analytics</li>

<li>🛰 Embedded Systems</li>

<li>💻 Software Development</li>

</ul>

<b>🎯 Vision</b>

<br>

To engineer intelligent technologies that solve real-world
infrastructure challenges and create meaningful impact.
I believe innovation should not only improve systems but
also inspire people to dream bigger, build fearlessly and
lead with purpose.

<br><br>

<b>🚀 Mission</b>

<br>

To create impactful engineering solutions through AI,
automation and smart technologies while inspiring
millions of learners, innovators and future engineers
to believe that ordinary people can build extraordinary
things.

</div>

""", unsafe_allow_html=True)
# ==========================================================
# FOOTER
# ==========================================================

def show_footer():

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-card">

        <h3 style="color:#00E5FF;">
            ⚡ GRIDSHIELD v4.0
        </h3>

        <p>
        National Intelligent Power Grid Command &
        Decision Support Platform
        </p>

        <hr>

        <p>

        © 2026 AKASH. V — Inspiring Greatness

        <br><br>

        Designed & Developed in Hosur, Tamil Nadu, India 🇮🇳

        <br><br>

        Powering Decisions • Preventing Blackouts

        </p>

    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# COMPLETE BRANDING
# ==========================================================

def apply_branding(title="GRIDSHIELD"):

    configure_page(title)

    load_css()

    show_header()

    project_banner()

    developer_card()