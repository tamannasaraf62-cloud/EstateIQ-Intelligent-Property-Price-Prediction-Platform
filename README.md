# 🏠 EstateIQ – House Price Prediction Using Machine Learning

EstateIQ is a Machine Learning-based web application that predicts median house values using historical Boston Housing data. It allows users to enter property details, explore the dataset, and view model performance through an interactive Streamlit dashboard.

## 🎯 Project Overview

The project uses regression algorithms to analyze housing features and estimate median house values. It covers the complete Machine Learning workflow, from data analysis and model training to evaluation and web application development.

## 📊 Dataset

- **Records:** 333
- **Columns:** 12
- **Input Features:** 10
- **Target Variable:** MEDV (Median House Value)
- **Missing Values:** 0

The dataset contains housing and neighbourhood-related information, including number of rooms, pollution levels, property tax, highway accessibility, and other factors.

*Note: This project uses a historical subset of the Boston Housing dataset and is intended for educational purposes, not current real-estate valuation.*

## 🤖 Machine Learning Models

The following regression algorithms were implemented and evaluated:

- Linear Regression
- K-Nearest Neighbors (KNN)
- Support Vector Regression (SVR)
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

Hyperparameter tuning was performed using RandomizedSearchCV with 5-fold cross-validation.

## 🏆 Best Model – Gradient Boosting

| Evaluation Metric | Result |
|---|---:|
| R² Score | 92.65% |
| MAE | 1.9231 |
| RMSE | 2.5723 |

Gradient Boosting achieved the best overall performance on the test dataset.

*MAE and RMSE are expressed in thousands of US dollars.*

## 🌐 Streamlit Application Features

- Interactive house price prediction
- Seller asking-price comparison
- Model performance comparison
- Feature importance visualization
- Dataset exploration and statistical summary
- Correlation heatmap
- Project information and limitations

## 🛠️ Technologies Used

Python · Pandas · NumPy · Scikit-learn · XGBoost · Matplotlib · Seaborn · Streamlit · Jupyter Notebook · Joblib

## 📂 Project Structure

```text
EstateIQ/
│
├── app.py
├── pages/
├── boston_data.csv
├── best_boston_model.joblib
├── requirements.txt
├── 01_Boston_EDA.ipynb
├── 02_Model_Training_Evaluation.ipynb
└── 03_House_Price_Prediction.ipynb
```

## 🚀 Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app.py
```

## 👩‍💻 Created By

**Tamanna Saraf**  
Data Scientist

---

*EstateIQ – Exploring House Price Prediction Through Machine Learning.*
