
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📁",
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

/* Metric card background */
[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DCE4F0;
}

/* Metric numbers */
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] div,
[data-testid="stMetricValue"] span {
    color: #17365D !important;
}

/* Metric labels */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] div,
[data-testid="stMetricLabel"] span {
    color: #344563 !important;
}

</style>
""", unsafe_allow_html=True)


# Load dataset
df = pd.read_csv("boston_data.csv")

# Page title
st.title("📁 Boston Housing Dataset Explorer")

st.write(
    "Explore the historical Boston Housing dataset "
    "used in our Machine Learning project."
)

st.divider()

# Dataset overview
st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", df.shape[0])
col2.metric("Total Columns", df.shape[1])
col3.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)

st.divider()


# Dataset preview
st.header("🔍 Dataset Preview")

st.write("View the first 10 records.")

st.dataframe(
    df.head(10),
    use_container_width=True,
    hide_index=True
)

st.divider()

# Dataset information
st.header("📋 Dataset Information")

st.subheader("Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)


# DATASET COLUMN INFORMATION

st.divider()

st.header("📚 Dataset Column Information")

st.write(
    "The Boston Housing dataset contains 12 columns. "
    "The table below explains each column and its data type."
)

column_info = pd.DataFrame({
    "Column Name": [
        "ID", "indus", "chas", "nox", "rm", "age",
        "dis", "rad", "tax", "ptratio", "lstat", "medv"
    ],
    "Description": [
        "Unique identification number of each record",
        "Proportion of non-retail business land",
        "Charles River proximity (1 = Yes, 0 = No)",
        "Nitrogen oxide concentration",
        "Average number of rooms per dwelling",
        "Proportion of owner-occupied homes built before 1940",
        "Distance to employment centres",
        "Accessibility to radial highways",
        "Property tax rate",
        "Pupil-teacher ratio",
        "Percentage of lower-status population",
        "Median house value (in thousands of USD)"
    ],
    "Data Type": [
        "Integer", "Float", "Integer", "Float",
        "Float", "Float", "Float", "Integer",
        "Float", "Float", "Float", "Float"
    ]
})

st.dataframe(
    column_info,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Note: ID is excluded from model training. "
    "The model uses 10 input features to predict MEDV."
)

st.divider()

# Feature distribution
st.header("📈 Feature Distribution")

numeric_columns = df.select_dtypes(
    include="number"
).columns.tolist()

selected_column = st.selectbox(
    "Select a feature:",
    numeric_columns
)

fig, ax = plt.subplots(figsize=(9, 4))

ax.hist(
    df[selected_column].dropna(),
    bins=20,
    edgecolor="black"
)

ax.set_title(f"Distribution of {selected_column}")
ax.set_xlabel(selected_column)
ax.set_ylabel("Frequency")
ax.grid(alpha=0.2)

st.pyplot(fig)
plt.close(fig)

st.divider()

# House price analysis
st.header("🏡 House Price Distribution")

fig, ax = plt.subplots(figsize=(9, 4))

ax.hist(
    df["medv"],
    bins=20,
    edgecolor="black"
)

ax.set_title("Distribution of Median House Prices")
ax.set_xlabel("House Value ($1000s)")
ax.set_ylabel("Number of Houses")
ax.grid(alpha=0.2)

st.pyplot(fig)
plt.close(fig)

st.info(
    "MEDV represents the median house value "
    "in thousands of dollars."
)

st.divider()


# Feature Correlation Heatmap

st.header("🔗 Feature Correlation")

st.write(
    "This heatmap shows the correlation between different "
    "features in the Boston Housing dataset."
)

correlation = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    center=0,
    square=True,
    cbar=True,
    ax=ax
)

ax.set_title(
    "Correlation Heatmap",
    fontsize=16,
    fontweight="bold",
    pad=15
)

plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

st.pyplot(fig, use_container_width=True)

plt.close(fig)



# Footer
st.divider()

st.markdown("---")

st.markdown(
    "<div style='text-align:center; color:#17365D;'>"
    "<h4>Created by Tamanna Saraf</h4>"
    "<p><b>DATA SCIENTIST</b></p>"
    "<p>Boston Home AI | Machine Learning Project</p>"
    "</div>",
    unsafe_allow_html=True
)