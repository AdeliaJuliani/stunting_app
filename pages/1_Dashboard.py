import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_excel("data/Overall Data.xlsx")

st.title("📊 Dashboard")

col1,col2,col3,col4 = st.columns(4)

with col1:
st.metric(
"Total Data",
f"{len(df):,}"
)

with col2:
st.metric(
"Stunted",
len(df[df["Height for Age"]=="Stunted"])
)

with col3:
st.metric(
"Not Stunted",
len(df[df["Height for Age"]=="Not Stunted"])
)

with col4:
st.metric(
"Gender",
df["Gender"].nunique()
)

st.divider()

left,right = st.columns(2)

with left:

```
st.subheader("Distribusi Status Stunting")

fig, ax = plt.subplots()

df["Height for Age"].value_counts().plot(
    kind="bar",
    ax=ax
)

st.pyplot(fig)
```

with right:

```
st.subheader("Distribusi Gender")

fig2, ax2 = plt.subplots()

df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax2
)

st.pyplot(fig2)
```

st.subheader("Distribusi Umur")

fig3, ax3 = plt.subplots()

ax3.hist(
df["Age (Month)"],
bins=20
)

st.pyplot(fig3)
