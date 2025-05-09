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

if st.button("Hitung Titik yang Akan Disampling"):
    def hitung_titik_sampling(diameter, jumlah_lubang):
    if jumlah_lubang == 1:
        posisi = [diameter / 2]
    elif jumlah_lubang == 2:
        posisi = [diameter * 0.25, diameter * 0.75]
    elif jumlah_lubang == 4:
        posisi = [diameter * 0.125, diameter * 0.375, diameter * 0.625, diameter * 0.875]
    else:
        return "Jumlah lubang harus 1, 2, atau 4."
        return posisi

# Contoh input
diameter = float(input("Masukkan diameter cerobong (m): "))
jumlah_lubang = int(input("Masukkan jumlah lubang (1, 2, atau 4): "))
titik = hitung_titik_sampling(diameter, jumlah_lubang)

print("Titik sampling dari ujung nozzle (m):")
for t in titik:
    print(round(t, 3))


        
    

'''  st.success(f"pH: {pH:.2f}")
    st.info(f"pOH: {pOH:.2f}")
    st.warning(f"Sifat larutan: {sifat}")
    st.caption(sifat_desc)
    st.markdown(f"**🔬 Rekomendasi indikator pH:** {indikator}")

    # Visualisasi
    st.subheader("🌈 Visualisasi Skala pH")
    colors = ["#ff0000", "#ff4500", "#ffa500", "#ffff00", "#adff2f", "#00ff00",
              "#00fa9a", "#00ced1", "#1e90ff", "#4169e1", "#0000cd", "#00008b", "#191970", "#4b0082", "#8a2be2"]

    st.markdown("<div style='display: flex; flex-direction: row;'>", unsafe_allow_html=True)
    for i in range(15):
        highlight = "border: 3px solid black;" if int(round(pH)) == i else ""
        st.markdown(
            f"<div style='background-color: {colors[i]}; width: 30px; height: 40px; margin-right: 2px; {highlight}' title='pH {i}'></div>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
    st.caption(f"pH kamu di sekitar angka {round(pH)} pada skala warna di atas.")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")'''
