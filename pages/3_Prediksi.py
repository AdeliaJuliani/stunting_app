import streamlit as st
import pandas as pd
import joblib

st.title("🔍 Prediksi Risiko Stunting")

model = joblib.load(
    "model/model.pkl"
)

target_encoder = joblib.load(
    "model/target_encoder.pkl"
)

gender_encoder = joblib.load(
    "model/gender_encoder.pkl"
)

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
    40.0
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

    prediction = model.predict(data)

    probability = model.predict_proba(data)

    result = target_encoder.inverse_transform(
        prediction
    )[0]

    confidence = (
        max(probability[0]) * 100
    )

    st.subheader("Hasil Prediksi")

    if result == "Stunted":

        st.error(
            f"⚠️ {result}"
        )

    else:

        st.success(
            f"✅ {result}"
        )

    st.write(
        f"Tingkat Keyakinan Model : {confidence:.2f}%"
    )

    st.progress(
        confidence / 100
    )

    # Interpretasi

    st.subheader(
        "Interpretasi"
    )

    if result == "Stunted":

        st.warning("""
        Balita memiliki indikasi risiko stunting.
        
        Disarankan:
        - Konsultasi ke tenaga kesehatan
        - Monitoring pertumbuhan rutin
        - Perbaikan asupan gizi
        """)

    else:

        st.info("""
        Pertumbuhan balita berada pada kondisi normal berdasarkan model prediksi.
        Tetap lakukan pemantauan rutin.
        """)