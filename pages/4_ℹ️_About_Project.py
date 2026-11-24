
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
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

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #17365D !important;
}

/* Main text */
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
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #17365D !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    padding: 20px !important;
    border-radius: 12px !important;
    border: 1px solid #DCE4F0 !important;
}

/* Metric numbers */
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div,
[data-testid="stMetricValue"] span {
    color: #17365D !important;
    font-weight: 700 !important;
}

/* Metric labels */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] div,
[data-testid="stMetricLabel"] span {
    color: #344563 !important;
}

/* Metric delta */
[data-testid="stMetricDelta"] {
    color: #2563EB !important;
}

</style>
""", unsafe_allow_html=True)


# Page title
st.title("ℹ️ About Boston Home AI")

st.subheader(
    "Machine Learning Based House Price Prediction"
)

st.write(
    "An intelligent application that estimates "
    "median house values using property-related features."
)

st.divider()

# Introduction
st.header("📌 Project Introduction")

st.write("""
Boston Home AI is a Machine Learning regression project.

The objective is to predict median house values based on
different property characteristics.

The application uses historical Boston Housing data
and a trained Gradient Boosting Regressor.
""")

st.divider()

# Problem statement
st.header("🎯 Problem Statement")

st.write("""
House prices depend on several factors, such as the number
of rooms, property tax, location-related characteristics
and other housing conditions.

This project uses Machine Learning algorithms to learn
patterns from historical housing data and estimate
house values.
""")

st.divider()

# Dataset
st.header("📊 Dataset Description")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", "333")
col2.metric("Input Features", "10")
col3.metric("Total Columns", "12")

st.write("""
**Dataset Features:**

| Feature | Description |
|---|---|
| ID | Record identifier |
| INDUS | Non-retail business land proportion |
| CHAS | Charles River boundary indicator |
| NOX | Nitric oxide concentration |
| RM | Average number of rooms |
| AGE | Older owner-occupied units proportion |
| DIS | Distance to employment centres |
| RAD | Highway accessibility index |
| TAX | Property tax rate |
| PTRATIO | Pupil-teacher ratio |
| LSTAT | Lower-status population percentage |
| MEDV | Median house value ($1000s) |

ID is excluded from model training.
""")

st.divider()

# Algorithms
st.header("🤖 Machine Learning Algorithms")

st.write("""
Seven regression algorithms were initially evaluated:

1. Linear Regression
2. K-Nearest Neighbors (KNN)
3. Support Vector Regression (SVR)
4. Decision Tree Regressor
5. Random Forest Regressor
6. Gradient Boosting Regressor
7. XGBoost Regressor

Hyperparameter tuning was performed to improve model performance.
""")

st.divider()

# Best model
st.header("🏆 Best Performing Model")

st.success("Gradient Boosting Regressor")

col1, col2, col3 = st.columns(3)

col1.metric("R² Score", "92.65%")
col2.metric("MAE", "1.9231")
col3.metric("RMSE", "2.5723")

st.write("""
Gradient Boosting achieved the best R² score among
the evaluated models on the test dataset.

The R² score indicates that approximately 92.65%
of the variation in house values was explained
by the model on this test split.
""")

st.divider()

# Technologies
st.header("🛠️ Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🐍 Python")
    st.write("Programming language")

    st.markdown("### 🐼 Pandas and NumPy")
    st.write("Data handling and numerical operations")

    st.markdown("### 📈 Matplotlib")
    st.write("Data visualization")

with col2:
    st.markdown("### 🤖 Scikit-learn")
    st.write("Machine Learning and evaluation")

    st.markdown("### ⚡ XGBoost")
    st.write("Gradient boosting algorithm")

    st.markdown("### 🌐 Streamlit")
    st.write("Web application development")

st.divider()

# Workflow
st.header("🔄 Project Workflow")

steps = [
    "Data Collection",
    "Data Cleaning",
    "Exploratory Data Analysis",
    "Feature Selection",
    "Model Training",
    "Hyperparameter Tuning",
    "Model Evaluation",
    "Best Model Selection",
    "House Price Prediction",
    "Web Application Development"
]

for index, step in enumerate(steps, start=1):
    st.write(f"**{index}.** {step}")

st.divider()

# Disclaimer
st.header("📝 Disclaimer")

st.info("""
This project is developed for educational and
Machine Learning demonstration purposes.

Predictions are estimates based on historical data
and should not be treated as actual market valuations.
""")

st.divider()


# Footer
# DATASET LIMITATIONS

st.divider()

st.header("⚠️ Dataset Limitations")

limitations = [
    "Historical Dataset: The dataset contains old housing information and does not represent today's real estate market.",

    "Limited Records: This project uses 333 records, a subset of the commonly documented original 506-record dataset.",

    "Limited Features: The model uses only 10 input features.",

    "Geographical Limitation: The dataset represents historical Boston-area housing information.",

    "Prediction Uncertainty: Predicted prices are estimates and may differ from actual selling prices.",

    "Buying Recommendation: A lower asking price does not guarantee a good investment. Always check property condition, location, and legal documents."
]

for i, limitation in enumerate(limitations, 1):
    st.markdown(f"**{i}.** {limitation}")

st.markdown("---")

st.markdown(
    "<div style='text-align:center; color:#17365D;'>"
    "<h4>Created by Tamanna Saraf</h4>"
    "<p><b>DATA SCIENTIST</b></p>"
    "<p>Boston Home AI | Machine Learning Project</p>"
    "</div>",
    unsafe_allow_html=True
)