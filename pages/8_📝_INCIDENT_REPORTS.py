import streamlit as st
import pandas as pd
import sqlite3
import uuid
from datetime import datetime



st.set_page_config(

    page_title="📄 GRIDSHIELD Incident Reports",

    page_icon="📄",

    layout="wide"

)



# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================


DB_NAME = "GRIDSHIELD_INCIDENTS.db"



def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute("""

    CREATE TABLE IF NOT EXISTS incidents(

        Incident_ID TEXT PRIMARY KEY,

        Time TEXT,

        Fault TEXT,

        Category TEXT,

        Location TEXT,

        Equipment TEXT,

        Status TEXT,

        Grid_Status TEXT,

        Health INTEGER,

        Consumers INTEGER,

        AI_Confidence REAL,

        Response_Team TEXT,

        ETA TEXT,

        Priority TEXT,

        Resolution_Time TEXT,

        Resolution_Remark TEXT

    )

    """)


    conn.commit()

    conn.close()



create_database()



# ==========================================================
# SESSION DEFAULT VALUES
# ==========================================================


defaults = {


"fault":"None",

"grid_status":"🟢 STABLE",

"health":100,

"fault_category":"Normal",

"equipment":"None",

"mission_location":"National Grid",

"mission_team":"Standby",

"mission_eta":"0 Minutes",

"mission_priority":"LOW",

"people_affected":0,

"ai_confidence":99.9,

"incident_status":"ACTIVE"


}



for key,value in defaults.items():

    if key not in st.session_state:

        st.session_state[key]=value



# ==========================================================
# INCIDENT ID GENERATOR
# ==========================================================


def generate_incident_id():


    return (

        "GS-"

        +

        datetime.now().strftime("%Y%m%d")

        +

        "-"

        +

        str(uuid.uuid4())[:5].upper()

    )
# ==========================================================
# SAVE INCIDENT INTO DATABASE
# ==========================================================


def save_incident():


    if st.session_state.fault != "None":


        incident_id = generate_incident_id()



        conn = sqlite3.connect(DB_NAME)

        cursor = conn.cursor()



        cursor.execute("""

        INSERT OR IGNORE INTO incidents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

        """,

        (

            incident_id,


            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),


            st.session_state.fault,


            st.session_state.fault_category,


            st.session_state.mission_location,


            st.session_state.equipment,


            st.session_state.incident_status,


            st.session_state.grid_status,


            st.session_state.health,


            st.session_state.people_affected,


            st.session_state.ai_confidence,


            st.session_state.mission_team,


            st.session_state.mission_eta,


            st.session_state.mission_priority,


            "Pending",


            "Awaiting restoration"

        ))



        conn.commit()

        conn.close()





# ==========================================================
# LOAD INCIDENT HISTORY
# ==========================================================


def load_incidents():


    conn = sqlite3.connect(DB_NAME)


    df = pd.read_sql(

        "SELECT * FROM incidents ORDER BY Time DESC",

        conn

    )


    conn.close()


    return df





save_incident()



# ==========================================================
# HEADER
# ==========================================================

st.markdown(

"""
<h1 style="text-align:center;color:#00E5FF;"> 
📄 INCIDENT REPORT CENTER 📄

</h1>


<h3 style="text-align:center;color:#AAAAAA;">

AI Powered Grid Fault Documentation System

</h3>


""",

unsafe_allow_html=True

)



st.divider()
# ==========================================================
# 🚨 CURRENT INCIDENT STATUS
# ==========================================================


st.header(
    "🚨 Current Incident Status"
)



if st.session_state.fault == "None":


    st.success(
"""
🟢 NATIONAL GRID NORMAL

No active incidents detected.

AI monitoring system is running continuously.
"""
    )



else:


    c1,c2,c3,c4 = st.columns(4)



    with c1:

        st.metric(

            "🚨 Fault",

            st.session_state.fault

        )


    with c2:

        st.metric(

            "📍 Location",

            st.session_state.mission_location

        )


    with c3:

        st.metric(

            "⚡ Grid Health",

            f"{st.session_state.health}%"

        )


    with c4:

        st.metric(

            "📌 Status",

            st.session_state.incident_status

        )



st.divider()



# ==========================================================
# 📚 INCIDENT HISTORY DATABASE
# ==========================================================


st.header(
    "📚 National Incident History Database"
)



incident_df = load_incidents()



if len(incident_df) > 0:



    st.subheader(
        "🔎 Incident Filter"
    )



    filter_status = st.selectbox(

        "Select Status",

        [

            "ALL",

            "ACTIVE",

            "SOLVED"

        ]

    )



    if filter_status != "ALL":


        incident_df = incident_df[

            incident_df["Status"] == filter_status

        ]



    st.dataframe(

        incident_df,

        use_container_width=True,

        hide_index=True

    )



else:


    st.info(
        "📭 No incident records available."
    )



st.divider()
# ==========================================================
# 📥 INCIDENT DATABASE EXPORT
# ==========================================================


st.header(
    "📥 Incident Database Export"
)



export_df = load_incidents()



if len(export_df) > 0:



    csv_data = export_df.to_csv(

        index=False

    ).encode("utf-8")



    st.download_button(

        label="📊 Download Complete Incident CSV",

        data=csv_data,

        file_name="GRIDSHIELD_Incident_Database.csv",

        mime="text/csv",

        use_container_width=True

    )



else:


    st.warning(
        "⚠ No incident records available."
    )



st.divider()



# ==========================================================
# ✅ INCIDENT RESOLUTION CONTROL CENTER
# ==========================================================


st.header(
    "✅ Incident Resolution Control Center"
)



active_df = load_incidents()



if len(active_df) > 0:



    active_df = active_df[

        active_df["Status"] == "ACTIVE"

    ]



    if len(active_df) > 0:



        st.warning(

            f"🚨 {len(active_df)} Active Incident(s) Need Resolution"

        )



        for index,row in active_df.iterrows():



            with st.container():



                st.info(

f"""

### 🚨 {row['Incident_ID']}


⚡ Fault :

{row['Fault']}


📍 Location :

{row['Location']}


⚙ Equipment :

{row['Equipment']}


👷 Response Team :

{row['Response_Team']}


⏱ ETA :

{row['ETA']}


📌 Status :

{row['Status']}

"""

                )





                if st.button(

                    f"✅ Mark {row['Incident_ID']} SOLVED",

                    key=f"solve_{index}"

                ):



                    conn = sqlite3.connect(DB_NAME)

                    cursor = conn.cursor()



                    cursor.execute(

                    """

                    UPDATE incidents

                    SET Status=?,

                    Resolution_Time=?,

                    Resolution_Remark=?

                    WHERE Incident_ID=?

                    """,

                    (

                    "SOLVED",

                    datetime.now().strftime(

                        "%d-%m-%Y %H:%M:%S"

                    ),

                    "Grid restored successfully. Normal operation resumed.",

                    row["Incident_ID"]

                    ))



                    conn.commit()

                    conn.close()



                    st.success(

                        "✅ Incident Successfully Resolved"

                    )


                    st.rerun()



    else:


        st.success(

            "🟢 All incidents solved. National Grid Stable."

        )



else:


    st.info(

        "📭 No incidents available."

    )



st.divider()



# ==========================================================
# SYSTEM STATUS
# ==========================================================


st.success(
"""
⚡ GRIDSHIELD INCIDENT MANAGEMENT SYSTEM ONLINE

AI Monitoring              ✅

Incident Logging           ✅

Fault History Database     ✅

ACTIVE / SOLVED Tracking   ✅

CSV Export                 ✅

National Command Records Active 🇮🇳
"""
)