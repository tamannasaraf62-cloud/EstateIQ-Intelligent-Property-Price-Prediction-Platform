
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split

# Page configuration
st.set_page_config(
    page_title="Model Performance",
    page_icon="📊",
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

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #E8EEF8 !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #17365D !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DCE4F0;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: #17365D !important;
}

</style>
""", unsafe_allow_html=True)

# Load dataset and model
df = pd.read_csv("boston_data.csv")
model = joblib.load("best_boston_model.joblib")

# Prepare features and target
X = df.drop(columns=["ID", "medv"])
y = df["medv"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Generate predictions
y_pred = model.predict(X_test)

# Page title
st.title("📊 Model Performance Analysis")

st.write(
    "Analyze and compare the performance of different "
    "Machine Learning regression algorithms."
)

st.divider()

# Best model performance
st.header("🏆 Best Performing Model")

st.subheader("Gradient Boosting Regressor")

col1, col2, col3 = st.columns(3)

col1.metric("R² Score", "92.65%")
col2.metric("MAE", "1.9231")
col3.metric("RMSE", "2.5723")

st.info(
    "Gradient Boosting achieved the highest R² score "
    "among the evaluated models."
)

st.divider()

# Model comparison
st.header("🤖 Model Comparison")

results = pd.DataFrame({
    "Model": [
        "Gradient Boosting",
        "Random Forest",
        "XGBoost",
        "Decision Tree",
        "SVR",
        "KNN"
    ],

    "R2 Score": [
        0.926479,
        0.909045,
        0.893391,
        0.793709,
        0.749218,
        0.559787
    ],

    "MAE": [
        1.923063,
        2.148235,
        2.113951,
        2.893290,
        2.675494,
        3.380133
    ],

    "RMSE": [
        2.572301,
        2.861077,
        3.097517,
        4.308810,
        4.750785,
        6.294316
    ]
})

st.dataframe(
    results,
    use_container_width=True,
    hide_index=True
)

st.divider()

# R2 comparison chart
st.header("📈 R² Score Comparison")

st.bar_chart(
    results,
    x="Model",
    y="R2 Score"
)

st.divider()

# Actual vs Predicted chart
st.header("🎯 Actual vs Predicted House Prices")

fig, ax = plt.subplots(figsize=(9, 5))

ax.scatter(
    y_test,
    y_pred,
    alpha=0.7
)

ax.set_xlabel("Actual House Price ($1000s)")
ax.set_ylabel("Predicted House Price ($1000s)")

ax.set_title("Actual vs Predicted Values")

ax.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

ax.grid(alpha=0.2)

st.pyplot(fig)

plt.close(fig)

st.write("""
**How to understand this chart?**

- Each dot represents one house.
- The X-axis shows the actual house price.
- The Y-axis shows the predicted house price.
- Dots closer to the diagonal line indicate better predictions.
""")

st.divider()

# Model explanation
st.header("📖 Understanding Evaluation Metrics")

with st.expander("What is R² Score?"):
    st.write(
        "R² measures how much variation in house prices "
        "is explained by the model. Higher values generally "
        "indicate better performance."
    )

with st.expander("What is MAE?"):
    st.write(
        "Mean Absolute Error measures the average absolute "
        "difference between actual and predicted prices. "
        "Lower values are better."
    )

with st.expander("What is RMSE?"):
    st.write(
        "Root Mean Squared Error measures prediction errors "
        "and gives greater weight to larger errors. "
        "Lower values are better."
    )

# FEATURE IMPORTANCE

st.divider()

st.header("🔍 Feature Importance")

st.write(
    "Feature importance shows which input features "
    "the trained model relies on most when making predictions."
)

# Get feature importance from Gradient Boosting model
importance = model.feature_importances_

# Create DataFrame
feature_importance = pd.DataFrame({
    "Feature": [
        "indus", "chas", "nox", "rm", "age",
        "dis", "rad", "tax", "ptratio", "lstat"
    ],
    "Importance": importance
})

# Sort in descending order
feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

# Display table
st.subheader("Feature Importance Table")
st.dataframe(feature_importance, use_container_width=True)

# Display chart
st.subheader("Feature Importance Chart")

st.bar_chart(
    feature_importance.set_index("Feature")["Importance"]
)

st.caption(
    "Higher importance means the model relies more on that feature. "
    "Importance does not prove that a feature causes house prices to change."
)

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