
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Custom styling

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



# Load model
model = joblib.load("best_boston_model.joblib")

# Header
st.title("🏠 House Price Prediction")
st.write(
    "Estimate the median house value using our "
    "trained Gradient Boosting Machine Learning model."
)

st.divider()

# Sidebar
st.sidebar.title("🏡 Property Details")
st.sidebar.write("Enter all 10 property features.")

indus = st.sidebar.number_input("INDUS", min_value=0.0, value=6.91)
chas = st.sidebar.selectbox("CHAS (Charles River)", [0, 1])
nox = st.sidebar.number_input("NOX", min_value=0.0, value=0.448)
rm = st.sidebar.number_input("RM (Average Rooms)", min_value=0.0, value=6.211)
age = st.sidebar.number_input("AGE", min_value=0.0, value=6.5)
dis = st.sidebar.number_input("DIS", min_value=0.0, value=5.7209)
rad = st.sidebar.number_input("RAD", min_value=0, value=3)
tax = st.sidebar.number_input("TAX", min_value=0, value=233)
ptratio = st.sidebar.number_input("PTRATIO", min_value=0.0, value=17.9)
lstat = st.sidebar.number_input("LSTAT", min_value=0.0, value=7.44)

st.sidebar.divider()

st.sidebar.subheader("💰 Seller's Asking Price")

asking_price = st.sidebar.number_input(
    "Enter Asking Price ($)",
    min_value=0.0,
    value=250000.0,
    step=5000.0
)

st.sidebar.divider()

# Main content
st.header("📋 Prediction Information")

col1, col2 = st.columns(2)

with col1:
    st.info("**Model:** Gradient Boosting Regressor")

with col2:
    st.info("**Input Features:** 10 Property Features")

st.divider()

st.subheader("Generate Your Prediction")


if st.button("🔍 Predict House Price", type="primary"):

    input_data = pd.DataFrame([{
        "indus": indus,
        "chas": chas,
        "nox": nox,
        "rm": rm,
        "age": age,
        "dis": dis,
        "rad": rad,
        "tax": tax,
        "ptratio": ptratio,
        "lstat": lstat
    }])

    # Predict house price
    prediction = model.predict(input_data)[0]

    estimated_price = prediction * 1000

    st.success("Prediction Generated Successfully!")

    # Display estimated house value
    st.subheader("🏆 Estimated House Value")

    st.metric(
        label="Predicted Median House Price",
        value=f"${estimated_price:,.2f}"
    )

    st.write(
        f"Estimated value in thousands of dollars: "
        f"${prediction:,.2f}"
    )

    st.caption(
        "This prediction is an estimate based on historical "
        "Boston Housing data, not a guaranteed market price."
    )

    # House Buying Recommendation
    st.divider()

    st.subheader("🏠 House Buying Recommendation")

    st.write(f"Seller's Asking Price: **${asking_price:,.2f}**")
    st.write(f"Estimated House Value: **${estimated_price:,.2f}**")

    if estimated_price <= 0:
        st.warning("Unable to generate a price comparison.")

    elif asking_price < estimated_price:

        savings = estimated_price - asking_price
        percentage = (savings / estimated_price) * 100

        st.success("✅ GOOD BUYING OPPORTUNITY!")

        st.metric(
            label="Potential Savings",
            value=f"${savings:,.2f}"
        )

        st.write(
            f"The seller is asking {percentage:.2f}% "
            "less than the estimated house value."
        )

        st.write(
            "The asking price is lower than the model's estimated value. "
            "Consider this property after checking its condition and documents."
        )

    elif asking_price == estimated_price:

        st.info("ℹ️ FAIR PRICE")

        st.write(
            "The seller's asking price matches the estimated house value."
        )

    else:

        extra_amount = asking_price - estimated_price
        percentage = (extra_amount / estimated_price) * 100

        st.error("⚠️ PRICE IS ABOVE ESTIMATED VALUE")

        st.write(
            f"The seller is asking ${extra_amount:,.2f} "
            f"({percentage:.2f}%) more than the estimated value."
        )

        st.write(
            "Consider negotiating with the seller before making a decision."
        )

    # Disclaimer
    st.info(
        "Important: This recommendation is based only on the model's "
        "estimated price. A lower price does not guarantee a good investment. "
        "Always check property condition, location, legal documents, "
        "and other expenses before buying."
    )


    prediction = model.predict(input_data)[0]

    st.success("Prediction Generated Successfully!")

    st.subheader("🏆 Estimated House Value")

    st.metric(
        label="Predicted Median House Price",
        value=f"${prediction * 1000:,.2f}"
    )

    st.write(
        f"Estimated value in thousands of dollars: "
        f"${prediction:,.2f}"
    )

    st.caption(
        "This prediction is an estimate based on historical "
        "Boston Housing data, not a guaranteed market price."
    )


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
