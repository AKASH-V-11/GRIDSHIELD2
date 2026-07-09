import streamlit as st
import time


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="GRIDSHIELD ⚡",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================================
# SESSION STATE INITIALIZATION
# ==========================================================

DEFAULT_STATE = {

    "boot": 0,

    "logged_in": False,

    "login_screen": False,

    "dashboard_loaded": False

}


for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value
# ==========================================================
# ⚡ GRIDSHIELD ELECTRIC LOADING SCREEN
# ==========================================================


def gridshield_loading():


    st.markdown("""

    <style>


    /* MAIN BACKGROUND */

    .stApp{

        background:
        radial-gradient(circle at top,#003B5C,#000000 60%);

    }



    /* GRIDSHIELD TITLE */

    .grid-title{


        text-align:center;

        font-size:85px;

        font-weight:1000;

        letter-spacing:8px;

        color:#00E5FF;

        text-shadow:

        0 0 10px #00E5FF,

        0 0 30px #00E5FF,

        0 0 60px cyan;


        animation:pulse 1.5s infinite;

    }



    @keyframes pulse{


        0%{

        transform:scale(1);

        }


        50%{

        transform:scale(1.05);

        }


        100%{

        transform:scale(1);

        }

    }



    /* LIGHTNING EFFECT */


    .electric{


        text-align:center;

        font-size:55px;

        animation:shock 0.8s infinite;

    }



    @keyframes shock{


        0%{

        opacity:0.3;

        transform:translateX(-8px);

        }


        50%{

        opacity:1;

        transform:translateX(8px);

        }


        100%{

        opacity:0.3;

        transform:translateX(-8px);

        }


    }



    /* POWER CARD */


    .power-card{


        margin:auto;

        width:70%;

        padding:20px;

        border-radius:20px;

        border:2px solid #00E5FF;


        background:

        linear-gradient(

        135deg,

        rgba(0,40,70,0.8),

        rgba(0,0,0,0.9)

        );


        box-shadow:

        0 0 25px cyan;


        text-align:center;

        color:white;

        font-size:22px;

    }



    </style>


    """,unsafe_allow_html=True)

    government_header()

    st.markdown(
    """

    <div class="electric">
    ⚡⚡⚡
    </div>


    <div class="grid-title">
    **⚡GRIDSHIELD⚡**


    <div class="power-card">
    NATIONAL POWER GRID CONTROL SYSTEM

    <br><br>

    ⚡ Initializing Grid Network ⚡


    </div>


    """,
    unsafe_allow_html=True
    )



    st.write("")



    progress_value = min(
        st.session_state.boot / 100,
        1.0
    )


    progress = st.progress(
        progress_value
    )


    status = st.empty()



    loading_steps = [

        "⚡ Activating Power Grid Interface",

        "🔌 Synchronizing Transmission Network",

        "🏭 Connecting Grid Stations",

        "🛰 Establishing Control Link",

        "✅ GRIDSHIELD ONLINE"

    ]



    if st.session_state.boot < 100:


        st.session_state.boot += 4



        current = min(
            st.session_state.boot,
            100
        )


        progress.progress(
            current / 100
        )



        index = min(
            current // 20,
            4
        )


        status.info(
            loading_steps[index]
        )


        time.sleep(0.08)


        st.rerun()



    else:


        status.success(
            "⚡ GRIDSHIELD SYSTEM READY ⚡ "
        )


        time.sleep(0.8)


        st.session_state.login_screen = True


        st.rerun()
# ==========================================================
# 🔐 GRIDSHIELD OPERATOR LOGIN
# ==========================================================


def login_page():


    st.markdown("""

    <style>


    .login-title{


        text-align:center;

        font-size:55px;

        font-weight:1000;

        color:#00E5FF;

        text-shadow:

        0 0 15px cyan,

        0 0 40px cyan;


    }



    .login-box{


        width:500px;

        margin:auto;

        padding:35px;


        border-radius:25px;


        background:

        linear-gradient(

        145deg,

        #061826,

        #000000

        );


        border:2px solid #00E5FF;


        box-shadow:

        0 0 30px cyan;


    }



    .login-text{


        text-align:center;

        color:white;

        font-size:22px;

        font-weight:bold;

    }



    .bolt{


        text-align:center;

        font-size:60px;

        animation:flash 1s infinite;

    }



    @keyframes flash{


        0%{

        opacity:0.4;

        }


        50%{

        opacity:1;

        }


        100%{

        opacity:0.4;

        }


    }


    </style>


    """,unsafe_allow_html=True)




    st.markdown(
    """

    <div class="bolt">
    <div class="login-title">
    ⚡GRIDSHIELD⚡

    </div>

    <br>


    <div class="login-box">


    <div class="login-text">

       🔐 OPERATOR ACCESS 🔐 

    National Grid Control Console

    </div>


    </div>


    """,

    unsafe_allow_html=True

    )


    st.write("")



    col1,col2,col3 = st.columns(
        [1,2,1]
    )



    with col2:


        email = st.text_input(

            "📧 OPERATOR EMAIL"

        )



        password = st.text_input(

            "🔑 PASSWORD",

            type="password"

        )



        st.write("")



        if st.button(

            "⚡ ENTER GRIDSHIELD ⚡ ",

            use_container_width=True

        ):



            # DEMO LOGIN
            # ANY EMAIL AND PASSWORD ACCEPTED


            if email.strip() != "" and password.strip() != "":


                st.session_state.logged_in = True


                st.success(

                    "⚡ Access Granted ⚡"

                )


                time.sleep(0.8)


                st.rerun()



            else:


                st.warning(

                    "Please enter email and password"

                )
# ==========================================================
# 🚀 GRIDSHIELD SYSTEM STARTUP AFTER LOGIN
# ==========================================================


def launch_gridshield():


    st.markdown("""

    <style>


    .launch-title{


        text-align:center;

        font-size:60px;

        font-weight:1000;

        color:#00E5FF;


        text-shadow:

        0 0 20px cyan,

        0 0 50px cyan;


    }



    .launch-box{


        text-align:center;

        font-size:22px;

        color:white;


        border:2px solid #00E5FF;

        border-radius:20px;

        padding:25px;

        width:70%;

        margin:auto;


        background:

        linear-gradient(

        135deg,

        #001A33,

        #000000

        );


        box-shadow:

        0 0 25px cyan;


    }



    </style>


    """,unsafe_allow_html=True)



    st.markdown(

    """

    <div class="launch-title">
    ⚡ GRIDSHIELD COMMAND CENTER ⚡

    </div>


    <br>


    <div class="launch-box">

    ---National Power Grid Interface---
    <br><br>
    ⚡ Establishing Secure Connection ⚡ 
    
    </div>

    """,

    unsafe_allow_html=True

    )



    st.write("")



    progress = st.progress(0)



    status = st.empty()



    startup_steps = [


        "🔐 Verifying Operator Session",

        "⚡ Loading Grid Engine",

        "🛰 Connecting Monitoring Modules",

        "🌍 Loading National Grid Map",

        "📊 Activating Analytics",

        "✅ Command Center Ready"


    ]



    for i,step in enumerate(startup_steps):


        status.info(step)



        value = int(

            ((i+1)/len(startup_steps))*100

        )



        progress.progress(

            min(value,100)

        )


        time.sleep(0.35)



    st.session_state.dashboard_loaded = True



    time.sleep(0.5)



    # OPEN DASHBOARD


    try:

        st.switch_page(

            "pages/1_📊_DASHBOARD.py"

        )


    except:


        st.warning(

            "CLICK ON 📊 DASHBOARD"
        )

# ==========================================================
# ⚡ GRIDSHIELD APPLICATION CONTROLLER
# ==========================================================


# FIRST TIME OPEN
if st.session_state.boot < 100:


    gridshield_loading()


    st.stop()



# AFTER LOADING SCREEN


if not st.session_state.login_screen:


    st.session_state.login_screen = True



# SHOW LOGIN


if not st.session_state.logged_in:


    login_page()


    st.stop()



# AFTER SUCCESSFUL LOGIN


if not st.session_state.dashboard_loaded:


    launch_gridshield()


    st.stop()



# ==========================================================
# FALLBACK
# ==========================================================


st.success(
    "⚡ GRIDSHIELD SYSTEM ACTIVE"
)
# ==========================================================
# ⚡ ELECTRIC GRID VISUAL EFFECT
# ==========================================================


st.markdown("""

<style>


.stApp{


background:

linear-gradient(

120deg,

#000814,

#001f3f,

#000000

);


overflow:hidden;


}



/* MOVING POWER GRID */


.stApp::before{


content:"";


position:fixed;


top:0;

left:0;


width:200%;

height:200%;



background-image:


linear-gradient(

90deg,

rgba(0,229,255,0.08) 1px,

transparent 1px

),


linear-gradient(

0deg,

rgba(0,229,255,0.08) 1px,

transparent 1px

);



background-size:

60px 60px;



animation:

gridmove 8s linear infinite;



z-index:-1;


}



@keyframes gridmove{


0%{


transform:

translate(0,0);

}



100%{


transform:

translate(-60px,-60px);


}



}





/* ELECTRIC FLASH */


.electric-flash{


position:fixed;


top:20%;


left:10%;


font-size:70px;


opacity:0.8;


animation:

flashmove 2s infinite;


}



@keyframes flashmove{


0%{


opacity:0.1;

transform:scale(0.8);


}


50%{


opacity:1;

transform:scale(1.2);


}


100%{


opacity:0.1;

transform:scale(0.8);


}



}





/* REMOVE STREAMLIT TOP SPACE */


.block-container{


padding-top:1rem;


}



</style>


""",
unsafe_allow_html=True)



st.markdown(

"""

<div class="electric-flash">
⚡

</div>

""",

unsafe_allow_html=True

)
# ==========================================================
# ⚡ FINAL GRIDSHIELD ROUTER
# ==========================================================


# STEP 1 : LOADING SCREEN

if st.session_state.boot < 100:


    gridshield_loading()


    st.stop()



# STEP 2 : LOGIN


if not st.session_state.logged_in:


    login_page()


    st.stop()



# STEP 3 : COMMAND CENTER STARTUP


if not st.session_state.dashboard_loaded:


    launch_gridshield()


    st.stop()



# STEP 4 : OPEN DASHBOARD


st.switch_page(
    "pages/1_📊_DASHBOARD.py"
)
