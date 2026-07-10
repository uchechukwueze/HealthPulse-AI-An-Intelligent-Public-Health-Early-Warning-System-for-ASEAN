# ============================================================
# HealthPulse AI Streamlit App
# Public Health Early-Warning System for ASEAN
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px


# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="HealthPulse AI",
    page_icon="🩺",
    layout="wide"
)


# ------------------------------------------------------------
# Load data and model
# ------------------------------------------------------------

@st.cache_data
def load_data():
    health_df = pd.read_csv("asean_health_risk_readiness_priority.csv")
    ai_output = pd.read_csv("healthpulse_ai_recommendations.csv")
    return health_df, ai_output


@st.cache_resource
def load_model():
    model = joblib.load("healthpulse_final_model.pkl")
    features = joblib.load("healthpulse_model_features.pkl")
    label_mapping = joblib.load("healthpulse_risk_label_mapping.pkl")
    return model, features, label_mapping


health_df, ai_output = load_data()
model, final_features, reverse_risk_mapping = load_model()

health_df["year"] = health_df["year"].astype(int)
ai_output["year"] = ai_output["year"].astype(int)


# ------------------------------------------------------------
# Styling
# ------------------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 44px;
        font-weight: 800;
        color: #0B3C68;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 20px;
        color: #555555;
        margin-top: 0px;
    }
    .metric-card {
        background-color: #F4F7FB;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #0B3C68;
    }
    .high-risk {
        color: #C62828;
        font-weight: bold;
    }
    .medium-risk {
        color: #E6A700;
        font-weight: bold;
    }
    .low-risk {
        color: #2E7D32;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def risk_color(level):
    if level == "High":
        return "🔴 High"
    elif level == "Medium":
        return "🟡 Medium"
    else:
        return "🟢 Low"


def readiness_color(level):
    if level == "High":
        return "🟢 High"
    elif level == "Medium":
        return "🟡 Medium"
    else:
        return "🔴 Low"


def generate_prediction(selected_row):
    X = selected_row[final_features]
    pred_encoded = model.predict(X)[0]
    pred_level = reverse_risk_mapping[pred_encoded]

    probabilities = model.predict_proba(X)[0]
    class_names = [reverse_risk_mapping[i] for i in model.classes_]

    prob_dict = {
        class_names[i]: probabilities[i]
        for i in range(len(class_names))
    }

    return pred_level, prob_dict


# ------------------------------------------------------------
# Sidebar navigation
# ------------------------------------------------------------

st.sidebar.title("HealthPulse AI")
page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Overview Dashboard",
        "Risk–Readiness Matrix",
        "Prediction & AI Recommendation",
        "Country Explorer"
    ]
)


# ------------------------------------------------------------
# Home Page
# ------------------------------------------------------------

if page == "Home":

    st.markdown('<div class="main-title">HealthPulse AI</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">An AI-powered early-warning and response system for ASEAN public health risk.</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.write(
        """
        **HealthPulse AI** helps identify which ASEAN countries are likely to face higher public health risk
        and recommends targeted actions for decision-makers.
        
        The system combines:
        
        - Health Risk Index
        - Health System Readiness Score
        - Risk–Readiness Priority Matrix
        - Machine Learning Prediction
        - AI-generated public health recommendations
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Countries Covered", health_df["country"].nunique())

    with col2:
        st.metric("Years Covered", f"{health_df['year'].min()}–{health_df['year'].max()}")

    with col3:
        st.metric("Observations", health_df.shape[0])

    st.markdown("### Solution Logic")

    st.info(
        """
        HealthPulse AI separates public health vulnerability into two parts:
        
        **1. Health Risk:** actual burden from mortality, diseases, and undernutrition.  
        **2. Readiness:** health system capacity using expenditure, immunization, and workforce indicators.  
        
        The system then predicts next-year risk and recommends policy actions.
        """
    )


# ------------------------------------------------------------
# Overview Dashboard
# ------------------------------------------------------------

elif page == "Overview Dashboard":

    st.title("Overview Dashboard")

    selected_year = st.selectbox(
        "Select Year",
        sorted(health_df["year"].unique()),
        index=len(sorted(health_df["year"].unique())) - 1
    )

    year_df = health_df[health_df["year"] == selected_year].copy()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Average Risk Score", round(year_df["health_risk_score"].mean(), 2))

    with col2:
        st.metric("Average Readiness Score", round(year_df["readiness_score"].mean(), 2))

    with col3:
        high_risk_count = (year_df["health_risk_level"] == "High").sum()
        st.metric("High-Risk Countries", high_risk_count)

    with col4:
        emergency_count = (year_df["priority_category"] == "Emergency Priority").sum()
        st.metric("Emergency Priority", emergency_count)

    st.markdown("### Health Risk Scores by Country")

    fig_risk = px.bar(
        year_df.sort_values("health_risk_score", ascending=False),
        x="country",
        y="health_risk_score",
        color="health_risk_level",
        color_discrete_map={
            "Low": "green",
            "Medium": "gold",
            "High": "red"
        },
        title=f"Health Risk Scores Across ASEAN Countries, {selected_year}"
    )

    fig_risk.update_layout(
        xaxis_title="Country",
        yaxis_title="Health Risk Score",
        legend_title="Risk Level"
    )

    st.plotly_chart(fig_risk, use_container_width=True)

    st.markdown("### Readiness Scores by Country")

    fig_readiness = px.bar(
        year_df.sort_values("readiness_score", ascending=True),
        x="country",
        y="readiness_score",
        color="readiness_level",
        color_discrete_map={
            "Low": "red",
            "Medium": "gold",
            "High": "green"
        },
        title=f"Health System Readiness Scores Across ASEAN Countries, {selected_year}"
    )

    fig_readiness.update_layout(
        xaxis_title="Country",
        yaxis_title="Readiness Score",
        legend_title="Readiness Level"
    )

    st.plotly_chart(fig_readiness, use_container_width=True)


# ------------------------------------------------------------
# Risk–Readiness Matrix
# ------------------------------------------------------------

elif page == "Risk–Readiness Matrix":

    st.title("Risk–Readiness Priority Matrix")

    selected_year = st.selectbox(
        "Select Year",
        sorted(health_df["year"].unique()),
        index=len(sorted(health_df["year"].unique())) - 1
    )

    matrix_df = health_df[health_df["year"] == selected_year].copy()

    st.write(
        """
        The Risk–Readiness Matrix identifies countries that have high health burden
        and weak health system capacity.
        """
    )

    fig_matrix = px.scatter(
        matrix_df,
        x="readiness_score",
        y="health_risk_score",
        color="priority_category",
        size="health_risk_score",
        hover_name="country",
        title=f"Risk–Readiness Matrix, {selected_year}"
    )

    fig_matrix.update_layout(
        xaxis_title="Health System Readiness Score",
        yaxis_title="Health Risk Score",
        legend_title="Priority Category"
    )

    st.plotly_chart(fig_matrix, use_container_width=True)

    st.markdown("### Priority Table")

    priority_table = matrix_df[
        [
            "country",
            "health_risk_score",
            "health_risk_level",
            "readiness_score",
            "readiness_level",
            "priority_category"
        ]
    ].sort_values(["health_risk_score", "readiness_score"], ascending=[False, True])

    st.dataframe(priority_table, use_container_width=True)


# ------------------------------------------------------------
# Prediction and AI Recommendation
# ------------------------------------------------------------

elif page == "Prediction & AI Recommendation":

    st.title("Prediction & AI Recommendation")

    st.write(
        """
        Select a country and year. The model will predict the next-year health risk level
        and generate a public health recommendation.
        """
    )

    country = st.selectbox(
        "Select Country",
        sorted(health_df["country"].unique())
    )

    country_df = health_df[health_df["country"] == country].copy()

    year = st.selectbox(
        "Select Year",
        sorted(country_df["year"].unique())
    )

    selected_row = country_df[country_df["year"] == year].copy()

    if selected_row.empty:
        st.warning("No data available for this country-year.")
    else:
        pred_level, prob_dict = generate_prediction(selected_row)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Current Risk Level", selected_row["health_risk_level"].iloc[0])

        with col2:
            st.metric("Current Readiness Level", selected_row["readiness_level"].iloc[0])

        with col3:
            st.metric("Predicted Next-Year Risk", pred_level)

        st.markdown("### Prediction Probabilities")

        prob_df = pd.DataFrame({
            "Risk Level": list(prob_dict.keys()),
            "Probability": list(prob_dict.values())
        })

        fig_prob = px.bar(
            prob_df,
            x="Risk Level",
            y="Probability",
            color="Risk Level",
            color_discrete_map={
                "Low": "green",
                "Medium": "gold",
                "High": "red"
            },
            title="Model Prediction Probability"
        )

        fig_prob.update_layout(yaxis_tickformat=".0%")
        st.plotly_chart(fig_prob, use_container_width=True)

        st.markdown("### AI Recommendation")

        ai_match = ai_output[
            (ai_output["country"] == country) &
            (ai_output["year"] == year)
        ]

        if not ai_match.empty:
            st.text(ai_match["ai_summary"].iloc[0])
        else:
            st.info(
                "AI recommendation is available for the latest prediction year only. "
                "Use the latest year to view pre-generated recommendations."
            )


# ------------------------------------------------------------
# Country Explorer
# ------------------------------------------------------------

elif page == "Country Explorer":

    st.title("Country Explorer")

    country = st.selectbox(
        "Select Country",
        sorted(health_df["country"].unique())
    )

    country_df = health_df[health_df["country"] == country].copy()

    st.markdown(f"### Health Risk and Readiness Trend: {country}")

    fig_trend = px.line(
        country_df,
        x="year",
        y=["health_risk_score", "readiness_score"],
        markers=True,
        title=f"Health Risk and Readiness Scores Over Time: {country}"
    )

    fig_trend.update_layout(
        xaxis_title="Year",
        yaxis_title="Score",
        legend_title="Metric"
    )

    st.plotly_chart(fig_trend, use_container_width=True)

    st.markdown("### Country-Year Data")

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
        use_container_width=True
    )