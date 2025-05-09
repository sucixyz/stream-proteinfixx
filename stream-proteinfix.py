import streamlit as st
import numpy as np

# Fungsi untuk menghitung protein harian
# Input User
berat = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, step=1.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=220.0, step=1.0)
umur = st.number_input("Umur", min_value=1, max_value=100, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
aktivitas = st.selectbox("Tingkat Aktivitas", [
    "Sedentari (minim aktivitas)",
    "Aktif ringan (olahraga ringan 1-3x/minggu)",
    "Aktif sedang (olahraga sedang 3-5x/minggu)",
    "Sangat aktif (olahraga berat tiap hari)"
])

# Halaman aplikasi Streamlit
def main():
    st.title('Perhitungan Protein Harian')

    # CSS untuk mengubah warna latar belakang, sidebar, dan ukuran font
    background_color = "#A60404"
    font_size = "25px"  # Ukuran font untuk teks biasa
    header_font_size = "40px"  # Ukuran font untuk header
    subheader_font_size = "30px"  # Ukuran font untuk subheader
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {background_color} !important;
            font-size: {font_size} !important;
        }}
        .st-bd {{
            background-color: {background_color} !important;
        }}
        h1 {{
            font-size: {header_font_size} !important;
        }}
        h2 {{
            font-size: {subheader_font_size} !important;
        }}
        </style>
        """, unsafe_allow_html=True)


    # Menambahkan opsi baru di select box
    menu = st.sidebar.selectbox("Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.write('Masukkan data X dan Y dalam bentuk tabel dengan dua kolom.')

# Input User
berat = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, step=1.0)
tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=220.0, step=1.0)
umur = st.number_input("Umur", min_value=1, max_value=100, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
aktivitas = st.selectbox("Tingkat Aktivitas", [
    "Sedentari (minim aktivitas)",
    "Aktif ringan (olahraga ringan 1-3x/minggu)",
    "Aktif sedang (olahraga sedang 3-5x/minggu)",
    "Sangat aktif (olahraga berat tiap hari)"
])

# Fungsi menghitung protein berdasarkan aktivitas
def hitung_protein_aktivitas(berat, aktivitas):
    faktor = {
        "Sedentari (minim aktivitas)": 0.8,
        "Aktif ringan (olahraga ringan 1-3x/minggu)": 1.2,
        "Aktif sedang (olahraga sedang 3-5x/minggu)": 1.5,
        "Sangat aktif (olahraga berat tiap hari)": 2.0
    }
    return round(berat * faktor[aktivitas], 1)

# Fungsi menghitung protein berdasarkan umur & jenis kelamin
def hitung_kebutuhan_protein(umur, berat, jenis_kelamin):
    if umur <= 3:
        kebutuhan_protein = berat * 1.05
    elif umur <= 8:
        kebutuhan_protein = berat * 0.95
    elif umur <= 18:
        kebutuhan_protein = berat * 0.85
    else:
        if jenis_kelamin == "Laki-laki":
            kebutuhan_protein = berat * 0.9
        else:
            kebutuhan_protein = berat * 0.8
    return round(kebutuhan_protein, 2)

# Tombol submit
if st.button("Hitung Kebutuhan Protein"):
    kebutuhan1 = hitung_protein_aktivitas(berat, aktivitas)
    kebutuhan2 = hitung_kebutuhan_protein(umur, berat, jenis_kelamin)

    st.success(f"Kebutuhan protein berdasarkan aktivitas: {kebutuhan1} gram")
    st.success(f"Kebutuhan protein berdasarkan usia & jenis kelamin: {kebutuhan2} gram")

    elif menu=='Perkenalan Kelompok':
        st.subheader('Kelompok 3 (1E-PMIP)')
        st.write('Anggota:')
        st.write('1. Dhika Nurafliansyah (2320517)')
        st.write('2. Herni Khairunisa (2320528)')
        st.write('3. Ibnu Rafif (2320530)')
        st.write('4. Khaira Mutya Arrahman (2320533)')
        st.write('5. Marsya Kaila Avridita Mulyono (2320535)')

    elif menu=='Tentang Aplikasi':
        st.subheader('Tentang Aplikasi')
        st.markdown('<style>.my-gif { width: 500px; height: auto; }</style>', unsafe_allow_html=True)
        st.markdown('<img src="https://jonmgomes.com/wp-content/uploads/2020/05/Comp_1.gif" class="my-gif">', unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        st.write('Aplikasi penentu persamaan linear ini dirancang untuk memudahkan pengguna dalam melakukan perhitungan dalam penentuan persamaan linear dan mengurangi kesalahan penempatan data saat menghitung secara manual. Pengguna dapat memilih menu kalkulator untuk dapat menghitung persamaan regresi linear, nilai slope (b), nilai intersept (a), dan nilai koefisien regresi korelasi (r).')

if _name_ == '_main_':
    main()
