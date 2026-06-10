import streamlit as st
import pandas as pd
import joblib

model = joblib.load(
    "model/model.pkl"
)

target_encoder = joblib.load(
    "model/target_encoder.pkl"
)

gender_encoder = joblib.load(
    "model/gender_encoder.pkl"
)

st.title("Prediksi Risiko Stunting")

gender = st.selectbox(
    "Jenis Kelamin",
    ["M","F"]
)

age = st.number_input(
    "Umur (bulan)",
    1,
    60
)

weight = st.number_input(
    "Berat Badan (kg)",
    1.0,
    50.0
)

height = st.number_input(
    "Tinggi Badan (cm)",
    30.0,
    150.0
)

if st.button("Prediksi"):

    gender_value = gender_encoder.transform(
        [gender]
    )[0]

    data = pd.DataFrame({
        "Gender":[gender_value],
        "Age (Month)":[age],
        "Weight":[weight],
        "Height":[height]
    })

    pred = model.predict(data)

    prob = model.predict_proba(data)

    hasil = target_encoder.inverse_transform(pred)

    risiko = max(prob[0]) * 100

    if hasil[0] == "Stunted":

        st.error(
            f"Prediksi : {hasil[0]}"
        )

    else:

        st.success(
            f"Prediksi : {hasil[0]}"
        )

    st.write(
        f"Tingkat Keyakinan Model : {risiko:.2f}%"
    )

    st.progress(
        float(risiko/100)
    )