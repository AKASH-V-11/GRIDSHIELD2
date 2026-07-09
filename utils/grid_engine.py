# ==========================================================
# GRIDSHIELD ADVANCED GRID CONTROL ENGINE
# PART 1/6
# ==========================================================

import streamlit as st
import pandas as pd
from datetime import datetime
import uuid


# ==========================================================
# INITIALIZE GLOBAL GRID MEMORY
# ==========================================================

def initialize():


    defaults = {


        # ==============================
        # NATIONAL GRID STATUS
        # ==============================


        "grid_status":
        "🟢 NATIONAL GRID STABLE",


        "fault":
        "None",


        "fault_active":
        False,



        # ==============================
        # LIVE GRID PARAMETERS
        # ==============================


        "generation":
        42.8,


        "demand":
        41.9,


        "frequency":
        50.00,


        "voltage":
        400,


        "health":
        99.8,



        # ==============================
        # INCIDENT MEMORY
        # ==============================


        "incidents":
        [],



        # ==============================
        # ACTIVE FAULT INTELLIGENCE
        # ==============================


        "fault_category":
        "",


        "equipment":
        "",


        "fault_image":
        "",


        "fault_coordinates":
        "",


        "affected_regions":
        [],



        # ==============================
        # AI INTELLIGENCE
        # ==============================


        "ai_confidence":
        0,


        "ai_prediction":
        "",


        "system_alert":
        "",



        # ==============================
        # IMPACT ANALYSIS
        # ==============================


        "people_affected":
        0,


        "energy_loss":
        0,


        "repair_cost":
        0,


        "money_saved":
        0,


        "restoration_time":
        "",



        # ==============================
        # EMERGENCY DISPATCH
        # ==============================


        "mission_status":
        "STANDBY",


        "mission_progress":
        0,


        "mission_team":
        "",


        "mission_vehicle":
        "",


        "mission_location":
        "",


        "mission_eta":
        "",


        "mission_priority":
        "",



        # ==============================
        # CONTROL ROOM LOGS
        # ==============================


        "mission_logs":
        []

    }



    for key,value in defaults.items():


        if key not in st.session_state:


            st.session_state[key] = value



# ==========================================================
# TIME LOGGER
# ==========================================================


def current_time():


    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )



# ==========================================================
# MISSION LOG SYSTEM
# ==========================================================


def add_log(message):


    if "mission_logs" not in st.session_state:

        st.session_state.mission_logs = []


    st.session_state.mission_logs.insert(

        0,

        f"{current_time()} | {message}"

    )
    # Incident creation


def create_incident(data):

    incident = {

        "Incident ID":
        "INC-" + str(uuid.uuid4())[:8].upper(),

        "Time":
        current_time(),

        **data,

        "Status":
        "ACTIVE"

    }


    st.session_state.incidents.insert(
        0,
        incident
    )


    return incident



# Emergency dispatch start


def start_dispatch(
    team,
    vehicle,
    location,
    eta,
    priority
):

    st.session_state.mission_status = (
        "🚑 DISPATCH ORDER ISSUED"
    )

    st.session_state.mission_progress = 20

    st.session_state.mission_team = team

    st.session_state.mission_vehicle = vehicle

    st.session_state.mission_location = location

    st.session_state.mission_eta = eta

    st.session_state.mission_priority = priority


    add_log(
        "Emergency response team dispatched"
    )



# Mission progression


def next_mission_step():


    progress = st.session_state.mission_progress



    if progress == 20:


        st.session_state.mission_progress = 40


        st.session_state.mission_status = (
            "🚚 RESPONSE TEAM MOVING"
        )


        add_log(
            "Emergency vehicle started movement"
        )



    elif progress == 40:


        st.session_state.mission_progress = 60


        st.session_state.mission_status = (
            "📍 TEAM ARRIVED AT INCIDENT LOCATION"
        )


        add_log(
            "Response team reached affected location"
        )



    elif progress == 60:


        st.session_state.mission_progress = 75


        st.session_state.mission_status = (
            "🔍 AI DAMAGE INSPECTION RUNNING"
        )


        add_log(
            "AI inspection started"
        )



    elif progress == 75:


        st.session_state.mission_progress = 90


        st.session_state.mission_status = (
            "🔧 GRID REPAIR OPERATION ACTIVE"
        )


        add_log(
            "Repair operation started"
        )



    elif progress == 90:


        st.session_state.mission_progress = 100


        st.session_state.mission_status = (
            "⚡ GRID RESTORATION COMPLETED"
        )


        complete_restoration()



# Close active incident


def close_current_incident():


    for incident in st.session_state.incidents:


        if incident["Status"] == "ACTIVE":


            incident["Status"] = "RESOLVED"


            incident["Resolution Time"] = current_time()


            break



# Grid restoration


def restore_grid():


    st.session_state.grid_status = (
        "🟢 NATIONAL GRID STABLE"
    )


    st.session_state.fault_active = False


    st.session_state.generation = 42.8

    st.session_state.demand = 41.9

    st.session_state.frequency = 50.00

    st.session_state.voltage = 400

    st.session_state.health = 99.8


    st.session_state.money_saved = (
        st.session_state.repair_cost * 3
    )


    add_log(
        "Grid parameters normalized"
    )



# Complete restoration process


def complete_restoration():


    close_current_incident()


    add_log(
        "AI verified grid stability"
    )


    add_log(
        "Incident resolved successfully"
    )


    restore_grid()
    # Fault activation engine


def activate_fault(

    fault,
    category,
    state,
    equipment,
    severity,
    consumers,

    generation,
    demand,
    frequency,
    voltage,
    health,

    confidence,
    repair_cost,
    energy_loss,

    eta,
    team,
    vehicle,
    priority,

    coordinates="",
    regions=None,
    prediction=""

):


    initialize()



    st.session_state.grid_status = (

        "🔴 CRITICAL GRID EVENT"

        if severity in ["HIGH", "CRITICAL"]

        else

        "🟡 GRID WARNING"

    )



    st.session_state.fault_active = True



    st.session_state.fault = fault



    st.session_state.fault_category = category



    st.session_state.equipment = equipment



    st.session_state.fault_coordinates = coordinates



    st.session_state.affected_regions = (
        regions if regions else []
    )



    st.session_state.ai_prediction = prediction



    st.session_state.system_alert = (

        f"{fault} detected at {state}"

    )



    st.session_state.generation = generation

    st.session_state.demand = demand

    st.session_state.frequency = frequency

    st.session_state.voltage = voltage

    st.session_state.health = health



    st.session_state.ai_confidence = confidence



    st.session_state.people_affected = consumers



    st.session_state.repair_cost = repair_cost



    st.session_state.energy_loss = energy_loss



    st.session_state.restoration_time = eta



    create_incident({

        "State":
        state,


        "Fault":
        fault,


        "Category":
        category,


        "Equipment":
        equipment,


        "Severity":
        severity,


        "Consumers":
        consumers,


        "AI Confidence":
        f"{confidence}%",


        "Energy Loss":
        f"{energy_loss} MWh",


        "Repair Cost":
        f"₹{repair_cost} Cr",


        "Location":
        coordinates

    })



    start_dispatch(

        team,

        vehicle,

        state,

        eta,

        priority

    )



    add_log(

        f"⚠️ {fault} detected in {state}"

    )



# Live data for dashboard


def get_grid_status():


    return {


        "status":
        st.session_state.grid_status,


        "fault":
        st.session_state.fault,


        "location":
        st.session_state.mission_location,


        "equipment":
        st.session_state.equipment,


        "health":
        st.session_state.health,


        "frequency":
        st.session_state.frequency,


        "voltage":
        st.session_state.voltage,


        "confidence":
        st.session_state.ai_confidence

    }



# AI commander feed


def get_ai_status():


    return {


        "fault":
        st.session_state.fault,


        "category":
        st.session_state.fault_category,


        "location":
        st.session_state.mission_location,


        "equipment":
        st.session_state.equipment,


        "confidence":
        st.session_state.ai_confidence,


        "impact":
        st.session_state.people_affected,


        "energy_loss":
        st.session_state.energy_loss,


        "repair_cost":
        st.session_state.repair_cost,


        "prediction":
        st.session_state.ai_prediction

    }
def transformer_failure():

     activate_fault(

        "Transformer Failure",

        "Equipment Failure",

        "Tamil Nadu",

        "765kV Power Transformer",

        "HIGH",

        1200000,

        39.2,

        41.9,

        49.62,

        360,

        90.4,

        97,

        18.5,

        850,

        "2 Hours",

        "Transformer Recovery Team",

        "Heavy Repair Unit 01",

        "CRITICAL",

        "13.0827, 80.2707",

        ["Tamil Nadu", "Puducherry"],

        "Transformer overheating pattern detected"

    )





def transmission_failure():

    activate_fault(

        "Transmission Line Failure",

        "Transmission Damage",

        "Karnataka",

        "400kV Transmission Corridor",

        "HIGH",

        850000,

        40.3,

        41.9,

        49.70,

        355,

        92.1,

        95,

        14.2,

        620,

        "3 Hours",

        "Transmission Restoration Crew",

        "Repair Vehicle 02",

        "HIGH",

        "12.9716,77.5946",

        ["Karnataka", "Andhra Pradesh"],

        "Transmission instability detected"

    )





def generator_failure():

    activate_fault(

        "Generator Failure",

        "Generation Unit Failure",

        "Maharashtra",

        "Thermal Power Generator Unit 5",

        "CRITICAL",

        2500000,

        33.8,

        41.9,

        49.35,

        350,

        87.2,

        99,

        32,

        1400,

        "4 Hours",

        "Generation Emergency Engineers",

        "Power Plant Response Vehicle",

        "CRITICAL",

        "19.0760,72.8777",

        ["Maharashtra", "Goa"],

        "Generation output anomaly detected"

    )





def lightning():

    activate_fault(

        "Lightning Strike",

        "Weather Related",

        "Kerala",

        "33kV Distribution Network",

        "MEDIUM",

        220000,

        42.3,

        41.8,

        49.88,

        385,

        95.5,

        90,

        5.5,

        180,

        "45 Minutes",

        "Protection Team",

        "Inspection Vehicle",

        "MEDIUM",

        "8.5241,76.9366",

        ["Kerala"],

        "Weather impact detected"

    )





def fire():

    activate_fault(

        "Substation Fire",

        "Fire Emergency",

        "Delhi",

        "Urban Electrical Substation",

        "HIGH",

        640000,

        40.5,

        41.9,

        49.58,

        350,

        88.4,

        98,

        24,

        900,

        "3 Hours",

        "Electrical Fire Response Team",

        "Fire Rescue Vehicle",

        "CRITICAL",

        "28.6139,77.2090",

        ["Delhi NCR"],

        "Thermal sensor detected abnormal heat"

    )





def overload():

    activate_fault(

        "Grid Overload",

        "Demand Stress",

        "Gujarat",

        "Regional Load Center",

        "MEDIUM",

        430000,

        45.5,

        46.8,

        49.90,

        390,

        93.2,

        92,

        8,

        300,

        "30 Minutes",

        "Load Dispatch Team",

        "Monitoring Vehicle",

        "MEDIUM",

        "23.0225,72.5714",

        ["Gujarat"],

        "Demand exceeded safe operating margin"

    )
def cyber_attack():

      activate_fault(

        "Cyber Security Attack",

        "Digital Infrastructure Threat",

        "National Control Network",

        "SCADA Control System",

        "CRITICAL",

        3500000,

        36.5,

        42.2,

        49.20,

        340,

        82.5,

        99,

        45,

        1800,

        "6 Hours",

        "Cyber Security Response Unit",

        "Mobile Security Command Vehicle",

        "CRITICAL",

        "17.3850,78.4867",

        ["Multiple States"],

        "AI detected abnormal SCADA communication activity"

    )





def solar_failure():

    activate_fault(

        "Solar Farm Failure",

        "Renewable Generation Failure",

        "Rajasthan",

        "500MW Solar Power Plant",

        "HIGH",

        900000,

        37.2,

        42.0,

        49.55,

        370,

        91.5,

        94,

        16,

        700,

        "5 Hours",

        "Renewable Energy Engineers",

        "Solar Maintenance Unit",

        "HIGH",

        "26.9124,75.7873",

        ["Rajasthan"],

        "Solar generation output dropped unexpectedly"

    )





def wind_failure():

    activate_fault(

        "Wind Farm Failure",

        "Renewable Energy Failure",

        "Tamil Nadu",

        "Wind Turbine Cluster",

        "MEDIUM",

        500000,

        40.1,

        42.0,

        49.75,

        390,

        94.0,

        93,

        9,

        250,

        "2 Hours",

        "Wind Energy Maintenance Team",

        "Wind Service Vehicle",

        "MEDIUM",

        "11.1271,78.6569",

        ["Tamil Nadu"],

        "Wind turbine performance anomaly detected"

    )





def flood_damage():

    activate_fault(

        "Flood Substation Damage",

        "Natural Disaster",

        "Assam",

        "River Side Substation",

        "CRITICAL",

        1500000,

        34.2,

        42.5,

        49.10,

        330,

        80.5,

        98,

        52,

        2200,

        "12 Hours",

        "Disaster Response Electrical Team",

        "Flood Rescue Vehicle",

        "CRITICAL",

        "26.2006,92.9376",

        ["Assam", "North East Region"],

        "Water level risk detected near electrical assets"

    )





def earthquake_damage():

    activate_fault(

        "Earthquake Grid Damage",

        "Geological Disaster",

        "Uttarakhand",

        "High Voltage Transmission Towers",

        "CRITICAL",

        2200000,

        31.5,

        42.0,

        48.90,

        310,

        75.5,

        99,

        75,

        3500,

        "18 Hours",

        "National Disaster Electrical Force",

        "Heavy Repair Convoy",

        "CRITICAL",

        "30.0668,79.0193",

        ["Uttarakhand", "Himachal Region"],

        "Structural damage prediction detected"

    )





def voltage_collapse():

    activate_fault(

        "Voltage Collapse",

        "Power Stability Failure",

        "Andhra Pradesh",

        "High Voltage Network",

        "HIGH",

        1800000,

        38.0,

        44.0,

        48.70,

        280,

        78.2,

        97,

        38,

        1600,

        "7 Hours",

        "Voltage Stabilization Team",

        "Grid Support Vehicle",

        "CRITICAL",

        "16.5062,80.6480",

        ["Andhra Pradesh", "Telangana"],

        "Voltage stability margin critically reduced"

    )





def frequency_instability():

    activate_fault(

        "Frequency Instability",

        "Grid Synchronization Failure",

        "Karnataka",

        "Inter-State Grid Link",

        "HIGH",

        1200000,

        39.5,

        43.5,

        48.95,

        350,

        85.8,

        96,

        20,

        1000,

        "3 Hours",

        "Grid Frequency Control Team",

        "Synchronization Unit",

        "HIGH",

        "15.3173,75.7139",

        ["South Grid"],

        "Frequency deviation beyond safe limit"

    )





def battery_failure():

    activate_fault(

        "Energy Storage Failure",

        "Battery System Failure",

        "Gujarat",

        "Grid Scale Battery Storage",

        "MEDIUM",

        300000,

        41.0,

        42.5,

        49.82,

        395,

        93.8,

        91,

        7,

        180,

        "1 Hour",

        "Energy Storage Engineers",

        "Battery Service Unit",

        "MEDIUM",

        "23.2156,72.6369",

        ["Gujarat"],

        "Battery temperature imbalance detected"

    )





def smart_meter_attack():

    activate_fault(

        "Smart Meter Network Attack",

        "IoT Security Failure",

        "Telangana",

        "Smart Meter Communication Grid",

        "HIGH",

        700000,

        40.0,

        43.0,

        49.40,

        360,

        89.5,

        95,

        13,

        450,

        "4 Hours",

        "IoT Security Response Team",

        "Digital Recovery Vehicle",

        "HIGH",

        "17.3850,78.4867",

        ["Telangana"],

        "Unauthorized smart meter communication detected"

    )
def get_analytics_data():


     return {


        "Fault":

        st.session_state.fault,


        "Location":

        st.session_state.mission_location,


        "Equipment":

        st.session_state.equipment,


        "Category":

        st.session_state.fault_category,


        "Grid Status":

        st.session_state.grid_status,


        "Consumers":

        st.session_state.people_affected,


        "Energy Loss (MWh)":

        st.session_state.energy_loss,


        "Repair Cost (Cr)":

        st.session_state.repair_cost,


        "AI Confidence":

        st.session_state.ai_confidence,


        "Mission Status":

        st.session_state.mission_status,


        "Time":

        current_time()

    }





def get_ai_commander_data():


    return {


        "Active Fault":

        st.session_state.fault,


        "Category":

        st.session_state.fault_category,


        "Affected Equipment":

        st.session_state.equipment,


        "Location":

        st.session_state.mission_location,


        "Severity":

        st.session_state.grid_status,


        "AI Confidence":

        st.session_state.ai_confidence,


        "Consumers":

        st.session_state.people_affected,


        "Energy Loss":

        st.session_state.energy_loss,


        "Repair Cost":

        st.session_state.repair_cost,


        "AI Prediction":

        st.session_state.ai_prediction,


        "Recommended Action":

        generate_ai_action()

    }





def get_live_grid_data():


    return {


        "status":

        st.session_state.grid_status,


        "fault":

        st.session_state.fault,


        "location":

        st.session_state.mission_location,


        "equipment":

        st.session_state.equipment,


        "health":

        st.session_state.health,


        "frequency":

        st.session_state.frequency,


        "voltage":

        st.session_state.voltage,


        "generation":

        st.session_state.generation,


        "demand":

        st.session_state.demand

    }





def generate_ai_action():


    actions = {


        "Transformer Failure":

        "Isolate transformer and activate backup feeder",



        "Transmission Line Failure":

        "Reroute power through alternate transmission corridor",



        "Generator Failure":

        "Activate reserve generation capacity",



        "Substation Fire":

        "Emergency isolation and alternate supply restoration",



        "Cyber Security Attack":

        "Switch SCADA network into secure operation mode",



        "Voltage Collapse":

        "Activate voltage stabilization protocol",



        "Frequency Instability":

        "Synchronize grid frequency controllers",



        "Solar Farm Failure":

        "Enable backup renewable generation support",



        "Wind Farm Failure":

        "Inspect turbine cluster and restore output",



        "Flood Substation Damage":

        "Deploy disaster electrical restoration team"

    }



    return actions.get(

        st.session_state.fault,

        "Continue AI monitoring"

    )





def export_incident_report():


    if len(st.session_state.incidents) == 0:

        return None



    return pd.DataFrame(

        st.session_state.incidents

    )





def reset_grid():


    values = {


        "grid_status":
        "🟢 NATIONAL GRID STABLE",


        "fault":
        "None",


        "fault_active":
        False,


        "generation":
        42.8,


        "demand":
        41.9,


        "frequency":
        50.00,


        "voltage":
        400,


        "health":
        99.8,


        "fault_category":
        "",


        "equipment":
        "",


        "ai_confidence":
        0,


        "repair_cost":
        0,


        "energy_loss":
        0,


        "people_affected":
        0,


        "restoration_time":
        "",


        "mission_status":
        "STANDBY",


        "mission_progress":
        0,


        "mission_team":
        "",


        "mission_vehicle":
        "",


        "mission_location":
        "",


        "mission_eta":
        "",


        "mission_priority":
        "",


        "mission_logs":
        []

    }



    for key,value in values.items():

        st.session_state[key] = value



    add_log(

        "GRIDSHIELD system reset completed"

    )
def next_mission_step():

    progress = st.session_state.mission_progress

    if progress == 20:

        st.session_state.mission_progress = 40
        st.session_state.mission_status = "🚚 RESPONSE TEAM EN ROUTE"


    elif progress == 40:

        st.session_state.mission_progress = 60
        st.session_state.mission_status = "📍 TEAM ARRIVED AT LOCATION"


    elif progress == 60:

        st.session_state.mission_progress = 75
        st.session_state.mission_status = "🔍 DAMAGE INSPECTION RUNNING"


    elif progress == 75:

        st.session_state.mission_progress = 90
        st.session_state.mission_status = "🔧 REPAIR IN PROGRESS"


    elif progress == 90:

        st.session_state.mission_progress = 100
        st.session_state.mission_status = "⚡ GRID RESTORED SUCCESSFULLY"

def generate_ai_action():

    fault = st.session_state.fault


    actions = {

        "Transformer Failure":
        "Isolate transformer and activate backup supply",


        "Transmission Line Failure":
        "Switch power through alternate transmission corridor",


        "Generator Failure":
        "Activate reserve generation units",


        "Substation Fire":
        "Isolate substation and protect critical feeders",


        "Lightning Strike":
        "Inspect protection system and restore supply",


        "Grid Overload":
        "Balance load using demand management"

    }


    return actions.get(
        fault,
        "AI monitoring grid continuously"
    )