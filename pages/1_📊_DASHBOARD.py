
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="⚡ GRIDSHIELD Command Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.block-container{
padding-top:1rem;
padding-bottom:0rem;
}

[data-testid="stMetric"]{
background:#111827;
padding:18px;
border-radius:18px;
border:1px solid #1f2937;
box-shadow:0px 0px 15px rgba(0,255,255,.15);
}

h1{
color:#00E5FF;
}

h2{
color:#29B6F6;
}

</style>
""",unsafe_allow_html=True)

# ============================================================
# 🇮🇳 COMPLETE NATIONAL DATABASE
# ============================================================

GRID_DATA=[

{"state":"Andhra Pradesh","population":53900000,"generation":48,"consumption":44,"waste":4,"money_required":10200,"money_spent":9650,"renewable":41,"industrial":18,"domestic":19,"commercial":7,"health":96,"status":"GREEN"},

{"state":"Arunachal Pradesh","population":1600000,"generation":7,"consumption":5,"waste":2,"money_required":1900,"money_spent":1700,"renewable":82,"industrial":1,"domestic":3,"commercial":1,"health":97,"status":"GREEN"},

{"state":"Assam","population":35600000,"generation":14,"consumption":12,"waste":2,"money_required":4200,"money_spent":3900,"renewable":44,"industrial":4,"domestic":6,"commercial":2,"health":95,"status":"GREEN"},

{"state":"Bihar","population":128500000,"generation":21,"consumption":19,"waste":2,"money_required":9100,"money_spent":8700,"renewable":24,"industrial":6,"domestic":10,"commercial":3,"health":93,"status":"YELLOW"},

{"state":"Chhattisgarh","population":30100000,"generation":44,"consumption":29,"waste":15,"money_required":7600,"money_spent":7100,"renewable":29,"industrial":15,"domestic":9,"commercial":5,"health":90,"status":"YELLOW"},

{"state":"Goa","population":1600000,"generation":5,"consumption":4,"waste":1,"money_required":1200,"money_spent":1100,"renewable":36,"industrial":1,"domestic":2,"commercial":1,"health":98,"status":"GREEN"},

{"state":"Gujarat","population":71500000,"generation":63,"consumption":57,"waste":6,"money_required":14100,"money_spent":13500,"renewable":49,"industrial":26,"domestic":20,"commercial":11,"health":97,"status":"GREEN"},

{"state":"Haryana","population":30200000,"generation":25,"consumption":23,"waste":2,"money_required":6200,"money_spent":5800,"renewable":31,"industrial":10,"domestic":9,"commercial":4,"health":95,"status":"GREEN"},

{"state":"Himachal Pradesh","population":7600000,"generation":18,"consumption":10,"waste":8,"money_required":3600,"money_spent":3300,"renewable":88,"industrial":2,"domestic":6,"commercial":2,"health":98,"status":"GREEN"},

{"state":"Jharkhand","population":40100000,"generation":28,"consumption":23,"waste":5,"money_required":6500,"money_spent":6100,"renewable":25,"industrial":11,"domestic":9,"commercial":3,"health":91,"status":"YELLOW"},

{"state":"Karnataka","population":69500000,"generation":49,"consumption":44,"waste":5,"money_required":10800,"money_spent":10100,"renewable":58,"industrial":16,"domestic":21,"commercial":7,"health":96,"status":"GREEN"},

{"state":"Kerala","population":35600000,"generation":17,"consumption":15,"waste":2,"money_required":4700,"money_spent":4350,"renewable":63,"industrial":4,"domestic":8,"commercial":3,"health":98,"status":"GREEN"},

{"state":"Madhya Pradesh","population":86500000,"generation":46,"consumption":39,"waste":7,"money_required":11200,"money_spent":10400,"renewable":37,"industrial":16,"domestic":17,"commercial":6,"health":94,"status":"GREEN"},

{"state":"Maharashtra","population":128000000,"generation":72,"consumption":66,"waste":6,"money_required":18200,"money_spent":17400,"renewable":42,"industrial":31,"domestic":25,"commercial":10,"health":96,"status":"GREEN"},

{"state":"Manipur","population":3300000,"generation":4,"consumption":3,"waste":1,"money_required":1100,"money_spent":980,"renewable":56,"industrial":1,"domestic":2,"commercial":0.5,"health":94,"status":"GREEN"},

{"state":"Meghalaya","population":3500000,"generation":6,"consumption":4,"waste":2,"money_required":1450,"money_spent":1300,"renewable":73,"industrial":1,"domestic":2,"commercial":1,"health":96,"status":"GREEN"},

{"state":"Mizoram","population":1300000,"generation":3,"consumption":2,"waste":1,"money_required":950,"money_spent":860,"renewable":67,"industrial":0.5,"domestic":1.2,"commercial":0.3,"health":97,"status":"GREEN"},

{"state":"Nagaland","population":2300000,"generation":4,"consumption":3,"waste":1,"money_required":980,"money_spent":910,"renewable":61,"industrial":0.8,"domestic":1.8,"commercial":0.4,"health":95,"status":"GREEN"},

{"state":"Odisha","population":47000000,"generation":39,"consumption":31,"waste":8,"money_required":8200,"money_spent":7600,"renewable":35,"industrial":15,"domestic":12,"commercial":4,"health":92,"status":"YELLOW"},

{"state":"Punjab","population":31200000,"generation":22,"consumption":20,"waste":2,"money_required":6100,"money_spent":5700,"renewable":28,"industrial":8,"domestic":9,"commercial":3,"health":94,"status":"GREEN"},

{"state":"Rajasthan","population":83200000,"generation":58,"consumption":46,"waste":12,"money_required":13300,"money_spent":12600,"renewable":69,"industrial":17,"domestic":21,"commercial":8,"health":95,"status":"GREEN"},

{"state":"Sikkim","population":700000,"generation":5,"consumption":2,"waste":3,"money_required":1200,"money_spent":1100,"renewable":91,"industrial":0.5,"domestic":1,"commercial":0.5,"health":99,"status":"GREEN"},

{"state":"Tamil Nadu","population":78000000,"generation":61,"consumption":56,"waste":5,"money_required":15100,"money_spent":14500,"renewable":54,"industrial":24,"domestic":23,"commercial":9,"health":98,"status":"GREEN"},

{"state":"Telangana","population":40300000,"generation":37,"consumption":34,"waste":3,"money_required":9200,"money_spent":8700,"renewable":39,"industrial":14,"domestic":15,"commercial":5,"health":96,"status":"GREEN"},

{"state":"Tripura","population":4300000,"generation":6,"consumption":5,"waste":1,"money_required":1500,"money_spent":1380,"renewable":48,"industrial":1,"domestic":3,"commercial":1,"health":95,"status":"GREEN"},

{"state":"Uttar Pradesh","population":241000000,"generation":76,"consumption":71,"waste":5,"money_required":20500,"money_spent":19700,"renewable":26,"industrial":24,"domestic":34,"commercial":13,"health":93,"status":"YELLOW"},

{"state":"Uttarakhand","population":11800000,"generation":20,"consumption":14,"waste":6,"money_required":4300,"money_spent":4000,"renewable":84,"industrial":3,"domestic":8,"commercial":3,"health":97,"status":"GREEN"},

{"state":"West Bengal","population":100000000,"generation":41,"consumption":38,"waste":3,"money_required":10900,"money_spent":10300,"renewable":32,"industrial":16,"domestic":17,"commercial":5,"health":95,"status":"GREEN"},

{"state":"Andaman & Nicobar","population":410000,"generation":1,"consumption":0.8,"waste":0.2,"money_required":650,"money_spent":590,"renewable":52,"industrial":0.1,"domestic":0.5,"commercial":0.2,"health":98,"status":"GREEN"},

{"state":"Chandigarh","population":1250000,"generation":2,"consumption":1.8,"waste":0.2,"money_required":900,"money_spent":850,"renewable":31,"industrial":0.4,"domestic":1,"commercial":0.4,"health":97,"status":"GREEN"},

{"state":"Dadra & Nagar Haveli and Daman & Diu","population":950000,"generation":3,"consumption":2.5,"waste":0.5,"money_required":880,"money_spent":810,"renewable":34,"industrial":1.2,"domestic":0.9,"commercial":0.4,"health":96,"status":"GREEN"},

{"state":"Delhi","population":21000000,"generation":11,"consumption":12,"waste":1,"money_required":7600,"money_spent":7300,"renewable":22,"industrial":3,"domestic":6,"commercial":3,"health":91,"status":"YELLOW"},

{"state":"Jammu & Kashmir","population":13600000,"generation":15,"consumption":12,"waste":3,"money_required":4200,"money_spent":3900,"renewable":71,"industrial":3,"domestic":7,"commercial":2,"health":95,"status":"GREEN"},

{"state":"Ladakh","population":310000,"generation":2,"consumption":1.1,"waste":0.9,"money_required":800,"money_spent":730,"renewable":94,"industrial":0.2,"domestic":0.7,"commercial":0.2,"health":99,"status":"GREEN"},

{"state":"Lakshadweep","population":68000,"generation":0.5,"consumption":0.4,"waste":0.1,"money_required":300,"money_spent":270,"renewable":87,"industrial":0.05,"domestic":0.25,"commercial":0.1,"health":99,"status":"GREEN"},

{"state":"Puducherry","population":1700000,"generation":3,"consumption":2.8,"waste":0.2,"money_required":950,"money_spent":900,"renewable":43,"industrial":0.8,"domestic":1.4,"commercial":0.6,"health":97,"status":"GREEN"}

]

df = pd.DataFrame(GRID_DATA)
# ============================================================
# ⚡ NATIONAL COMMAND SUMMARY
# ============================================================

st.title("⚡GRIDSHIELD NATIONAL COMMAND CENTER⚡")

st.subheader(
    "AI Powered National Power Grid Command & Decision Support System"
)

st.success("🟢 NATIONAL GRID STATUS : STABLE")

st.divider()


# ============================================================
# NATIONAL CALCULATIONS
# ============================================================

total_population = df["population"].sum()

total_generation = df["generation"].sum()

total_consumption = df["consumption"].sum()

total_waste = df["waste"].sum()

total_required = df["money_required"].sum()

total_spent = df["money_spent"].sum()

avg_health = round(df["health"].mean(), 2)

avg_renewable = round(df["renewable"].mean(), 2)

grid_efficiency = round(
    (total_consumption / total_generation) * 100,
    2
)


# ============================================================
# EXECUTIVE KPI CARDS
# ============================================================
st.header("📊 NATIONAL GRID EXECUTIVE DASHBOARD 📊")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "👥 Population Served",
        f"{total_population/1_000_000:.1f} M"
    )

with c2:
    st.metric(
        "⚡ Generation",
        f"{total_generation:.1f} GW"
    )

with c3:
    st.metric(
        "🔋 Consumption",
        f"{total_consumption:.1f} GW"
    )

with c4:
    st.metric(
        "♻ Energy Loss",
        f"{total_waste:.1f} GW"
    )

with c5:
    st.metric(
        "🟢 Grid Health",
        f"{avg_health}%"
    )


c6, c7, c8, c9, c10 = st.columns(5)

with c6:
    st.metric(
        "💰 Budget Required",
        f"₹ {total_required:,} Cr"
    )

with c7:
    st.metric(
        "💸 Budget Spent",
        f"₹ {total_spent:,} Cr"
    )

with c8:
    st.metric(
        "⚡ Grid Efficiency",
        f"{grid_efficiency}%"
    )

with c9:
    st.metric(
        "🌱 Renewable Share",
        f"{avg_renewable}%"
    )

with c10:
    st.metric(
        "🏛 Regions",
        len(df)
    )

st.divider()


# ============================================================
# NATIONAL LIVE STATUS
# ============================================================

green = len(df[df["status"] == "GREEN"])
yellow = len(df[df["status"] == "YELLOW"])
red = len(df[df["status"] == "RED"])

a, b, c = st.columns(3)

with a:
    st.success(f"🟢 Healthy Regions : {green}")

with b:
    st.warning(f"🟡 Warning Regions : {yellow}")

with c:
    st.error(f"🔴 Critical Regions : {red}")

st.divider()
# ============================================================
# 🇮🇳 INTERACTIVE STATE / UT COMMAND CENTER
# ============================================================

st.header("🗺️ STATE & UNION TERRITORY COMMAND CENTER")

selected_state = st.selectbox(
    "Select State / Union Territory",
    sorted(df["state"].tolist())
)

state = df[df["state"] == selected_state].iloc[0]

st.divider()

st.subheader(f"⚡ {selected_state} GRID INTELLIGENCE REPORT")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "👥 Population",
        f"{state['population']:,}"
    )

with k2:
    st.metric(
        "⚡ Generation",
        f"{state['generation']} GW"
    )

with k3:
    st.metric(
        "🔋 Consumption",
        f"{state['consumption']} GW"
    )

with k4:
    st.metric(
        "♻ Energy Loss",
        f"{state['waste']} GW"
    )



k5, k6, k7, k8 = st.columns(4)

with k5:
    st.metric(
        "💰 Budget Required",
        f"₹ {state['money_required']:,} Cr"
    )

with k6:
    st.metric(
        "💸 Budget Spent",
        f"₹ {state['money_spent']:,} Cr"
    )

with k7:
    st.metric(
        "🌱 Renewable",
        f"{state['renewable']} %"
    )

with k8:
    st.metric(
        "🟢 Grid Health",
        f"{state['health']} %"
    )



k9, k10, k11 = st.columns(3)

with k9:
    st.metric(
        "🏭 Industrial Demand",
        f"{state['industrial']} GW"
    )

with k10:
    st.metric(
        "🏠 Domestic Demand",
        f"{state['domestic']} GW"
    )

with k11:
    st.metric(
        "🏢 Commercial Demand",
        f"{state['commercial']} GW"
    )

st.divider()


# ============================================================
# AI ANALYSIS
# ============================================================

st.header("🤖 AI GRID ANALYSIS")

efficiency = round(
    (state["consumption"] / state["generation"]) * 100,
    2
)

if state["status"] == "GREEN":

    st.success(f"""
### 🟢 {selected_state}

✅ Grid operating normally

✅ Grid Health : {state['health']}%

✅ Energy Efficiency : {efficiency}%

✅ Renewable Energy : {state['renewable']}%

✅ Budget Utilization :
₹ {state['money_spent']:,} Cr

Recommendation

• Continue preventive maintenance

• Monitor renewable generation

• Maintain reserve capacity
""")

elif state["status"] == "YELLOW":

    st.warning(f"""
### 🟡 {selected_state}

⚠ Grid requires monitoring

⚠ Energy Loss : {state['waste']} GW

⚠ Renewable Share : {state['renewable']}%

⚠ Efficiency : {efficiency}%

Recommendation

• Reduce transmission losses

• Increase reserve generation

• Deploy inspection teams
""")

else:

    st.error(f"""
### 🔴 {selected_state}

🚨 Critical Grid Condition

🚨 Immediate intervention required

🚨 Heavy power loss detected

🚨 Activate emergency response

Recommendation

• Dispatch engineers immediately

• Restore transmission corridors

• Prioritize hospitals & essential services
""")

st.divider()
# ============================================================
# 📊 NATIONAL VISUAL ANALYTICS
# ============================================================

st.header("📊 NATIONAL POWER ANALYTICS ⚡")


# ============================================================
# GENERATION vs CONSUMPTION
# ============================================================

fig1 = px.bar(

    df,

    x="state",

    y=["generation","consumption"],

    barmode="group",

    color="state",

    text_auto=True,

    title="⚡ State-wise Power Generation vs Consumption"

)

fig1.update_layout(

    height=600,

    xaxis_title="States / Union Territories",

    yaxis_title="Power (GW)",

    legend_title="Parameter"

)

st.plotly_chart(
    fig1,
    use_container_width=True
)


# ============================================================
# GRID HEALTH
# ============================================================

fig2 = px.bar(

    df.sort_values("health",ascending=False),

    x="state",

    y="health",

    color="health",

    text="health",

    title="🟢 State-wise Grid Health (%)",

    color_continuous_scale="Turbo"

)

fig2.update_layout(

    height=600,

    xaxis_title="States",

    yaxis_title="Health (%)"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# ============================================================
# ENERGY LOSS
# ============================================================

fig3 = px.pie(

    df,

    names="state",

    values="waste",

    hole=0.45,

    title="♻ State-wise Energy Loss Distribution",

    color_discrete_sequence=px.colors.qualitative.Bold

)

st.plotly_chart(
    fig3,
    use_container_width=True
)


# ============================================================
# RENEWABLE SHARE
# ============================================================

fig4 = px.treemap(

    df,

    path=["state"],

    values="renewable",

    color="renewable",

    color_continuous_scale="Viridis",

    title="🌱 Renewable Energy Share"

)

st.plotly_chart(
    fig4,
    use_container_width=True
)


# ============================================================
# POPULATION vs CONSUMPTION
# ============================================================

fig5 = px.scatter(

    df,

    x="population",

    y="consumption",

    size="generation",

    color="health",

    hover_name="state",

    title="👥 Population vs Power Consumption",

    color_continuous_scale="Rainbow"

)

fig5.update_layout(height=650)

st.plotly_chart(
    fig5,
    use_container_width=True
)


# ============================================================
# BUDGET ANALYSIS
# ============================================================

fig6 = px.bar(

    df,

    x="state",

    y=["money_required","money_spent"],

    barmode="group",

    color="state",

    title="💰 Budget Required vs Budget Spent"

)

fig6.update_layout(

    height=650,

    yaxis_title="₹ Crores"

)

st.plotly_chart(
    fig6,
    use_container_width=True
)


st.divider()
# ============================================================
# 📈 NATIONAL ADVANCED ANALYTICS
# ============================================================

st.header("📈 ADVANCED NATIONAL GRID ANALYTICS")

left, right = st.columns(2)

# ============================================================
# ENERGY DEMAND DISTRIBUTION
# ============================================================

with left:

    fig7 = px.sunburst(

        df,

        path=["status", "state"],

        values="consumption",

        color="health",

        color_continuous_scale="Turbo",

        title="⚡ National Demand Distribution"

    )

    st.plotly_chart(
        fig7,
        use_container_width=True
    )


# ============================================================
# BUDGET UTILIZATION
# ============================================================

with right:

    fig8 = px.funnel(

        df.sort_values(
            "money_spent",
            ascending=False
        ),

        x="money_spent",

        y="state",

        color="state",

        title="💸 Budget Utilization"

    )

    st.plotly_chart(
        fig8,
        use_container_width=True
    )


st.divider()


# ============================================================
# INDUSTRIAL / DOMESTIC / COMMERCIAL
# ============================================================

fig9 = px.bar(

    df,

    x="state",

    y=[

        "industrial",

        "domestic",

        "commercial"

    ],

    barmode="stack",

    color_discrete_sequence=px.colors.qualitative.Vivid,

    title="🏭 State-wise Electricity Consumption Sector"

)

fig9.update_layout(

    height=700,

    xaxis_title="States",

    yaxis_title="GW"

)

st.plotly_chart(
    fig9,
    use_container_width=True
)


# ============================================================
# GRID HEALTH GAUGE
# ============================================================

fig10 = go.Figure(

    go.Indicator(

        mode="gauge+number",

        value=avg_health,

        title={

            "text":"🇮🇳 National Grid Health"

        },

        gauge={

            "axis":{"range":[0,100]},

            "bar":{"color":"lime"},

            "steps":[

                {"range":[0,40],"color":"red"},

                {"range":[40,70],"color":"orange"},

                {"range":[70,100],"color":"green"}

            ]

        }

    )

)

fig10.update_layout(
    height=450
)

st.plotly_chart(
    fig10,
    use_container_width=True
)


# ============================================================
# TOP 10 POWER PRODUCERS
# ============================================================

st.subheader("🏆 TOP 10 POWER GENERATING STATES")

top_generation = df.sort_values(

    "generation",

    ascending=False

).head(10)

fig11 = px.bar(

    top_generation,

    x="state",

    y="generation",

    color="generation",

    text="generation",

    color_continuous_scale="Plasma"

)

fig11.update_layout(height=600)

st.plotly_chart(
    fig11,
    use_container_width=True
)


# ============================================================
# TOP 10 POWER CONSUMERS
# ============================================================

st.subheader("🔋 TOP 10 POWER CONSUMING STATES")

top_consumption = df.sort_values(

    "consumption",

    ascending=False

).head(10)

fig12 = px.bar(

    top_consumption,

    x="state",

    y="consumption",

    color="consumption",

    text="consumption",

    color_continuous_scale="Rainbow"

)

fig12.update_layout(height=600)

st.plotly_chart(
    fig12,
    use_container_width=True
)


st.divider()
# ============================================================
# 🚨 NATIONAL AI COMMAND CENTER
# ============================================================

st.header("🤖 NATIONAL AI COMMAND CENTER")

# ------------------------------------------------------------
# AI SCORE CALCULATIONS
# ------------------------------------------------------------

df["efficiency"] = (
    (df["consumption"] / df["generation"]) * 100
).round(2)

df["budget_utilization"] = (
    (df["money_spent"] / df["money_required"]) * 100
).round(2)

df["risk_score"] = (
    (100 - df["health"])
    + (df["waste"] * 2)
    + (100 - df["renewable"]) * 0.10
).round(2)


# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "🤖 AI Risk Score",
        f"{df['risk_score'].mean():.1f}"
    )

with c2:

    st.metric(
        "⚡ Avg Efficiency",
        f"{df['efficiency'].mean():.2f}%"
    )

with c3:

    st.metric(
        "💰 Budget Utilization",
        f"{df['budget_utilization'].mean():.2f}%"
    )

with c4:

    st.metric(
        "🟢 National Health",
        f"{df['health'].mean():.2f}%"
    )

st.divider()


# ------------------------------------------------------------
# RISK HEATMAP
# ------------------------------------------------------------

st.subheader("🔥 National Risk Heatmap")

fig13 = px.density_heatmap(

    df,

    x="state",

    y="risk_score",

    z="health",

    color_continuous_scale="Turbo",

    title="AI Risk Assessment"

)

st.plotly_chart(
    fig13,
    use_container_width=True
)

st.divider()


# ------------------------------------------------------------
# AI RANKING
# ------------------------------------------------------------

st.subheader("🚨 Highest Risk Regions")

risk_df = df.sort_values(
    "risk_score",
    ascending=False
)

st.dataframe(

    risk_df[[
        "state",
        "risk_score",
        "health",
        "generation",
        "consumption",
        "waste",
        "efficiency"
    ]],

    use_container_width=True,

    hide_index=True

)

st.divider()


# ------------------------------------------------------------
# NATIONAL ALERT ENGINE
# ------------------------------------------------------------

st.subheader("🚨 LIVE AI ALERT ENGINE")

for _, row in risk_df.head(10).iterrows():

    if row["risk_score"] >= 20:

        st.error(f"""
🔴 {row['state']}

Risk Score : {row['risk_score']}

Grid Health : {row['health']}%

Action :

• Immediate Inspection

• Backup Generation

• AI Fault Isolation

• Deploy Emergency Team
""")

    elif row["risk_score"] >= 12:

        st.warning(f"""
🟡 {row['state']}

Risk Score : {row['risk_score']}

Action :

• Increase Monitoring

• Check Transmission Lines

• Verify Load Balance
""")

    else:

        st.success(f"""
🟢 {row['state']}

Grid Stable

Preventive Monitoring Active
""")

st.divider()


# ------------------------------------------------------------
# AI RECOMMENDATION
# ------------------------------------------------------------

st.header("🧠 NATIONAL AI RECOMMENDATION")

st.info(f"""

🇮🇳 National Grid Intelligence Report

👥 Population Served :
{total_population:,}

⚡ Total Generation :
{total_generation} GW

🔋 Total Consumption :
{total_consumption} GW

♻ Energy Loss :
{total_waste} GW

💰 Budget Required :
₹ {total_required:,} Crores

💸 Budget Utilized :
₹ {total_spent:,} Crores

🌱 Average Renewable Energy :
{avg_renewable}%

⚡ National Efficiency :
{grid_efficiency}%

🤖 Overall AI Status :

GRIDSHIELD AI predicts a stable national grid with localized monitoring
requirements. Renewable integration is satisfactory. Budget utilization
remains healthy. Continue predictive maintenance and AI surveillance
across all states and union territories.

""")

st.divider()

st.success("⚡ GRIDSHIELD NATIONAL COMMAND CENTER ONLINE 🇮🇳")

st.caption(
    "GRIDSHIELD V2.0 | AI Powered National Grid Intelligence Platform | Developed by AKASH.V"
)
if st.button("🚪 Logout"):

    st.session_state.logged_in = False

    st.switch_page("pages/LOGIN.py")