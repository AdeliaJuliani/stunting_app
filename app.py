import streamlit as st

st.set_page_config(
    page_title="Prediksi Stunting Balita",
    page_icon="👶",
    layout="wide"
)

st.title("👶 Sistem Prediksi Risiko Stunting Balita")

st.markdown("""
Aplikasi ini menggunakan algoritma Random Forest untuk memprediksi risiko stunting berdasarkan data antropometri balita.

### Menu:
- Dashboard
- Evaluasi Model
- Prediksi
""")