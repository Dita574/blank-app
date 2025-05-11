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

if st.button("Hitung"):
    # Syarat lurusan
    syarat_up = 8 * D
    syarat_down = 2 * D

    hasil_up = "Memenuhi" if upstream >= syarat_up else "Tidak Memenuhi"
    hasil_down = "Memenuhi" if downstream >= syarat_down else "Tidak Memenuhi"

    st.subheader("Hasil Evaluasi Lurusan:")
    st.write(f"• Panjang gangguan hulu: {upstream} m → {hasil_up} (min: {syarat_up:.2f} m)")
    st.write(f"• Panjang gangguan hilir: {downstream} m → {hasil_down} (min: {syarat_down:.2f} m)")

    st.subheader("Konfigurasi Titik Sampling:")
    if D < 0.3:
        titik = 6
    elif D < 1:
        titik = 12
    else: 
        titik = 24 #Kondisi terburuk

st.write(f"• Diameter cerobong: {D} m → Gunakan {titik} titik sampling")
    st.write(f"• Jumlah lubang sampling: {n_lubang}")

    if n_lubang == 1:
        st.info("Ambil semua titik dari 1 sisi.")
    elif n_lubang == 2:
        st.info("Ambil titik dari sisi berlawanan (180°).")
    elif n_lubang == 4:
        st.info("Ambil titik dari 4 sisi (90° per lubang).")
    



