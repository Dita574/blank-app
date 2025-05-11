import streamlit as st
import math

st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

# Title
st.title("📏Kalkulator Titik Sampling Pada Emisi Tidak Bergerak💨")
st.header(":blue[Metode 1]")

# Description
st.write("""
Kalkulator ini membantu menghitung titik sampling yang diperlukan pada cerobong dengan metode isokinetik
""")

# Sidebar for input
with st.sidebar:
    st.header("Input Parameter")
    namber = st.number_input(
    "DIameter Cerobong", value=None, placeholder="Type a number...")
    nimber = st.number_input(
    "Panjang Nipple", value=None, placeholder="Type a number...")
    number = st.number_input(
    "Banyaknya Titik Lintas", value=None, placeholder="Type a number...")
    nember = st.number_input(
    "Upstream", value=None, placeholder="Type a number...")
    nomber = st.number_input(
    "Downstream", value=None, placeholder="Type a number...")

# Divider
st.markdown("---")

if st.button("Hitung Titik Sampling"):
    A = upstream / diameter  # dalam satuan D
    B = downstream / diameter

    # Logika penentuan jumlah titik dari grafik
    if A >= 2.5 and B >= 7:
        titik = 12
    elif A >= 2 and B >= 5:
        titik = 16
    elif A >= 1.5 and B >= 4:
        titik = 20
    elif A >= 1 and B >= 3:
        titik = 24
    else:
        titik = 24  # kondisi terburuk

    st.success(f"Jumlah titik sampling minimum: {titik} titik")

    st.subheader("📌 Konfigurasi Lubang Sampling")
    if lubang == 1:
        st.info("Semua titik diambil dari satu sisi.")
    elif lubang == 2:
        st.info("Titik diambil dari dua sisi yang berseberangan (180°).")
    else:
        st.info("Titik diambil dari empat sisi
                
st.markdown("---")
st.caption("📘 Perhitungan berdasarkan pendekatan grafik standar EPA Method 1.")
                
