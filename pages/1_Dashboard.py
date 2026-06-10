import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dashboard")

df = pd.read_excel("data/Overall Data.xlsx")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Data",
    len(df)
)

col2.metric(
    "Stunted",
    len(df[df["Height for Age"]=="Stunted"])
)

col3.metric(
    "Not Stunted",
    len(df[df["Height for Age"]=="Not Stunted"])
)

col4.metric(
    "Gender",
    df["Gender"].nunique()
)

# ===================================
# Distribusi Stunting
# ===================================

st.subheader("Distribusi Status Stunting")

fig, ax = plt.subplots()

df["Height for Age"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)

# ===================================
# Distribusi Gender
# ===================================

st.subheader("Distribusi Gender")

fig2, ax2 = plt.subplots()

df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)

st.pyplot(fig2)

# ===================================
# Distribusi Umur
# ===================================

st.subheader("Distribusi Umur")

fig3, ax3 = plt.subplots()

ax3.hist(
    df["Age (Month)"],
    bins=20
)

st.pyplot(fig3)