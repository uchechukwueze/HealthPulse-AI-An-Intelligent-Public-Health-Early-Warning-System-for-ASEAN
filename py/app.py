# # ============================================================
# # HealthPulse AI
# # Beautiful Streamlit App Layout
# # ASEAN Public Health Early-Warning System
# # ============================================================

# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px
# import plotly.graph_objects as go
# from pathlib import Path


# # ============================================================
# # PAGE CONFIG
# # ============================================================

# st.set_page_config(
#     page_title="HealthPulse AI",
#     page_icon="🩺",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )


# # ============================================================
# # BRAND SETTINGS
# # ============================================================

# BRAND = {
#     "navy": "#071B3A",
#     "blue": "#0B3C68",
#     "cyan": "#00B4D8",
#     "teal": "#00A896",
#     "green": "#2E7D32",
#     "gold": "#F9C74F",
#     "orange": "#F8961E",
#     "red": "#D62828",
#     "cream": "#F7F9FC",
#     "white": "#FFFFFF",
#     "muted": "#6B7280",
#     "dark": "#111827"
# }

# RISK_COLORS = {
#     "Low": BRAND["green"],
#     "Medium": BRAND["gold"],
#     "High": BRAND["red"]
# }

# READINESS_COLORS = {
#     "Low": BRAND["red"],
#     "Medium": BRAND["gold"],
#     "High": BRAND["green"]
# }

# PRIORITY_COLORS = {
#     "Emergency Priority": BRAND["red"],
#     "High Priority": BRAND["orange"],
#     "Preventive Priority": BRAND["gold"],
#     "Monitor Closely": BRAND["cyan"],
#     "Moderate Priority": BRAND["blue"],
#     "Capacity Building Needed": "#8B5CF6",
#     "Controlled Risk": BRAND["teal"],
#     "Stable but Needs Support": "#60A5FA",
#     "Stable / Resilient": BRAND["green"]
# }


# # ============================================================
# # CUSTOM CSS
# # ============================================================

# st.markdown(
#     f"""
#     <style>

#     /* Main page */
#     .stApp {{
#         background: linear-gradient(180deg, #F7F9FC 0%, #FFFFFF 45%, #F7F9FC 100%);
#     }}

#     /* Sidebar */
#     section[data-testid="stSidebar"] {{
#         background: linear-gradient(180deg, {BRAND["navy"]} 0%, {BRAND["blue"]} 100%);
#     }}

#     section[data-testid="stSidebar"] * {{
#         color: white !important;
#     }}

#     /* Hide Streamlit default */
#     #MainMenu {{visibility: hidden;}}
#     footer {{visibility: hidden;}}

#     /* Hero section */
#     .hero {{
#         padding: 34px 38px;
#         border-radius: 24px;
#         background: linear-gradient(135deg, {BRAND["navy"]} 0%, {BRAND["blue"]} 55%, {BRAND["cyan"]} 120%);
#         color: white;
#         margin-bottom: 28px;
#         box-shadow: 0 18px 45px rgba(7, 27, 58, 0.22);
#     }}

#     .hero h1 {{
#         font-size: 48px;
#         font-weight: 900;
#         margin: 0;
#         letter-spacing: -1.5px;
#         color: white;
#     }}

#     .hero p {{
#         font-size: 19px;
#         margin-top: 10px;
#         max-width: 950px;
#         line-height: 1.55;
#         color: #E5F7FF;
#     }}

#     .hero-badge {{
#         display: inline-block;
#         padding: 8px 14px;
#         border-radius: 999px;
#         background: rgba(255, 255, 255, 0.15);
#         border: 1px solid rgba(255, 255, 255, 0.25);
#         font-size: 13px;
#         font-weight: 700;
#         margin-bottom: 14px;
#         color: white;
#     }}

#     /* Cards */
#     .metric-card {{
#         background: white;
#         padding: 22px 22px;
#         border-radius: 18px;
#         border: 1px solid #E5E7EB;
#         box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
#         min-height: 120px;
#     }}

#     .metric-label {{
#         color: {BRAND["muted"]};
#         font-size: 13px;
#         font-weight: 700;
#         text-transform: uppercase;
#         letter-spacing: .6px;
#         margin-bottom: 8px;
#     }}

#     .metric-value {{
#         color: {BRAND["navy"]};
#         font-size: 34px;
#         font-weight: 900;
#         margin-bottom: 2px;
#     }}

#     .metric-note {{
#         color: {BRAND["muted"]};
#         font-size: 13px;
#     }}

#     .section-title {{
#         font-size: 26px;
#         font-weight: 900;
#         color: {BRAND["navy"]};
#         margin-top: 8px;
#         margin-bottom: 6px;
#     }}

#     .section-subtitle {{
#         color: {BRAND["muted"]};
#         font-size: 15px;
#         margin-bottom: 20px;
#     }}

#     .glass-card {{
#         background: rgba(255, 255, 255, 0.92);
#         border: 1px solid #E5E7EB;
#         border-radius: 20px;
#         padding: 22px;
#         box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
#     }}

#     .pill {{
#         display: inline-block;
#         padding: 7px 12px;
#         border-radius: 999px;
#         font-size: 13px;
#         font-weight: 800;
#         margin-right: 6px;
#         margin-bottom: 6px;
#     }}

#     .pill-high {{
#         background: rgba(214, 40, 40, 0.12);
#         color: {BRAND["red"]};
#     }}

#     .pill-medium {{
#         background: rgba(249, 199, 79, 0.20);
#         color: #9A6A00;
#     }}

#     .pill-low {{
#         background: rgba(46, 125, 50, 0.12);
#         color: {BRAND["green"]};
#     }}

#     .recommendation-box {{
#         background: linear-gradient(135deg, #FFFFFF 0%, #EEF8FF 100%);
#         border-left: 6px solid {BRAND["cyan"]};
#         border-radius: 18px;
#         padding: 22px;
#         box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
#         line-height: 1.6;
#         color: {BRAND["dark"]};
#     }}

#     .warning-box {{
#         background: rgba(214, 40, 40, 0.08);
#         border-left: 6px solid {BRAND["red"]};
#         border-radius: 16px;
#         padding: 18px;
#         color: {BRAND["dark"]};
#     }}

#     div[data-testid="stDataFrame"] {{
#         border-radius: 18px;
#         overflow: hidden;
#     }}

#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # ============================================================
# # LOAD DATA
# # ============================================================

# @st.cache_data
# def load_data():
#     health_df = pd.read_csv("asean_health_risk_readiness_priority.csv")
#     ai_output = pd.read_csv("healthpulse_ai_recommendations.csv")
#     return health_df, ai_output


# @st.cache_resource
# def load_model():
#     model = joblib.load("healthpulse_final_model.pkl")
#     features = joblib.load("healthpulse_model_features.pkl")
#     label_mapping = joblib.load("healthpulse_risk_label_mapping.pkl")
#     return model, features, label_mapping


# health_df, ai_output = load_data()
# model, final_features, reverse_risk_mapping = load_model()

# health_df["year"] = health_df["year"].astype(int)
# ai_output["year"] = ai_output["year"].astype(int)


# # ============================================================
# # PLOTLY TEMPLATE
# # ============================================================

# plotly_template = "plotly_white"

# px.defaults.template = plotly_template
# px.defaults.color_discrete_sequence = [
#     BRAND["blue"],
#     BRAND["cyan"],
#     BRAND["teal"],
#     BRAND["gold"],
#     BRAND["orange"],
#     BRAND["red"]
# ]


# # ============================================================
# # HELPER FUNCTIONS
# # ============================================================

# def metric_card(label, value, note=""):
#     st.markdown(
#         f"""
#         <div class="metric-card">
#             <div class="metric-label">{label}</div>
#             <div class="metric-value">{value}</div>
#             <div class="metric-note">{note}</div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


# def section_header(title, subtitle=""):
#     st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
#     if subtitle:
#         st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


# def risk_badge(level):
#     level = str(level)
#     if level == "High":
#         return '<span class="pill pill-high">🔴 High Risk</span>'
#     elif level == "Medium":
#         return '<span class="pill pill-medium">🟡 Medium Risk</span>'
#     return '<span class="pill pill-low">🟢 Low Risk</span>'


# def readiness_badge(level):
#     level = str(level)
#     if level == "High":
#         return '<span class="pill pill-low">🟢 High Readiness</span>'
#     elif level == "Medium":
#         return '<span class="pill pill-medium">🟡 Medium Readiness</span>'
#     return '<span class="pill pill-high">🔴 Low Readiness</span>'


# def predict_next_risk(selected_row):
#     X = selected_row[final_features]
#     pred_encoded = model.predict(X)[0]
#     pred_level = reverse_risk_mapping[pred_encoded]

#     probabilities = model.predict_proba(X)[0]
#     class_names = [reverse_risk_mapping[i] for i in model.classes_]

#     prob_dict = {
#         class_names[i]: probabilities[i]
#         for i in range(len(class_names))
#     }

#     return pred_level, prob_dict


# risk_indicators = [
#     "infant_mortality_rate",
#     "under_5_mortality_rate",
#     "maternal_mortality_rate",
#     "malaria_prevalence",
#     "tb_prevalence",
#     "undernourished_population"
# ]

# readiness_indicators = [
#     "government_health_expenditure",
#     "dpt_immunization",
#     "measles_immunization",
#     "nurses_midwives_density",
#     "physicians_density"
# ]

# indicator_medians = health_df[final_features].median()


# def readable_name(col):
#     return col.replace("_", " ").title()


# def identify_concerns(row, top_n=5):
#     concerns = []

#     for col in risk_indicators:
#         value = row[col]
#         median_value = indicator_medians[col]
#         if value > median_value:
#             concerns.append({
#                 "indicator": col,
#                 "message": f"{readable_name(col)} is above the ASEAN median.",
#                 "gap": value - median_value
#             })

#     for col in readiness_indicators:
#         value = row[col]
#         median_value = indicator_medians[col]
#         if value < median_value:
#             concerns.append({
#                 "indicator": col,
#                 "message": f"{readable_name(col)} is below the ASEAN median.",
#                 "gap": median_value - value
#             })

#     concerns = sorted(concerns, key=lambda x: x["gap"], reverse=True)
#     return concerns[:top_n]


# def generate_actions(concerns):
#     indicators = [item["indicator"] for item in concerns]
#     actions = []

#     if "under_5_mortality_rate" in indicators or "infant_mortality_rate" in indicators:
#         actions.append("Expand child health services, immunization outreach, and early disease screening.")

#     if "maternal_mortality_rate" in indicators:
#         actions.append("Prioritize emergency obstetric care, skilled birth attendance, and maternal referral systems.")

#     if "malaria_prevalence" in indicators:
#         actions.append("Strengthen malaria surveillance, rapid testing, vector control, and community prevention.")

#     if "tb_prevalence" in indicators:
#         actions.append("Scale TB screening, treatment adherence support, and community health monitoring.")

#     if "undernourished_population" in indicators:
#         actions.append("Integrate nutrition support with maternal and child health programs.")

#     if "dpt_immunization" in indicators or "measles_immunization" in indicators:
#         actions.append("Launch targeted vaccine catch-up campaigns and strengthen routine immunization systems.")

#     if "nurses_midwives_density" in indicators:
#         actions.append("Increase deployment of nurses and midwives in underserved facilities.")

#     if "physicians_density" in indicators:
#         actions.append("Use mobile clinics, telemedicine, and rural service incentives to improve physician access.")

#     if "government_health_expenditure" in indicators:
#         actions.append("Increase targeted public health financing for frontline services and high-burden regions.")

#     if not actions:
#         actions.append("Maintain health investments, continue monitoring, and strengthen early-warning surveillance.")

#     return actions


# def create_recommendation_text(row, pred_level, prob_dict):
#     concerns = identify_concerns(row, top_n=5)
#     actions = generate_actions(concerns)

#     concern_text = ""
#     for idx, item in enumerate(concerns, 1):
#         concern_text += f"<li>{item['message']}</li>"

#     action_text = ""
#     for idx, action in enumerate(actions, 1):
#         action_text += f"<li>{action}</li>"

#     prob_high = prob_dict.get("High", 0)

#     return f"""
#     <div class="recommendation-box">
#         <h3 style="margin-top:0;color:{BRAND['navy']};">AI Public Health Recommendation</h3>
#         <p><b>Predicted next-year risk:</b> {pred_level} risk</p>
#         <p><b>Probability of high risk:</b> {prob_high:.1%}</p>

#         <h4 style="color:{BRAND['blue']};">Main risk signals</h4>
#         <ol>{concern_text}</ol>

#         <h4 style="color:{BRAND['blue']};">Recommended actions</h4>
#         <ol>{action_text}</ol>
#     </div>
#     """


# def style_plotly(fig, title=None):
#     fig.update_layout(
#         template="plotly_white",
#         paper_bgcolor="rgba(0,0,0,0)",
#         plot_bgcolor="rgba(0,0,0,0)",
#         font=dict(family="Arial", color=BRAND["dark"]),
#         title=dict(
#             text=title if title else fig.layout.title.text,
#             font=dict(size=20, color=BRAND["navy"]),
#             x=0.02
#         ),
#         margin=dict(l=30, r=30, t=70, b=40),
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=-0.25,
#             xanchor="center",
#             x=0.5
#         )
#     )
#     fig.update_xaxes(showgrid=False)
#     fig.update_yaxes(gridcolor="rgba(0,0,0,0.08)")
#     return fig


# # ============================================================
# # SIDEBAR BRANDING
# # ============================================================

# logo_path = Path("assets/10alytics_logo.png")

# with st.sidebar:
#     if logo_path.exists():
#         st.image(str(logo_path), use_container_width=True)
#     else:
#         st.markdown(
#             """
#             <div style="font-size:28px;font-weight:900;margin-bottom:0;">10Alytics</div>
#             <div style="font-size:13px;opacity:.8;margin-bottom:20px;">Global Hackathon 2026</div>
#             """,
#             unsafe_allow_html=True
#         )

#     st.markdown("---")

#     page = st.radio(
#         "Navigation",
#         [
#             "Executive Overview",
#             "Risk Intelligence",
#             "Readiness & Priority",
#             "AI Prediction Copilot",
#             "Country Deep Dive",
#             "Methodology"
#         ]
#     )

#     st.markdown("---")
#     st.caption("HealthPulse AI · SDG 3")


# # ============================================================
# # HERO
# # ============================================================

# def render_hero():
#     st.markdown(
#         """
#         <div class="hero">
#             <div class="hero-badge">SDG 3 · AI for Public Health Resilience</div>
#             <h1>HealthPulse AI</h1>
#             <p>
#             A predictive public health intelligence system for ASEAN — combining health risk scoring,
#             system readiness, machine learning, and AI recommendations to identify where intervention
#             is needed before the next crisis escalates.
#             </p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


# # ============================================================
# # PAGE 1: EXECUTIVE OVERVIEW
# # ============================================================

# if page == "Executive Overview":

#     render_hero()

#     latest_year = health_df["year"].max()
#     latest_df = health_df[health_df["year"] == latest_year].copy()

#     avg_risk = latest_df["health_risk_score"].mean()
#     avg_readiness = latest_df["readiness_score"].mean()
#     high_risk = (latest_df["health_risk_level"] == "High").sum()
#     emergency = (latest_df["priority_category"] == "Emergency Priority").sum()

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:
#         metric_card("Countries", health_df["country"].nunique(), "ASEAN member countries")

#     with c2:
#         metric_card("Years", f"{health_df['year'].min()}–{health_df['year'].max()}", "Historical panel dataset")

#     with c3:
#         metric_card("Avg. 2014 Risk", f"{avg_risk:.1f}", "Composite health risk score")

#     with c4:
#         metric_card("Emergency Cases", emergency, f"In {latest_year}")

#     st.markdown("<br>", unsafe_allow_html=True)

#     section_header(
#         "2014 ASEAN Health Risk Snapshot",
#         "Countries are ranked by their composite Health Risk Score."
#     )

#     country_latest = latest_df.sort_values("health_risk_score", ascending=False)

#     fig = px.bar(
#         country_latest,
#         x="health_risk_score",
#         y="country",
#         orientation="h",
#         color="health_risk_level",
#         color_discrete_map=RISK_COLORS,
#         text="health_risk_score"
#     )

#     fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
#     fig.update_yaxes(categoryorder="total ascending")
#     fig.update_layout(height=520)
#     fig = style_plotly(fig, "Health Risk Scores Across ASEAN Countries, 2014")

#     st.plotly_chart(fig, use_container_width=True)

#     section_header(
#         "Risk Category Trend",
#         "Share of ASEAN countries classified as Low, Medium, or High risk over time."
#     )

#     risk_share = (
#         health_df
#         .groupby(["year", "health_risk_level"])
#         .size()
#         .reset_index(name="count")
#     )

#     risk_share["share"] = (
#         risk_share
#         .groupby("year")["count"]
#         .transform(lambda x: x / x.sum() * 100)
#     )

#     fig_area = px.area(
#         risk_share,
#         x="year",
#         y="share",
#         color="health_risk_level",
#         color_discrete_map=RISK_COLORS,
#         category_orders={"health_risk_level": ["High", "Medium", "Low"]}
#     )

#     fig_area.update_layout(height=430)
#     fig_area = style_plotly(fig_area, "Health Risk Levels Across ASEAN, 2004–2014")
#     fig_area.update_yaxes(title="Share of countries (%)")
#     fig_area.update_xaxes(title="Year")

#     st.plotly_chart(fig_area, use_container_width=True)


# # ============================================================
# # PAGE 2: RISK INTELLIGENCE
# # ============================================================

# elif page == "Risk Intelligence":

#     render_hero()

#     section_header(
#         "Risk Intelligence",
#         "Explore countries with the highest health burden and how risk changed over time."
#     )

#     selected_year = st.selectbox(
#         "Select year",
#         sorted(health_df["year"].unique()),
#         index=len(sorted(health_df["year"].unique())) - 1
#     )

#     year_df = health_df[health_df["year"] == selected_year].copy()

#     left, right = st.columns([1.25, 1])

#     with left:
#         fig = px.bar(
#             year_df.sort_values("health_risk_score", ascending=False),
#             x="country",
#             y="health_risk_score",
#             color="health_risk_level",
#             color_discrete_map=RISK_COLORS,
#             text="health_risk_score"
#         )
#         fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
#         fig.update_layout(height=440)
#         fig = style_plotly(fig, f"Health Risk Scores by Country, {selected_year}")
#         st.plotly_chart(fig, use_container_width=True)

#     with right:
#         risk_counts = year_df["health_risk_level"].value_counts().reset_index()
#         risk_counts.columns = ["risk_level", "count"]

#         fig_pie = px.pie(
#             risk_counts,
#             names="risk_level",
#             values="count",
#             hole=0.55,
#             color="risk_level",
#             color_discrete_map=RISK_COLORS
#         )
#         fig_pie.update_layout(height=440)
#         fig_pie = style_plotly(fig_pie, f"Risk Category Mix, {selected_year}")
#         st.plotly_chart(fig_pie, use_container_width=True)

#     section_header("Country Risk Trends", "Compare health risk score movement from 2004 to 2014.")

#     countries = st.multiselect(
#         "Select countries to compare",
#         options=sorted(health_df["country"].unique()),
#         default=sorted(health_df["country"].unique())[:4]
#     )

#     trend_df = health_df[health_df["country"].isin(countries)]

#     fig_line = px.line(
#         trend_df,
#         x="year",
#         y="health_risk_score",
#         color="country",
#         markers=True
#     )
#     fig_line.update_layout(height=480)
#     fig_line = style_plotly(fig_line, "Health Risk Trend by Country")
#     st.plotly_chart(fig_line, use_container_width=True)


# # ============================================================
# # PAGE 3: READINESS AND PRIORITY
# # ============================================================

# elif page == "Readiness & Priority":

#     render_hero()

#     section_header(
#         "Readiness & Priority Matrix",
#         "Identify countries with high health risk and weak response capacity."
#     )

#     selected_year = st.selectbox(
#         "Select year",
#         sorted(health_df["year"].unique()),
#         index=len(sorted(health_df["year"].unique())) - 1
#     )

#     matrix_df = health_df[health_df["year"] == selected_year].copy()

#     c1, c2 = st.columns([1.2, 1])

#     with c1:
#         fig_matrix = px.scatter(
#             matrix_df,
#             x="readiness_score",
#             y="health_risk_score",
#             color="priority_category",
#             size="health_risk_score",
#             hover_name="country",
#             color_discrete_map=PRIORITY_COLORS,
#             size_max=34
#         )

#         fig_matrix.add_vline(
#             x=matrix_df["readiness_score"].median(),
#             line_dash="dash",
#             line_color="gray"
#         )

#         fig_matrix.add_hline(
#             y=matrix_df["health_risk_score"].median(),
#             line_dash="dash",
#             line_color="gray"
#         )

#         fig_matrix.update_layout(height=530)
#         fig_matrix = style_plotly(fig_matrix, f"Risk–Readiness Priority Matrix, {selected_year}")
#         fig_matrix.update_xaxes(title="Health system readiness score")
#         fig_matrix.update_yaxes(title="Health risk score")

#         st.plotly_chart(fig_matrix, use_container_width=True)

#     with c2:
#         priority_counts = (
#             matrix_df["priority_category"]
#             .value_counts()
#             .reset_index()
#         )
#         priority_counts.columns = ["priority_category", "count"]

#         fig_priority = px.bar(
#             priority_counts,
#             x="count",
#             y="priority_category",
#             orientation="h",
#             color="priority_category",
#             color_discrete_map=PRIORITY_COLORS,
#             text="count"
#         )

#         fig_priority.update_yaxes(categoryorder="total ascending")
#         fig_priority.update_layout(height=530, showlegend=False)
#         fig_priority = style_plotly(fig_priority, "Priority Category Distribution")

#         st.plotly_chart(fig_priority, use_container_width=True)

#     section_header("Priority Table", "Countries sorted by urgency.")

#     priority_table = matrix_df[
#         [
#             "country",
#             "health_risk_score",
#             "health_risk_level",
#             "readiness_score",
#             "readiness_level",
#             "priority_category"
#         ]
#     ].sort_values(
#         ["health_risk_score", "readiness_score"],
#         ascending=[False, True]
#     )

#     st.dataframe(priority_table, use_container_width=True, hide_index=True)


# # ============================================================
# # PAGE 4: AI PREDICTION COPILOT
# # ============================================================

# elif page == "AI Prediction Copilot":

#     render_hero()

#     section_header(
#         "AI Prediction Copilot",
#         "Predict next-year health risk and generate public health recommendations."
#     )

#     col_left, col_right = st.columns([0.9, 1.1])

#     with col_left:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)

#         country = st.selectbox(
#             "Select country",
#             sorted(health_df["country"].unique())
#         )

#         country_df = health_df[health_df["country"] == country].copy()

#         year = st.selectbox(
#             "Select assessment year",
#             sorted(country_df["year"].unique())
#         )

#         selected_row = country_df[country_df["year"] == year].copy()

#         st.markdown("</div>", unsafe_allow_html=True)

#     with col_right:
#         if not selected_row.empty:
#             pred_level, prob_dict = predict_next_risk(selected_row)

#             c1, c2, c3 = st.columns(3)

#             with c1:
#                 metric_card(
#                     "Current Risk",
#                     selected_row["health_risk_level"].iloc[0],
#                     f"Score: {selected_row['health_risk_score'].iloc[0]:.1f}"
#                 )

#             with c2:
#                 metric_card(
#                     "Readiness",
#                     selected_row["readiness_level"].iloc[0],
#                     f"Score: {selected_row['readiness_score'].iloc[0]:.1f}"
#                 )

#             with c3:
#                 metric_card(
#                     "Predicted Risk",
#                     pred_level,
#                     "Next-year risk level"
#                 )

#             st.markdown(
#                 risk_badge(selected_row["health_risk_level"].iloc[0])
#                 + readiness_badge(selected_row["readiness_level"].iloc[0]),
#                 unsafe_allow_html=True
#             )

#     if not selected_row.empty:

#         st.markdown("<br>", unsafe_allow_html=True)

#         prob_df = pd.DataFrame({
#             "Risk Level": list(prob_dict.keys()),
#             "Probability": list(prob_dict.values())
#         })

#         fig_prob = px.bar(
#             prob_df,
#             x="Risk Level",
#             y="Probability",
#             color="Risk Level",
#             color_discrete_map=RISK_COLORS,
#             text="Probability"
#         )
#         fig_prob.update_traces(texttemplate="%{text:.1%}", textposition="outside")
#         fig_prob.update_layout(height=390, showlegend=False)
#         fig_prob.update_yaxes(tickformat=".0%")
#         fig_prob = style_plotly(fig_prob, "Prediction Probability")

#         st.plotly_chart(fig_prob, use_container_width=True)

#         recommendation_html = create_recommendation_text(
#             selected_row.iloc[0],
#             pred_level,
#             prob_dict
#         )

#         st.markdown(recommendation_html, unsafe_allow_html=True)


# # ============================================================
# # PAGE 5: COUNTRY DEEP DIVE
# # ============================================================

# elif page == "Country Deep Dive":

#     render_hero()

#     section_header(
#         "Country Deep Dive",
#         "Explore a country’s health risk, readiness, and priority pathway over time."
#     )

#     country = st.selectbox(
#         "Select country",
#         sorted(health_df["country"].unique())
#     )

#     country_df = health_df[health_df["country"] == country].copy()

#     latest_row = country_df.sort_values("year").iloc[-1]

#     c1, c2, c3 = st.columns(3)

#     with c1:
#         metric_card("Latest Risk Score", f"{latest_row['health_risk_score']:.1f}", latest_row["health_risk_level"])

#     with c2:
#         metric_card("Latest Readiness", f"{latest_row['readiness_score']:.1f}", latest_row["readiness_level"])

#     with c3:
#         metric_card("Priority", latest_row["priority_category"], f"Year: {latest_row['year']}")

#     fig = go.Figure()

#     fig.add_trace(
#         go.Scatter(
#             x=country_df["year"],
#             y=country_df["health_risk_score"],
#             mode="lines+markers",
#             name="Health risk score",
#             line=dict(color=BRAND["red"], width=4)
#         )
#     )

#     fig.add_trace(
#         go.Scatter(
#             x=country_df["year"],
#             y=country_df["readiness_score"],
#             mode="lines+markers",
#             name="Readiness score",
#             line=dict(color=BRAND["teal"], width=4)
#         )
#     )

#     fig.update_layout(height=500)
#     fig = style_plotly(fig, f"Risk and Readiness Trend: {country}")

#     st.plotly_chart(fig, use_container_width=True)

#     section_header("Country-Year Records")

#     st.dataframe(
#         country_df[
#             [
#                 "country",
#                 "year",
#                 "health_risk_score",
#                 "health_risk_level",
#                 "readiness_score",
#                 "readiness_level",
#                 "priority_category"
#             ]
#         ],
#         use_container_width=True,
#         hide_index=True
#     )


# # ============================================================
# # PAGE 6: METHODOLOGY
# # ============================================================

# elif page == "Methodology":

#     render_hero()

#     section_header("Methodology", "How HealthPulse AI was built.")

#     st.markdown(
#         """
#         <div class="glass-card">
#         <h3>1. Health Risk Index</h3>
#         <p>
#         The Health Risk Index measures direct public health burden using infant mortality,
#         under-5 mortality, maternal mortality, malaria prevalence, tuberculosis prevalence,
#         and undernourished population. The indicators were normalized and combined into a
#         0–100 score, then classified into Low, Medium, and High risk.
#         </p>

#         <h3>2. Health System Readiness Score</h3>
#         <p>
#         The Readiness Score measures system capacity using government health expenditure,
#         DPT immunization, measles immunization, nurses/midwives density, and physician density.
#         Higher readiness indicates stronger health system capacity.
#         </p>

#         <h3>3. Risk–Readiness Priority Matrix</h3>
#         <p>
#         Health risk and readiness were combined to classify country-year observations into
#         policy priority groups such as Emergency Priority, High Priority, Preventive Priority,
#         and Stable / Resilient.
#         </p>

#         <h3>4. Machine Learning Model</h3>
#         <p>
#         A next-year prediction model was trained so that current-year indicators predict the
#         following year’s health risk level. The final model uses raw health indicators and
#         predicts Low, Medium, or High next-year risk.
#         </p>

#         <h3>5. AI Recommendation Layer</h3>
#         <p>
#         The recommendation engine compares each country’s indicators against ASEAN median values,
#         identifies major concern signals, and translates them into targeted public health actions.
#         </p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )


# ============================================================
# HealthPulse AI
# 10Alytics Global Hackathon 2026
# SDG 3: Public Health Early-Warning System for ASEAN
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import textwrap


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HealthPulse AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# BRAND COLORS
# ============================================================

BRAND = {
    "navy": "#071B3A",
    "blue": "#0B3C68",
    "cyan": "#00B4D8",
    "teal": "#00A896",
    "green": "#2E7D32",
    "gold": "#F9C74F",
    "orange": "#F8961E",
    "red": "#D62828",
    "cream": "#F7F9FC",
    "white": "#FFFFFF",
    "muted": "#6B7280",
    "dark": "#111827"
}

RISK_COLORS = {
    "Low": BRAND["green"],
    "Medium": BRAND["gold"],
    "High": BRAND["red"]
}

READINESS_COLORS = {
    "Low": BRAND["red"],
    "Medium": BRAND["gold"],
    "High": BRAND["green"]
}

PRIORITY_COLORS = {
    "Emergency Priority": BRAND["red"],
    "High Priority": BRAND["orange"],
    "Preventive Priority": BRAND["gold"],
    "Monitor Closely": BRAND["cyan"],
    "Moderate Priority": BRAND["blue"],
    "Capacity Building Needed": "#8B5CF6",
    "Controlled Risk": BRAND["teal"],
    "Stable but Needs Support": "#60A5FA",
    "Stable / Resilient": BRAND["green"]
}


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background: linear-gradient(180deg, #F7F9FC 0%, #FFFFFF 45%, #F7F9FC 100%);
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {BRAND["navy"]} 0%, {BRAND["blue"]} 100%);
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    .hero {{
        padding: 34px 38px;
        border-radius: 24px;
        background: linear-gradient(135deg, {BRAND["navy"]} 0%, {BRAND["blue"]} 55%, {BRAND["cyan"]} 120%);
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 18px 45px rgba(7, 27, 58, 0.22);
    }}

    .hero h1 {{
        font-size: 48px;
        font-weight: 900;
        margin: 0;
        letter-spacing: -1.5px;
        color: white;
    }}

    .hero p {{
        font-size: 19px;
        margin-top: 10px;
        max-width: 1000px;
        line-height: 1.55;
        color: #E5F7FF;
    }}

    .hero-badge {{
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.25);
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 14px;
        color: white;
    }}

    .metric-card {{
        background: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
        min-height: 120px;
    }}

    .metric-label {{
        color: {BRAND["muted"]};
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .6px;
        margin-bottom: 8px;
    }}

    .metric-value {{
        color: {BRAND["navy"]};
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 2px;
    }}

    .metric-note {{
        color: {BRAND["muted"]};
        font-size: 13px;
    }}

    .section-title {{
        font-size: 26px;
        font-weight: 900;
        color: {BRAND["navy"]};
        margin-top: 8px;
        margin-bottom: 6px;
    }}

    .section-subtitle {{
        color: {BRAND["muted"]};
        font-size: 15px;
        margin-bottom: 20px;
    }}

    .glass-card {{
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid #E5E7EB;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
    }}

    .pill {{
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 800;
        margin-right: 6px;
        margin-bottom: 6px;
    }}

    .pill-high {{
        background: rgba(214, 40, 40, 0.12);
        color: {BRAND["red"]};
    }}

    .pill-medium {{
        background: rgba(249, 199, 79, 0.22);
        color: #9A6A00;
    }}

    .pill-low {{
        background: rgba(46, 125, 50, 0.12);
        color: {BRAND["green"]};
    }}

    .recommendation-box {{
        background: linear-gradient(135deg, #FFFFFF 0%, #EEF8FF 100%);
        border-left: 6px solid {BRAND["cyan"]};
        border-radius: 18px;
        padding: 26px;
        box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
        line-height: 1.65;
        color: {BRAND["dark"]};
        margin-top: 18px;
    }}

    .recommendation-box h3 {{
        margin-top: 0;
        color: {BRAND["navy"]};
        font-size: 25px;
        font-weight: 900;
    }}

    .recommendation-box h4 {{
        color: {BRAND["blue"]};
        margin-top: 20px;
        margin-bottom: 8px;
        font-weight: 900;
    }}

    .recommendation-box li {{
        margin-bottom: 7px;
    }}

    .method-card {{
        background: white;
        padding: 26px;
        border-radius: 20px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 10px 28px rgba(17, 24, 39, 0.06);
        line-height: 1.65;
    }}

    .method-card h3 {{
        color: {BRAND["navy"]};
        font-weight: 900;
    }}

    div[data-testid="stDataFrame"] {{
        border-radius: 18px;
        overflow: hidden;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA AND MODEL
# ============================================================

@st.cache_data
def load_data():
    health_df = pd.read_csv("asean_health_risk_readiness_priority.csv")
    return health_df


@st.cache_resource
def load_model():
    model = joblib.load("healthpulse_final_model.pkl")
    features = joblib.load("healthpulse_model_features.pkl")
    label_mapping = joblib.load("healthpulse_risk_label_mapping.pkl")
    return model, features, label_mapping


health_df = load_data()
model, final_features, reverse_risk_mapping = load_model()

health_df["year"] = health_df["year"].astype(int)

for col in ["health_risk_level", "readiness_level"]:
    if col in health_df.columns:
        health_df[col] = health_df[col].astype(str)


# ============================================================
# PLOTLY STYLE
# ============================================================

px.defaults.template = "plotly_white"
px.defaults.color_discrete_sequence = [
    BRAND["blue"],
    BRAND["cyan"],
    BRAND["teal"],
    BRAND["gold"],
    BRAND["orange"],
    BRAND["red"]
]


def style_plotly(fig, title=None):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", color=BRAND["dark"]),
        title=dict(
            text=title if title else fig.layout.title.text,
            font=dict(size=20, color=BRAND["navy"]),
            x=0.02
        ),
        margin=dict(l=30, r=30, t=70, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        )
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="rgba(0,0,0,0.08)")
    return fig


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def metric_card(label, value, note=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_header(title, subtitle=""):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def risk_badge(level):
    level = str(level)

    if level == "High":
        return '<span class="pill pill-high">🔴 High Risk</span>'
    elif level == "Medium":
        return '<span class="pill pill-medium">🟡 Medium Risk</span>'
    else:
        return '<span class="pill pill-low">🟢 Low Risk</span>'


def readiness_badge(level):
    level = str(level)

    if level == "High":
        return '<span class="pill pill-low">🟢 High Readiness</span>'
    elif level == "Medium":
        return '<span class="pill pill-medium">🟡 Medium Readiness</span>'
    else:
        return '<span class="pill pill-high">🔴 Low Readiness</span>'


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">10Alytics Global Hackathon 2026 · SDG 3</div>
            <h1>HealthPulse AI</h1>
            <p>
            An AI-powered public health early-warning and response system for ASEAN.
            HealthPulse AI combines health risk scoring, system readiness, machine learning,
            and AI recommendations to identify where intervention is needed before a crisis escalates.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def readable_name(col):
    return col.replace("_", " ").title()


risk_indicators = [
    "infant_mortality_rate",
    "under_5_mortality_rate",
    "maternal_mortality_rate",
    "malaria_prevalence",
    "tb_prevalence",
    "undernourished_population"
]

readiness_indicators = [
    "government_health_expenditure",
    "dpt_immunization",
    "measles_immunization",
    "nurses_midwives_density",
    "physicians_density"
]

indicator_medians = health_df[final_features].median(numeric_only=True)


def predict_next_risk(selected_row):
    X = selected_row[final_features]

    pred_encoded = model.predict(X)[0]
    pred_level = reverse_risk_mapping[int(pred_encoded)]

    probabilities = model.predict_proba(X)[0]
    class_names = [reverse_risk_mapping[int(i)] for i in model.classes_]

    prob_dict = {
        class_names[i]: probabilities[i]
        for i in range(len(class_names))
    }

    return pred_level, prob_dict


def identify_concerns(row, top_n=5):
    concerns = []

    for col in risk_indicators:
        value = row[col]
        median_value = indicator_medians[col]

        if value > median_value:
            concerns.append({
                "indicator": col,
                "message": f"{readable_name(col)} is above the ASEAN median.",
                "gap": value - median_value
            })

    for col in readiness_indicators:
        value = row[col]
        median_value = indicator_medians[col]

        if value < median_value:
            concerns.append({
                "indicator": col,
                "message": f"{readable_name(col)} is below the ASEAN median.",
                "gap": median_value - value
            })

    concerns = sorted(concerns, key=lambda x: x["gap"], reverse=True)

    return concerns[:top_n]


def generate_actions(concerns):
    indicators = [item["indicator"] for item in concerns]
    actions = []

    if "under_5_mortality_rate" in indicators or "infant_mortality_rate" in indicators:
        actions.append(
            "Expand child health services, immunization outreach, early childhood disease screening, and community-level child survival programs."
        )

    if "maternal_mortality_rate" in indicators:
        actions.append(
            "Prioritize emergency obstetric care, skilled birth attendance, maternal referral systems, and midwife-led maternal health services."
        )

    if "malaria_prevalence" in indicators:
        actions.append(
            "Strengthen malaria surveillance, rapid testing, vector control, and community prevention campaigns."
        )

    if "tb_prevalence" in indicators:
        actions.append(
            "Scale TB screening, case detection, treatment adherence support, and community health monitoring."
        )

    if "undernourished_population" in indicators:
        actions.append(
            "Integrate nutrition support with maternal and child health programs, especially in vulnerable communities."
        )

    if "dpt_immunization" in indicators or "measles_immunization" in indicators:
        actions.append(
            "Launch targeted vaccine catch-up campaigns and strengthen routine immunization systems."
        )

    if "nurses_midwives_density" in indicators:
        actions.append(
            "Increase deployment of nurses and midwives, especially in underserved and rural health facilities."
        )

    if "physicians_density" in indicators:
        actions.append(
            "Use mobile clinics, telemedicine support, and rural service incentives to improve physician access."
        )

    if "government_health_expenditure" in indicators:
        actions.append(
            "Increase targeted public health financing toward frontline health services and high-burden health priorities."
        )

    if not actions:
        actions.append(
            "Maintain current health investments, continue surveillance, and monitor early-warning indicators."
        )

    return actions


def create_recommendation_text(row, pred_level, prob_dict):
    concerns = identify_concerns(row, top_n=5)
    actions = generate_actions(concerns)

    concern_items = "".join(
        [f"<li>{item['message']}</li>" for item in concerns]
    )

    action_items = "".join(
        [f"<li>{action}</li>" for action in actions]
    )

    prob_high = prob_dict.get("High", 0)

    html = f"""
<div class="recommendation-box">
    <h3>AI Public Health Recommendation</h3>

    <p><b>Country assessed:</b> {row["country"]}</p>
    <p><b>Assessment year:</b> {int(row["year"])}</p>
    <p><b>Predicted next-year risk:</b> {pred_level} risk</p>
    <p><b>Probability of high risk:</b> {prob_high:.1%}</p>

    <h4>Main risk signals</h4>
    <ol>
        {concern_items}
    </ol>

    <h4>Recommended actions</h4>
    <ol>
        {action_items}
    </ol>
</div>
"""
    return textwrap.dedent(html)


# ============================================================
# SIDEBAR
# ============================================================

logo_path = Path("assets/10alytics_logo.png")

with st.sidebar:
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.markdown(
            """
            <div style="font-size:30px;font-weight:900;margin-bottom:0;">10Alytics</div>
            <div style="font-size:13px;opacity:.85;margin-bottom:20px;">Global Hackathon 2026</div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Executive Overview",
            "Risk Intelligence",
            "Readiness & Priority",
            "AI Prediction Copilot",
            "Country Deep Dive",
            "Methodology"
        ]
    )

    st.markdown("---")
    st.caption("HealthPulse AI · SDG 3")


# ============================================================
# PAGE 1: EXECUTIVE OVERVIEW
# ============================================================

if page == "Executive Overview":

    render_hero()

    latest_year = health_df["year"].max()
    latest_df = health_df[health_df["year"] == latest_year].copy()

    avg_risk = latest_df["health_risk_score"].mean()
    avg_readiness = latest_df["readiness_score"].mean()
    high_risk = (latest_df["health_risk_level"] == "High").sum()
    emergency = (latest_df["priority_category"] == "Emergency Priority").sum()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Countries", health_df["country"].nunique(), "ASEAN member countries")

    with c2:
        metric_card("Years", f"{health_df['year'].min()}–{health_df['year'].max()}", "Country-year panel data")

    with c3:
        metric_card("Avg. Risk", f"{avg_risk:.1f}", f"Average score in {latest_year}")

    with c4:
        metric_card("Emergency Cases", emergency, f"Priority cases in {latest_year}")

    st.markdown("<br>", unsafe_allow_html=True)

    section_header(
        "ASEAN Health Risk Snapshot",
        f"Countries ranked by Health Risk Score in {latest_year}."
    )

    country_latest = latest_df.sort_values("health_risk_score", ascending=False)

    fig = px.bar(
        country_latest,
        x="health_risk_score",
        y="country",
        orientation="h",
        color="health_risk_level",
        color_discrete_map=RISK_COLORS,
        text="health_risk_score"
    )

    fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    fig.update_yaxes(categoryorder="total ascending")
    fig.update_layout(height=520)
    fig = style_plotly(fig, f"Health Risk Scores Across ASEAN Countries, {latest_year}")

    st.plotly_chart(fig, use_container_width=True)

    section_header(
        "Risk Category Trend",
        "Share of ASEAN countries classified as Low, Medium, or High risk over time."
    )

    risk_share = (
        health_df
        .groupby(["year", "health_risk_level"])
        .size()
        .reset_index(name="count")
    )

    risk_share["share"] = (
        risk_share.groupby("year")["count"].transform(lambda x: x / x.sum() * 100)
    )

    fig_area = px.area(
        risk_share,
        x="year",
        y="share",
        color="health_risk_level",
        color_discrete_map=RISK_COLORS,
        category_orders={"health_risk_level": ["High", "Medium", "Low"]}
    )

    fig_area.update_layout(height=430)
    fig_area = style_plotly(fig_area, "Health Risk Levels Across ASEAN, 2004–2014")
    fig_area.update_yaxes(title="Share of countries (%)")
    fig_area.update_xaxes(title="Year")

    st.plotly_chart(fig_area, use_container_width=True)


# ============================================================
# PAGE 2: RISK INTELLIGENCE
# ============================================================

elif page == "Risk Intelligence":

    render_hero()

    section_header(
        "Risk Intelligence",
        "Explore countries with the highest health burden and how risk changed over time."
    )

    selected_year = st.selectbox(
        "Select year",
        sorted(health_df["year"].unique()),
        index=len(sorted(health_df["year"].unique())) - 1
    )

    year_df = health_df[health_df["year"] == selected_year].copy()

    left, right = st.columns([1.25, 1])

    with left:
        fig = px.bar(
            year_df.sort_values("health_risk_score", ascending=False),
            x="country",
            y="health_risk_score",
            color="health_risk_level",
            color_discrete_map=RISK_COLORS,
            text="health_risk_score"
        )

        fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
        fig.update_layout(height=440)
        fig = style_plotly(fig, f"Health Risk Scores by Country, {selected_year}")

        st.plotly_chart(fig, use_container_width=True)

    with right:
        risk_counts = year_df["health_risk_level"].value_counts().reset_index()
        risk_counts.columns = ["risk_level", "count"]

        fig_pie = px.pie(
            risk_counts,
            names="risk_level",
            values="count",
            hole=0.55,
            color="risk_level",
            color_discrete_map=RISK_COLORS
        )

        fig_pie.update_layout(height=440)
        fig_pie = style_plotly(fig_pie, f"Risk Category Mix, {selected_year}")

        st.plotly_chart(fig_pie, use_container_width=True)

    section_header("Country Risk Trends", "Compare Health Risk Score movement from 2004 to 2014.")

    countries = st.multiselect(
        "Select countries to compare",
        options=sorted(health_df["country"].unique()),
        default=sorted(health_df["country"].unique())[:4]
    )

    trend_df = health_df[health_df["country"].isin(countries)]

    fig_line = px.line(
        trend_df,
        x="year",
        y="health_risk_score",
        color="country",
        markers=True
    )

    fig_line.update_layout(height=480)
    fig_line = style_plotly(fig_line, "Health Risk Trend by Country")

    st.plotly_chart(fig_line, use_container_width=True)


# ============================================================
# PAGE 3: READINESS AND PRIORITY
# ============================================================

elif page == "Readiness & Priority":

    render_hero()

    section_header(
        "Readiness & Priority Matrix",
        "Identify countries with high health risk and weak response capacity."
    )

    selected_year = st.selectbox(
        "Select year",
        sorted(health_df["year"].unique()),
        index=len(sorted(health_df["year"].unique())) - 1
    )

    matrix_df = health_df[health_df["year"] == selected_year].copy()

    c1, c2 = st.columns([1.2, 1])

    with c1:
        fig_matrix = px.scatter(
            matrix_df,
            x="readiness_score",
            y="health_risk_score",
            color="priority_category",
            size="health_risk_score",
            hover_name="country",
            color_discrete_map=PRIORITY_COLORS,
            size_max=34
        )

        fig_matrix.add_vline(
            x=matrix_df["readiness_score"].median(),
            line_dash="dash",
            line_color="gray"
        )

        fig_matrix.add_hline(
            y=matrix_df["health_risk_score"].median(),
            line_dash="dash",
            line_color="gray"
        )

        fig_matrix.update_layout(height=530)
        fig_matrix = style_plotly(fig_matrix, f"Risk–Readiness Priority Matrix, {selected_year}")
        fig_matrix.update_xaxes(title="Health system readiness score")
        fig_matrix.update_yaxes(title="Health risk score")

        st.plotly_chart(fig_matrix, use_container_width=True)

    with c2:
        priority_counts = matrix_df["priority_category"].value_counts().reset_index()
        priority_counts.columns = ["priority_category", "count"]

        fig_priority = px.bar(
            priority_counts,
            x="count",
            y="priority_category",
            orientation="h",
            color="priority_category",
            color_discrete_map=PRIORITY_COLORS,
            text="count"
        )

        fig_priority.update_yaxes(categoryorder="total ascending")
        fig_priority.update_layout(height=530, showlegend=False)
        fig_priority = style_plotly(fig_priority, "Priority Category Distribution")

        st.plotly_chart(fig_priority, use_container_width=True)

    section_header("Priority Table", "Countries sorted by urgency.")

    priority_table = matrix_df[
        [
            "country",
            "health_risk_score",
            "health_risk_level",
            "readiness_score",
            "readiness_level",
            "priority_category"
        ]
    ].sort_values(
        ["health_risk_score", "readiness_score"],
        ascending=[False, True]
    )

    st.dataframe(priority_table, use_container_width=True, hide_index=True)


# ============================================================
# PAGE 4: AI PREDICTION COPILOT
# ============================================================

elif page == "AI Prediction Copilot":

    render_hero()

    section_header(
        "AI Prediction Copilot",
        "Predict next-year health risk and generate public health recommendations."
    )

    col_left, col_right = st.columns([0.9, 1.1])

    with col_left:
        country = st.selectbox(
            "Select country",
            sorted(health_df["country"].unique())
        )

        country_df = health_df[health_df["country"] == country].copy()

        year = st.selectbox(
            "Select assessment year",
            sorted(country_df["year"].unique())
        )

        selected_row = country_df[country_df["year"] == year].copy()

    with col_right:
        if not selected_row.empty:
            pred_level, prob_dict = predict_next_risk(selected_row)

            c1, c2, c3 = st.columns(3)

            with c1:
                metric_card(
                    "Current Risk",
                    selected_row["health_risk_level"].iloc[0],
                    f"Score: {selected_row['health_risk_score'].iloc[0]:.1f}"
                )

            with c2:
                metric_card(
                    "Readiness",
                    selected_row["readiness_level"].iloc[0],
                    f"Score: {selected_row['readiness_score'].iloc[0]:.1f}"
                )

            with c3:
                metric_card(
                    "Predicted Risk",
                    pred_level,
                    "Next-year risk level"
                )

            st.markdown(
                risk_badge(selected_row["health_risk_level"].iloc[0])
                + readiness_badge(selected_row["readiness_level"].iloc[0]),
                unsafe_allow_html=True
            )

    if not selected_row.empty:

        st.markdown("<br>", unsafe_allow_html=True)

        prob_df = pd.DataFrame({
            "Risk Level": list(prob_dict.keys()),
            "Probability": list(prob_dict.values())
        })

        fig_prob = px.bar(
            prob_df,
            x="Risk Level",
            y="Probability",
            color="Risk Level",
            color_discrete_map=RISK_COLORS,
            text="Probability"
        )

        fig_prob.update_traces(texttemplate="%{text:.1%}", textposition="outside")
        fig_prob.update_layout(height=390, showlegend=False)
        fig_prob.update_yaxes(tickformat=".0%")
        fig_prob = style_plotly(fig_prob, "Prediction Probability")

        st.plotly_chart(fig_prob, use_container_width=True)

        recommendation_html = create_recommendation_text(
            selected_row.iloc[0],
            pred_level,
            prob_dict
        )

        st.markdown(recommendation_html, unsafe_allow_html=True)


# ============================================================
# PAGE 5: COUNTRY DEEP DIVE
# ============================================================

elif page == "Country Deep Dive":

    render_hero()

    section_header(
        "Country Deep Dive",
        "Explore a country’s health risk, readiness, and priority pathway over time."
    )

    country = st.selectbox(
        "Select country",
        sorted(health_df["country"].unique())
    )

    country_df = health_df[health_df["country"] == country].copy()
    latest_row = country_df.sort_values("year").iloc[-1]

    c1, c2, c3 = st.columns(3)

    with c1:
        metric_card(
            "Latest Risk Score",
            f"{latest_row['health_risk_score']:.1f}",
            latest_row["health_risk_level"]
        )

    with c2:
        metric_card(
            "Latest Readiness",
            f"{latest_row['readiness_score']:.1f}",
            latest_row["readiness_level"]
        )

    with c3:
        metric_card(
            "Priority",
            latest_row["priority_category"],
            f"Year: {latest_row['year']}"
        )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=country_df["year"],
            y=country_df["health_risk_score"],
            mode="lines+markers",
            name="Health risk score",
            line=dict(color=BRAND["red"], width=4)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=country_df["year"],
            y=country_df["readiness_score"],
            mode="lines+markers",
            name="Readiness score",
            line=dict(color=BRAND["teal"], width=4)
        )
    )

    fig.update_layout(height=500)
    fig = style_plotly(fig, f"Risk and Readiness Trend: {country}")

    st.plotly_chart(fig, use_container_width=True)

    section_header("Country-Year Records")

    st.dataframe(
        country_df[
            [
                "country",
                "year",
                "health_risk_score",
                "health_risk_level",
                "readiness_score",
                "readiness_level",
                "priority_category"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 6: METHODOLOGY
# ============================================================

elif page == "Methodology":

    render_hero()

    section_header("Methodology", "How HealthPulse AI was built.")

    st.markdown(
        """
        <div class="method-card">
            <h3>1. Health Risk Index</h3>
            <p>
            The Health Risk Index measures direct public health burden using infant mortality,
            under-5 mortality, maternal mortality, malaria prevalence, tuberculosis prevalence,
            and undernourished population. Each indicator was normalized and combined into a
            0–100 score, then classified into Low, Medium, and High risk.
            </p>

            <h3>2. Health System Readiness Score</h3>
            <p>
            The Readiness Score measures system capacity using government health expenditure,
            DPT immunization, measles immunization, nurses/midwives density, and physician density.
            Higher readiness indicates stronger capacity to prevent and respond to health risks.
            </p>

            <h3>3. Risk–Readiness Priority Matrix</h3>
            <p>
            Health risk and readiness were combined to classify each country-year observation
            into policy priority groups such as Emergency Priority, High Priority, Preventive Priority,
            and Stable / Resilient.
            </p>

            <h3>4. Machine Learning Model</h3>
            <p>
            The machine learning model was structured as an early-warning system. Current-year
            public health indicators were used to predict the following year’s health risk level.
            The final model predicts Low, Medium, or High next-year risk.
            </p>

            <h3>5. AI Recommendation Layer</h3>
            <p>
            The recommendation layer compares each country’s indicators against ASEAN median values,
            identifies major risk signals, and translates them into targeted public health actions.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )