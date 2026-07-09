
import streamlit as st
import time

from utils.grid_engine import (
    generate_ai_action,
    initialize,
    next_mission_step,
    reset_grid,
    transformer_failure,
    transmission_failure,
    generator_failure,
    lightning,
    fire,
    overload,
    cyber_attack,
    solar_failure,
    wind_failure,
    flood_damage,
    earthquake_damage,
    voltage_collapse,
    frequency_instability,
    battery_failure,
    smart_meter_attack
)


initialize()


st.set_page_config(
    page_title="GRIDSHIELD Fault Simulator",
    page_icon="🚨",
    layout="wide"
)


st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}


.title{
    font-size:42px;
    font-weight:900;
    text-align:center;
}


.subtitle{
    text-align:center;
    font-size:18px;
}


.card{

    padding:20px;
    border-radius:15px;
    border:1px solid #444;
    background:#111;

}


.status{

    padding:18px;
    border-radius:15px;
    text-align:center;
    font-size:22px;
    font-weight:bold;

}

</style>
""",
unsafe_allow_html=True)


st.divider()
st.markdown(
"""
<div class="title">
⚠️GRIDSHIELD NATIONAL
<div class="title">
FAULT SIMULATOR⚠️ 

</div>

<div class="subtitle">

AI Powered Power Grid Emergency Testing & Response Platform

</div>

""",
unsafe_allow_html=True
)


st.write("")


status = st.session_state.grid_status



if "STABLE" in status:

    status_color = "🟢"

elif "WARNING" in status:

    status_color = "🟡"

else:

    status_color = "🔴"



st.markdown(
f"""

<div class="status">

{status_color}
GRID STATUS {status}
<br>

🕒 {time.strftime("%d-%m-%Y | %H:%M:%S")}

</div>

""",
unsafe_allow_html=True
)



st.divider()



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
        "❤️ Grid Health",
        f"{st.session_state.health}%"
    )


with f:

    st.metric(
        "🚨 Fault",
        st.session_state.fault
    )


st.divider()
# pages/fault_simulator.py

import streamlit as st
import time

from utils.grid_engine import (
    initialize,
    reset_grid,transformer_failure ,
    transmission_failure,
    generator_failure,
    lightning,
    fire,
    overload,
    cyber_attack,
    solar_failure,
    wind_failure,
    flood_damage,
    earthquake_damage,
    voltage_collapse,
    frequency_instability,
    battery_failure,
    smart_meter_attack
)


initialize()


st.set_page_config(
    page_title="GRIDSHIELD Fault Simulator",
    page_icon="🚨",
    layout="wide"
)


st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}


.title{
    font-size:50px;
    font-weight:1300;
    font-weight:bold;
    text-align:center;
    
}


.subtitle{
    text-align:center;
    font-size:18px;
}


.card{

    padding:18px;
    border-radius:15px;
    border:1px solid #444;
    background:#111;

}


.status{

    padding:18px;
    border-radius:15px;
    text-align:center;
    font-size:22px;
    font-weight:bold;

}

</style>
""",
unsafe_allow_html=True)


st.header("🚨NATIONAL FAULT SIMULATION CENTER🚨")

st.info(
"""
⚡ Select an emergency scenario below.
GRIDSHIELD AI will automatically analyse,
dispatch response teams and update SCADA systems.
"""
)


col1,col2,col3,col4 = st.columns(4)


with col1:

    st.subheader("⚡Affect Transmission")


    if st.button(
        "⚡ Transformer Failure",
        use_container_width=True
    ):

        transformer_failure()

        st.session_state.fault = "Transformer Failure"

        st.rerun()



    if st.button(
        "🔌 Line Failure",
        use_container_width=True
    ):

        transmission_failure()

        st.session_state.fault = "Transmission Line Failure"

        st.rerun()



with col2:

    st.subheader("🏭 Affect Equipments")


    if st.button(
        "🏭 Generator Failure",
        use_container_width=True
    ):

        generator_failure()

        st.session_state.fault = "Generator Failure"

        st.rerun()



    if st.button(
        "💥 Turbine Failure",
        use_container_width=True
    ):

        generator_failure()

        st.session_state.fault = "Steam Turbine Failure"

        st.rerun()



with col3:

    st.subheader("🏢 Affect Substation")


    if st.button(
        "🔥 Substation Fire",
        use_container_width=True
    ):

        fire()

        st.session_state.fault = "Substation Fire"

        st.rerun()



    if st.button(
        "⚙ Busbar Failure",
        use_container_width=True
    ):

        fire()

        st.session_state.fault = "Busbar Failure"

        st.rerun()



with col4:

    st.subheader("🌩 Natural Events")


    if st.button(
        "🌩 Lightning Strike",
        use_container_width=True
    ):

        lightning()

        st.session_state.fault = "Lightning Strike"

        st.rerun()



    if st.button(
        "📈 Grid Overload",
        use_container_width=True
    ):

        overload()

        st.session_state.fault = "Grid Overload"

        st.rerun()
st.divider()
st.header("📍 LIVE INCIDENT COMMAND PANEL 📍")


fault = st.session_state.fault



if fault == "None":

    st.success(
        """
        🟢 NO ACTIVE INCIDENT
        
        National Grid monitoring systems are operating normally.
        AI surveillance network is active.
        """
    )


else:


    left,right = st.columns([2,1])



    with left:


        st.error(
            f"""
            🚨 ACTIVE INCIDENT DETECTED
            
            {fault}
            """
        )


        st.write(
            f"""
            🏷 Fault Category  
            {st.session_state.fault_category}


            ⚙ Equipment Affected  
            {st.session_state.equipment}


            📍 Incident Location  
            {st.session_state.mission_location}


            ⏳ Estimated Restoration  
            {st.session_state.restoration_time}
            """
        )



        st.markdown("---")


        st.subheader(
            "🧠 AI Diagnostic Report"
        )


        st.info(
            f"""
            AI Confidence :

            {st.session_state.ai_confidence}%


            Fault Classification :

            {st.session_state.fault_category}


            Recommended Action :

            Isolate affected equipment,
            activate backup routes,
            dispatch specialized response team,
            restore grid synchronization.
            """
        )




    with right:


        st.subheader(
            "🚑 Emergency Response"
        )


        st.metric(
            "👷 Response Team",
            st.session_state.mission_team
        )


        st.metric(
            "🚒 Vehicle",
            st.session_state.mission_vehicle
        )


        st.metric(
            "⏱ ETA",
            st.session_state.mission_eta
        )


        st.metric(
            "🚨 Priority",
            st.session_state.mission_priority
        )



st.divider()



st.subheader(
    "📊 Grid Intelligence Parameters"
)



g1,g2,g3,g4 = st.columns(4)



with g1:

    st.metric(
        "🧠 AI Accuracy",
        f"{st.session_state.ai_confidence}%"
    )


with g2:

    st.metric(
        "👥 Consumers Impacted",
        f"{st.session_state.people_affected:,}"
    )


with g3:

    st.metric(
        "⚡ Energy Loss",
        f"{st.session_state.energy_loss} MWh"
    )


with g4:

    st.metric(
        "💰 Repair Estimate",
        f"₹{st.session_state.repair_cost} Cr"
    )


st.divider()
st.header("🛰 LIVE SCADA GRID MONITORING")


fault = st.session_state.fault



left,right = st.columns([1.5,1])



with left:


    st.subheader(
        "⚡ National Power Flow Map"
    )



    if fault == "None":


        st.code(
"""
🟢 POWER GENERATION

        │

        ▼

🟢 STEP-UP TRANSFORMER

        │

        ▼

══════════════════════

🟢 765 kV TRANSMISSION

══════════════════════

        │

        ▼

🟢 REGIONAL SUBSTATION

        │

        ▼

🟢 DISTRIBUTION NETWORK

        │

        ▼

🏠 🏥 🏭 CONSUMERS


SYSTEM CONDITION :

NORMAL OPERATION
"""
        )



    else:


        st.code(
f"""
🟢 POWER GENERATION

        │

        ▼

⚠️ GRID DISTURBANCE DETECTED

        │

        ▼

🔴 {st.session_state.equipment}

        │

═══════ ❌ ═══════

POWER FLOW INTERRUPTION

═══════ ❌ ═══════

        │

        ▼

🟡 AUTOMATIC BACKUP ROUTE ENABLED

        │

        ▼

🏥 CRITICAL LOAD PRIORITIZATION

        │

        ▼

🚑 RESPONSE TEAM DEPLOYED


FAULT :

{fault}


LOCATION :

{st.session_state.mission_location}
"""
        )




with right:


    st.subheader(
        "📡 SCADA Live Parameters"
    )



    health = st.session_state.health



    if health >= 95:

        condition = "🟢 STABLE"


    elif health >= 85:

        condition = "🟡 DEGRADED"


    else:

        condition = "🔴 CRITICAL"



    st.metric(
        "Grid Condition",
        condition
    )



    st.metric(
        "⚡ Frequency",
        f"{st.session_state.frequency} Hz"
    )


    st.metric(
        "🔌 Voltage",
        f"{st.session_state.voltage} kV"
    )


    st.metric(
        "❤️ System Health",
        f"{health}%"
    )


    st.metric(
        "⚡ Generation",
        f"{st.session_state.generation} GW"
    )


    st.metric(
        "🔋 Demand",
        f"{st.session_state.demand} GW"
    )



st.divider()



st.subheader(
    "🌐 Power Stability Analysis"
)



p1,p2,p3 = st.columns(3)



with p1:


    if st.session_state.frequency >= 49.8:

        st.success(
            "📡 Frequency Synchronization Normal"
        )

    else:

        st.error(
            "📡 Frequency Instability Detected"
        )



with p2:


    if st.session_state.voltage >= 380:

        st.success(
            "🔌 Voltage Profile Healthy"
        )

    else:

        st.warning(
            "⚠️ Voltage Deviation Detected"
        )



with p3:


    if st.session_state.health >= 90:

        st.success(
            "🟢 Grid Resilience Strong"
        )

    else:

        st.error(
            "🔴 Grid Resilience Low"
        )



st.divider()
st.header("🤖 NATIONAL AI COMMAND CENTER")


fault = st.session_state.fault



if fault == "None":


    risk_level = "🟢 LOW"

    confidence = 99.9

    response = (
        "Continue continuous AI monitoring"
    )

    protocol = (
        "Normal Grid Protection Protocol"
    )

    dispatch = (
        "No emergency deployment required"
    )



else:


    confidence = st.session_state.ai_confidence



    if confidence >= 98:


        risk_level = "🔴 CRITICAL"


    elif confidence >= 90:


        risk_level = "🟠 HIGH"


    else:


        risk_level = "🟡 MEDIUM"



    response = {

        "Transformer Failure":
        "Isolate transformer and transfer load through backup feeder.",


        "Transmission Line Failure":
        "Activate alternate transmission corridor and inspect damaged line.",


        "Generator Failure":
        "Increase reserve generation and synchronize standby units.",


        "Cyber Security Attack":
        "Switch SCADA network to protected emergency mode.",


        "Solar Farm Failure":
        "Balance renewable loss using regional generation reserve.",


        "Wind Farm Failure":
        "Redistribute renewable power flow.",


        "Flood Substation Damage":
        "Disconnect flooded equipment and activate disaster response.",


        "Voltage Collapse":
        "Start voltage recovery and reactive power support.",


        "Frequency Instability":
        "Activate frequency regulation controllers."

    }.get(

        fault,

        "Deploy engineering team and perform grid stabilization."

    )



    protocol = (

        f"{st.session_state.mission_priority} "
        "Emergency Response Protocol"

    )


    dispatch = (

        f"{st.session_state.mission_team} "
        "with "
        f"{st.session_state.mission_vehicle}"

    )




a,b,c,d = st.columns(4)



with a:

    st.metric(

        "🎯 AI Confidence",

        f"{confidence}%"

    )



with b:

    st.metric(

        "🚨 Threat Level",

        risk_level

    )



with c:

    st.metric(

        "⚡ Response ETA",

        st.session_state.mission_eta
        if fault!="None"
        else "0 Minutes"

    )



with d:

    st.metric(

        "🧠 Priority",

        st.session_state.mission_priority
        if fault!="None"
        else "NORMAL"

    )



st.markdown("---")



left,right = st.columns([2,1])



with left:


    st.subheader(
        "🧠 AI Decision Report"
    )


    if fault=="None":


        st.success(
"""
SYSTEM ANALYSIS

✅ No abnormal behaviour detected

✅ Frequency within safe range

✅ Voltage stable

✅ Generation-demand balance maintained

✅ Protection systems active

AI monitoring continues 24×7
"""
        )



    else:


        st.error(

f"""
INCIDENT INTELLIGENCE REPORT


Detected Fault :

{fault}


Equipment :

{st.session_state.equipment}


Location :

{st.session_state.mission_location}


AI Diagnosis :

{st.session_state.fault_category}


Recommended Action :

{response}


Confidence :

{confidence}%

"""
        )




with right:


    st.subheader(
        "🚑 AI Dispatch Strategy"
    )


    st.info(

f"""
COMMAND :

{protocol}


TEAM :

{dispatch}


RESTORATION WINDOW :

{st.session_state.restoration_time}


STATUS :

AUTONOMOUS RESPONSE ACTIVE
"""
    )



st.divider()



st.subheader(
    "🔮 AI Prediction Engine"
)



x1,x2,x3 = st.columns(3)



with x1:

    if fault=="None":

        st.success(
            "Future Risk : Minimal"
        )

    else:

        st.warning(
            "Future Risk : Under Observation"
        )



with x2:

    st.info(
        "Backup Network : Available"
    )



with x3:

    st.info(
        "AI Model : GRIDSHIELD Neural Engine"
    )



st.divider()
st.header("🚑 NATIONAL EMERGENCY DISPATCH CENTER")


st.subheader(
    "📡 Live Response Mission"
)



mission = st.session_state.mission_status



if mission == "STANDBY":


    st.success(
        "🟢 No emergency missions active"
    )


else:


    st.warning(
        f"🚨 ACTIVE MISSION : {mission}"
    )



st.markdown("---")



d1,d2,d3,d4 = st.columns(4)



with d1:

    st.metric(

        "👷 Response Team",

        st.session_state.mission_team
        if st.session_state.mission_team
        else "Standby"

    )



with d2:

    st.metric(

        "🚒 Vehicle",

        st.session_state.mission_vehicle
        if st.session_state.mission_vehicle
        else "Available"

    )



with d3:

    st.metric(

        "📍 Location",

        st.session_state.mission_location
        if st.session_state.mission_location
        else "National Grid"

    )



with d4:

    st.metric(

        "⏱ ETA",

        st.session_state.mission_eta
        if st.session_state.mission_eta
        else "N/A"

    )



st.divider()



st.subheader(
    "🛰 Mission Progress Tracking"
)



progress = st.session_state.mission_progress



st.progress(
    progress / 100
)



p1,p2 = st.columns([2,1])



with p1:


    if progress == 0:


        st.info(
            "Waiting for emergency dispatch..."
        )


    elif progress == 20:


        st.warning(
"""
🚨 Dispatch Order Issued

Emergency team preparing equipment.
"""
        )


    elif progress == 40:


        st.warning(
"""
🚚 Response Team En Route

Vehicle tracking activated.
"""
        )


    elif progress == 60:


        st.info(
"""
📍 Team Reached Location

Initial inspection started.
"""
        )


    elif progress == 75:


        st.warning(
"""
🔧 Repair Operation Running

Equipment restoration underway.
"""
        )


    elif progress == 90:


        st.warning(
"""
⚡ Grid Synchronization Started

Power restoration sequence active.
"""
        )


    elif progress == 100:


        st.success(
"""
🟢 Mission Completed

Grid successfully restored.
"""
        )





with p2:


    st.subheader(
        "🎮 Mission Control"
    )


    if st.button(
        "▶ Advance Mission Step",
        use_container_width=True
    ):


        next_mission_step()

        st.rerun()



    if st.button(
        "🔄 Reset Mission",
        use_container_width=True
    ):


        reset_grid()

        st.rerun()




st.divider()



st.subheader(
    "📜 Command Communication Log"
)



if (
    "mission_logs"
    in st.session_state
    and len(st.session_state.mission_logs)>0
):


    for log in st.session_state.mission_logs[:10]:


        st.write(
            "📡",
            log
        )



else:


    st.info(
        "No command activity recorded."
    )



st.divider()



st.subheader(
    "🌐 Multi Agency Coordination"
)



agency1,agency2,agency3,agency4 = st.columns(4)



with agency1:

    st.success(
"""
⚡ Power Engineers

READY
"""
    )


with agency2:

    st.success(
"""
🚒 Fire Response

READY
"""
    )


with agency3:

    st.success(
"""
🚁 Drone Surveillance

READY
"""
    )


with agency4:

    st.success(
"""
🏥 Medical Support

READY
"""
    )



st.divider()
st.header("📊 ADVANCED SCADA ANALYTICS CENTER")


st.subheader(
    "🛰 Real-Time Grid Performance Analysis"
)



a1,a2,a3,a4 = st.columns(4)



with a1:

    st.metric(

        "⚡ Current Generation",

        f"{st.session_state.generation} GW"

    )


with a2:

    st.metric(

        "🔋 Current Demand",

        f"{st.session_state.demand} GW"

    )


with a3:

    st.metric(

        "📡 Frequency",

        f"{st.session_state.frequency} Hz"

    )


with a4:

    st.metric(

        "🔌 Voltage",

        f"{st.session_state.voltage} kV"

    )



st.divider()



st.subheader(
    "🟢 National Grid Health Monitoring"
)



health = st.session_state.health



if health >= 95:

    health_status = "🟢 EXCELLENT"

elif health >= 85:

    health_status = "🟡 STABLE WITH WARNING"

else:

    health_status = "🔴 CRITICAL CONDITION"



h1,h2 = st.columns([2,1])



with h1:


    st.progress(
        health / 100
    )



with h2:


    st.metric(

        "Grid Health Status",

        f"{health}% {health_status}"

    )



st.divider()



st.subheader(
    "📈 SCADA Parameter Trend Simulation"
)



import pandas as pd



if "scada_history" not in st.session_state:


    st.session_state.scada_history = []



scada_record = {

    "Time":
    time.strftime("%H:%M:%S"),


    "Generation":
    st.session_state.generation,


    "Demand":
    st.session_state.demand,


    "Frequency":
    st.session_state.frequency,


    "Voltage":
    st.session_state.voltage,


    "Health":
    st.session_state.health

}



st.session_state.scada_history.append(
    scada_record
)



if len(st.session_state.scada_history)>20:

    st.session_state.scada_history.pop(0)



scada_df = pd.DataFrame(
    st.session_state.scada_history
)



st.line_chart(

    scada_df.set_index("Time")

)



st.divider()



st.subheader(
    "⚡ Power Balance Analysis"
)



balance = (
    st.session_state.generation
    -
    st.session_state.demand
)



b1,b2,b3 = st.columns(3)



with b1:


    st.metric(

        "Power Balance",

        f"{round(balance,2)} GW"

    )



with b2:


    if balance >=0:

        st.success(
            "🟢 Supply Available"
        )

    else:

        st.error(
            "🔴 Power Deficit"
        )



with b3:


    reserve = round(
        max(balance,0),
        2
    )


    st.metric(

        "Reserve Capacity",

        f"{reserve} GW"

    )



st.divider()



st.subheader(
    "🤖 AI Grid Prediction Engine"
)



if st.session_state.fault_active:


    prediction = [

        "⚠ Abnormal grid behaviour detected",

        "🔍 AI analysing equipment condition",

        "🚑 Emergency response recommended",

        "⚡ Backup supply prioritised"

    ]


else:


    prediction = [

        "🟢 Grid parameters normal",

        "📡 No abnormal pattern detected",

        "🤖 AI monitoring active",

        "⚡ Future stability predicted"

    ]



for item in prediction:

    st.write(item)



st.divider()



st.subheader(
    "🌍 Environmental Impact Monitoring"
)



e1,e2,e3 = st.columns(3)



carbon = (
    st.session_state.energy_loss * 112
)



with e1:

    st.metric(

        "🌱 Carbon Impact",

        f"{round(carbon,2)} tCO₂"

    )



with e2:

    st.metric(

        "⚡ Energy Loss",

        f"{st.session_state.energy_loss} MWh"

    )



with e3:

    st.metric(

        "💰 Potential Savings",

        f"₹{st.session_state.money_saved} Cr"

    )



st.divider()
st.header("📄 NATIONAL GRID INCIDENT REPORT GENERATOR")


st.subheader(
    "📝 AI Generated Emergency Report"
)



fault = st.session_state.fault



if fault == "None":


    st.success(
        """
🟢 SYSTEM STATUS

No active incidents detected.

GRIDSHIELD AI monitoring system
is continuously analysing national
power infrastructure.
"""
    )



else:


    report_time = time.strftime(
        "%d-%m-%Y %H:%M:%S"
    )


    report = f"""

🇮🇳 GRIDSHIELD NATIONAL POWER GRID

EMERGENCY INCIDENT REPORT


Report Generated:
{report_time}


━━━━━━━━━━━━━━━━━━━━━━


INCIDENT DETAILS


Fault:
{st.session_state.fault}


Location:
{st.session_state.mission_location}


Equipment:
{st.session_state.equipment}


Grid Status:
{st.session_state.grid_status}


━━━━━━━━━━━━━━━━━━━━━━


AI ANALYSIS


AI Confidence:
{st.session_state.ai_confidence}%


Fault Category:
{st.session_state.fault_category}


Recommended Action:

{generate_ai_action()}


━━━━━━━━━━━━━━━━━━━━━━


IMPACT ASSESSMENT


Consumers Affected:
{st.session_state.people_affected}


Energy Loss:
{st.session_state.energy_loss} MWh


Estimated Repair Cost:
₹{st.session_state.repair_cost} Crore


Restoration ETA:
{st.session_state.restoration_time}


━━━━━━━━━━━━━━━━━━━━━━


DISPATCH INFORMATION


Team:
{st.session_state.mission_team}


Vehicle:
{st.session_state.mission_vehicle}


Priority:
{st.session_state.mission_priority}


━━━━━━━━━━━━━━━━━━━━━━


GRIDSHIELD AI COMMAND SYSTEM

Incident monitoring completed.

"""


    st.code(
        report,
        language="text"
    )



    st.download_button(

        label="⬇ Download AI Emergency Report",

        data=report,

        file_name=
        "GRIDSHIELD_AI_Incident_Report.txt",

        mime="text/plain"

    )



st.divider()



st.header(
    "📚 NATIONAL INCIDENT HISTORY"
)



if "fault_history" not in st.session_state:


    st.session_state.fault_history=[]



if st.session_state.fault != "None":


    history_record = {


        "Time":
        time.strftime("%H:%M:%S"),


        "Fault":
        st.session_state.fault,


        "Location":
        st.session_state.mission_location,


        "Status":
        st.session_state.mission_status

    }


    if history_record not in st.session_state.fault_history:


        st.session_state.fault_history.insert(
            0,
            history_record
        )




if len(st.session_state.fault_history)>0:


    history_df = pd.DataFrame(

        st.session_state.fault_history

    )


    st.dataframe(

        history_df,

        use_container_width=True,

        hide_index=True

    )


else:


    st.info(
        "No historical incidents available."
    )



st.divider()



st.header(
    "🔐 SYSTEM SECURITY STATUS"
)



s1,s2,s3,s4 = st.columns(4)



with s1:

    st.success(
        """
🔒 SCADA Security

ONLINE
"""
    )


with s2:

    st.success(
        """
🛰 Sensor Network

ACTIVE
"""
    )


with s3:

    st.success(
        """
🤖 AI Engine

RUNNING
"""
    )


with s4:

    st.success(
        """
☁ Data Backup

SYNCED
"""
    )



st.divider()



st.success(
"""
⚡ GRIDSHIELD NATIONAL INTELLIGENT POWER GRID PLATFORM ONLINE

🇮🇳 AI Powered Grid Monitoring | Emergency Response | Smart Restoration

Developed for Advanced Power Infrastructure Simulation
"""
)



st.caption(
"GRIDSHIELD V2.0 | National Smart Grid Command Platform"
)