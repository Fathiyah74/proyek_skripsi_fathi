import streamlit as st

st.title("🕌 Salat_F")
layout="centered"
st.markdown("---")

# Hero content (tetap pakai teks Anda)
st.markdown("""
**Salat_F** merupakan aplikasi berbasis web yang dikembangkan untuk membantu pengguna dalam memperoleh informasi waktu salat berdasarkan perhitungan astronomi. Aplikasi ini memanfaatkan data posisi Matahari sebagai dasar penentuan awal waktu salat, sehingga jadwal yang dihasilkan tidak hanya bersifat perkiraan, tetapi dihitung melalui pendekatan ilmiah yang relevan dengan kajian falak.
""", unsafe_allow_html=True)

st.markdown("""
Pengembangan **Salat_F** dilakukan sebagai bentuk pemanfaatan teknologi digital dalam mendukung kebutuhan ibadah masyarakat, khususnya dalam menyediakan informasi waktu salat yang dapat diakses secara praktis melalui perangkat komputer maupun smartphone. Dengan adanya fitur penentuan lokasi dan zona waktu, aplikasi ini dapat menyesuaikan perhitungan sesuai wilayah pengguna.
""", unsafe_allow_html=True)

st.markdown("""
Melalui penerapan metode komputasi astronomi menggunakan ***library Skyfield*** serta proses pencarian waktu peristiwa Matahari menggunakan fungsi ***find_discrete***, **Salat_F** diharapkan mampu menjadi media pembelajaran sekaligus alat bantu yang berguna dalam memahami konsep perhitungan awal waktu salat secara lebih sistematis.
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    ✨ Fitur Unggulan
    - **Perhitungan Astronomis:** menggunakan ephemeris Skyfield (DE421) dan metode *find_discrete* untuk mendeteksi perubahan waktu salat berdasarkan posisi Matahari.
    - **Berbasis Lokasi:** penentuan koordinat dapat dilakukan melalui klik peta (interaktif) atau input manual (lintang, bujur, dan elevasi).
    - **Penyesuaian Zona Waktu Otomatis:** aplikasi mendeteksi timezone berdasarkan koordinat lokasi.
    - **Edukasi Ilmu Falak:** menyediakan penjelasan ilmiah mengenai dasar astronomis penentuan awal waktu salat.
    
with col2:
    st.image("./assets/Logo_Website.png", width=100)  # Visual Matahari


    st.page_link("views/waktu_salat.py", label="🔍 Cek Waktu Salat", use_container_width=True)

