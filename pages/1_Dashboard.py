import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data/Overall Data.xlsx")

df["Weight"] = pd.to_numeric(
    df["Weight"],
    errors="coerce"
)

st.title("Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Data", len(df))

col2.metric(
    "Stunted",
    len(df[df["Height for Age"] == "Stunted"])
)

col3.metric(
    "Not Stunted",
    len(df[df["Height for Age"] == "Not Stunted"])
)

# Distribusi Gender

st.subheader("Distribusi Gender")

fig, ax = plt.subplots()

df["Gender"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# Distribusi Stunting

st.subheader("Distribusi Stunting")

fig2, ax2 = plt.subplots()

df["Height for Age"].value_counts().plot(
    kind="bar",
    ax=ax2
)

st.pyplot(fig2)

# Histogram Umur

st.subheader("Distribusi Umur")

fig3, ax3 = plt.subplots()

ax3.hist(df["Age (Month)"])

st.pyplot(fig3)