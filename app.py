import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# LOAD DATA
# ===============================
st.title("Dashboard Visualisasi Kuesioner")

uploaded_file = st.file_uploader("Upload file Excel (xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("📌 Data Mentah")
    st.dataframe(df)

    # ===============================
    # PILIH KOLOM PERTANYAAN
    # ===============================
    st.subheader("🔍 Pilih Kolom Pertanyaan")
    kolom = st.selectbox("Pilih kolom yang ingin divisualisasikan:", df.columns)

    # ===============================
    # HITUNG FREKUENSI
    # ===============================
    st.subheader("📊 Frekuensi Jawaban")
    freq = df[kolom].value_counts().reset_index()
    freq.columns = ["Jawaban", "Jumlah"]

    st.write(freq)

    # ===============================
    # BAR CHART
    # ===============================
    fig_bar = px.bar(
        freq,
        x="Jawaban",
        y="Jumlah",
        title=f"Distribusi Jawaban Untuk: {kolom}",
        text="Jumlah"
    )
    st.plotly_chart(fig_bar)

    # ===============================
    # PIE CHART
    # ===============================
    fig_pie = px.pie(
        freq,
        names="Jawaban",
        values="Jumlah",
        title=f"Persentase Jawaban Untuk: {kolom}",
        hole=0.3
    )
    st.plotly_chart(fig_pie)

else:
    st.info("Silakan upload file Excel terlebih dahulu.")
