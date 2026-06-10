import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

metrics = joblib.load(
    "model/metrics.pkl"
)

st.title("Evaluasi Model")

st.metric(
    "Accuracy",
    round(metrics["accuracy"], 4)
)

st.metric(
    "Precision",
    round(metrics["precision"], 4)
)

st.metric(
    "Recall",
    round(metrics["recall"], 4)
)

st.metric(
    "F1 Score",
    round(metrics["f1"], 4)
)

st.subheader("Confusion Matrix")

cm = metrics["cm"]

cm_df = pd.DataFrame(
    cm,
    columns=["Pred Not Stunted","Pred Stunted"],
    index=["Actual Not Stunted","Actual Stunted"]
)

st.dataframe(cm_df)

st.subheader("Feature Importance")

features = [
    "Gender",
    "Age",
    "Weight",
    "Height"
]

importance = metrics["feature_importance"]

fig, ax = plt.subplots()

ax.bar(
    features,
    importance
)

st.pyplot(fig)