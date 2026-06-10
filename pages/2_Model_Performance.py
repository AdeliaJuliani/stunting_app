import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.title("📈 Evaluasi Model")

metrics = joblib.load(
    "model/metrics.pkl"
)

col1,col2,col3 = st.columns(3)

col1.metric(
    "Accuracy",
    round(metrics["accuracy"],4)
)

col2.metric(
    "Precision",
    round(metrics["precision"],4)
)

col3.metric(
    "Recall",
    round(metrics["recall"],4)
)

col4,col5,col6 = st.columns(3)

col4.metric(
    "F1 Score",
    round(metrics["f1"],4)
)

col5.metric(
    "ROC AUC",
    round(metrics["roc_auc"],4)
)

col6.metric(
    "Cross Validation",
    round(metrics["cv_mean"],4)
)

# ===================================
# Confusion Matrix
# ===================================

st.subheader("Confusion Matrix")

cm = metrics["cm"]

cm_df = pd.DataFrame(
    cm,
    columns=[
        "Pred Not Stunted",
        "Pred Stunted"
    ],
    index=[
        "Actual Not Stunted",
        "Actual Stunted"
    ]
)

st.dataframe(cm_df)

# ===================================
# Feature Importance
# ===================================

if metrics["feature_importance"] is not None:

    st.subheader(
        "Feature Importance"
    )

    features = [
        "Gender",
        "Age",
        "Weight",
        "Height"
    ]

    fig, ax = plt.subplots()

    ax.bar(
        features,
        metrics["feature_importance"]
    )

    st.pyplot(fig)