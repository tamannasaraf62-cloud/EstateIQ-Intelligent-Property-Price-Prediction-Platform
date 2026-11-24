import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Boston Home AI",
    page_icon="🏡",
    layout="wide"
)

# Custom CSS

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F4F7FC;
    color: #172B4D;
}

/* Main page headings */
h1, h2, h3, h4, h5, h6 {
    color: #17365D !important;
}

/* Main page text */
.stApp p,
.stApp label,
.stApp span,
.stApp li {
    color: #172B4D !important;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #E8EEF8 !important;
}

/* Sidebar text */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #17365D !important;
}

/* Input fields */
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #172B4D !important;
}

/* Metrics cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DCE4F0;
}

/* Metric text */
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: #17365D !important;
}

</style>
""", unsafe_allow_html=True)


# Hero section
st.title("🏡 Boston Home AI")

st.subheader(
    "Smart House Price Prediction Platform"
)

st.write(
    "An intelligent Machine Learning application "
    "designed to estimate house prices using property features."
)

st.divider()

# Welcome section
st.header("Welcome to Boston Housing Predictor")

st.write("""
Explore an interactive Machine Learning platform
that predicts median house values using historical
Boston Housing data.

Our application uses a trained Gradient Boosting
Regressor to generate house price estimates.
""")

st.info(
    "Use the navigation menu on the left to explore "
    "house price prediction, model performance, "
    "dataset analysis and project information."
)

st.divider()

# Project highlights
st.header("📊 Project Highlights")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Dataset Records", "333")
col2.metric("Input Features", "10")
col3.metric("R² Score", "92.65%")
col4.metric("Best Model", "Gradient Boosting")

st.divider()

# Model performance
st.header("🏆 Best Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric("R² Score", "92.65%")
col2.metric("MAE", "1.9231")
col3.metric("RMSE", "2.5723")

st.write(
    "Gradient Boosting achieved the best R² score "
    "among the evaluated regression models."
)

st.divider()

# Technologies
st.header("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🐍 Python")
    st.write("Programming Language")

with col2:
    st.markdown("### 🤖 Scikit-learn")
    st.write("Machine Learning")

with col3:
    st.markdown("### 🌐 Streamlit")
    st.write("Web Application")

st.divider()

# Project workflow
st.header("🔄 Project Workflow")

st.write("""
**Data Collection → Data Cleaning → EDA → Feature Selection
→ Model Training → Hyperparameter Tuning → Model Evaluation
→ House Price Prediction**
""")

st.divider()

# Footer
st.markdown("---")

st.markdown(
    "<div style='text-align:center; color:#17365D;'>"
    "<h4>Created by Tamanna Saraf</h4>"
    "<p><b>DATA SCIENTIST</b></p>"
    "<p>Boston Home AI | Machine Learning Project</p>"
    "</div>",
    unsafe_allow_html=True
)