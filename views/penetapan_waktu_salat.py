import streamlit as st

# --- HERO SELECTED ---
st.title("Salat_F", anchor=False)
st.write(
        "Perhitungan Awal Waktu Salat dengan Mengunakan Fungsi ***Find_Discrete*** pada ***Package Skyfield***"
    )
st.write("اِنَّ الصَّلٰوةَ كَانَتْ عَلَى الْمُؤْمِنِيْنَ كِتٰبًا مَّوْقُوْتًا ")
layout="centered"
# --- BATASAN WAKTU SALAT SECARA FIQH DAN ASTRONOMI ---
st.write("\n")
st.subheader("Awal Waktu Salat dalam Perspektif Ilmu Falak ", anchor=False)

st.markdown(
    """
    <div style="text-align: justify; line-height: 1.8;">
    Penentuan awal waktu salat dalam aplikasi Salat_F disusun berdasarkan prinsip-prinsip Ilmu Falak yang menjadikan fenomena harian Matahari sebagai dasar utama dalam penentuan waktu ibadah. 
    Para ulama falak dalam menyusun jadwal waktu salat berangkat dari hadis-hadis Nabi yang menjelaskan bahwa awal waktu salat ditandai oleh perubahan posisi Matahari, seperti tergelincirnya Matahari dari meridian,
    perubahan panjang bayangan, terbenamnya Matahari, hilangnya syafak, serta munculnya fajar.
    <br><br>
    Dengan demikian aplikasi Salat_F memanfaatkan konsep astronomi praktis untuk menerjemahkan tanda-tanda syar’i tersebut ke dalam bentuk perhitungan yang dapat diterapkan dengan menggunakan fungsi find discrete.
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

# --- ZUHUR ---
st.markdown("### Awal Waktu Zuhur")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Awal waktu Zuhur dimulai ketika Matahari telah tergelincir dari garis meridian setelah mencapai titik kulminasi atas (transit). Dalam hisab falak klasik, waktu transit dapat ditentukan menggunakan rumus:
    <br><br>
    WH = 12 – e + (λʷ – λ) / 15
    <br><br>
    Namun dalam aplikasi ini, penentuan waktu Zuhur dilakukan dengan bantuan metode find_discrete. 
    Aplikasi mencari peristiwa transit Matahari berdasarkan status ketika Matahari tepat melintasi meridian. 
    Waktu yang dihasilkan merupakan waktu ketika pusat piringan Matahari berimpit dengan meridian.
    <br><br>
    Untuk memastikan bahwa Matahari telah benar-benar tergelincir sebagaimana kehati-hatian dalam fiqh,
    maka aplikasi menambahkan nilai ihtiyat sebesar 2 menit setelah transit sebagai penetapan masuk waktu Zuhur.
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

# --- ASAR ---
st.markdown("### Awal Waktu Asar")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Awal waktu Asar ditandai ketika panjang bayangan suatu benda sama dengan satu kali tinggi benda ditambah panjang bayangan ketika transit (menurut jumhur ulama). 
    Secara astronomis, kondisi tersebut diterjemahkan dalam bentuk sudut ketinggian Matahari.
    <br><br>
    Dalam aplikasi ini digunakan prinsip perhitungan:<br>
    cot h = tan |φ – δ| + 1<br>
    dengan:<br>
    h = altitude Matahari saat Asar<br>
    φ = lintang tempat<br>
    δ = deklinasi Matahari
    <br><br>
    Dalam implementasi aplikasi, nilai altitude Asar dihitung secara dinamis berdasarkan lintang tempat dan deklinasi Matahari yang diperoleh dari ephemeris (DE).
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- MAGHRIB ---
st.markdown("### Awal Waktu Maghrib")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Awal waktu Maghrib dimulai ketika Matahari terbenam, yaitu saat piringan Matahari menghilang dari ufuk pengamat. Dalam fiqh, Maghrib ditandai dengan hilangnya seluruh piringan Matahari.
    <br><br>
    Karena Maghrib berpatokan langsung pada piringan Matahari, maka perhitungan altitude Matahari pada saat terbenam harus mempertimbangkan koreksi astronomis, yaitu:<br>
    1. Refraksi atmosfer<br>
    2. Semi diameter Matahari<br>
    3. Kerendahan ufuk akibat elevasi lokasi<br>
    Dengan demikian, ketinggian Matahari yang digunakan adalah tinggi ufuk mar’i (ufuk yang tampak). 
    Dalam aplikasi ini digunakan pendekatan praktis yang lazim dipakai di Indonesia, yaitu dengan menetapkan altitude Matahari:
    <br><br>
    h₀ = -1°
    <br><br>
    Menurut Thomas Djamaluddin, nilai -1° telah mencukupi untuk perhitungan awal waktu Maghrib di wilayah Indonesia. 
    Koreksi tinggi tempat menjadi signifikan hanya pada lokasi yang sangat tinggi seperti puncak gunung atau gedung tinggi yang memiliki ufuk langsung ke laut.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- ISYA ---
st.markdown("### Awal Waktu Isya")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Awal waktu Isya dimulai ketika hilangnya cahaya syafak (mega merah) dan berakhir saat masuk waktu Subuh. 
    Secara astronomis, hilangnya syafak terjadi karena posisi Matahari semakin jauh berada di bawah ufuk sehingga hamburan cahaya senja tidak lagi terlihat.
    <br><br>
    Dalam aplikasi ini, awal waktu Isya ditetapkan ketika Matahari berada pada ketinggian:<br>
    h₀ = -18°
    <br><br>
    Nilai tersebut merupakan standar yang banyak digunakan oleh Kementerian Agama Republik Indonesia.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- SUBUH ---
st.markdown("### Awal Waktu Subuh")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Awal waktu Subuh dimulai ketika muncul fajar ṣādiq dan berakhir ketika Matahari terbit. 
    Secara astronomis, fajar ṣādiq terjadi karena adanya hamburan cahaya Matahari di atmosfer ketika Matahari masih berada di bawah ufuk timur.
    <br><br>
    Dalam aplikasi ini, awal waktu Subuh mengikuti standar yang digunakan oleh Kementerian Agama Republik Indonesia, yaitu ketika Matahari berada pada ketinggian:<br>
    h₀ = -20°
    <br><br>
    Nilai ini dipilih karena masih menjadi rujukan resmi dalam penyusunan jadwal waktu salat di Indonesia.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# --- KONTAK DEVELOPER ---
st.markdown("### 📩 Hubungi Developer")
st.markdown(
    """
    Jika terdapat saran, kritik, atau pertanyaan mengenai aplikasi Salat_F, silakan hubungi developer melalui tautan berikut:
    
    - 📧 Email: fathiyazahrah7@gmail.com 
    - 💬 Instagram: [DM:Fathiyah Zahrah Arifin](https://www.instagram.com/fathiyahzahrah_?igsh=MTZ0cjJkYTZzaWw3OA==)  

    """,
    unsafe_allow_html=True
)

