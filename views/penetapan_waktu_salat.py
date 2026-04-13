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
    Awal waktu Zuhur dimulai ketika Matahari telah tergelincir dari garis meridian setelah mencapai titik kulminasi atas (transit).
    Secara astronomis, kondisi ini terjadi ketika Matahari melintasi meridian lokal.
    <br><br>
    Dalam aplikasi Salat_F, waktu Zuhur ditentukan menggunakan fungsi <b>find_discrete</b> dengan memanfaatkan kondisi perubahan azimuth dari sebelum kulminasi ke setelah kulminasi.
    Pada kode, hal ini ditandai ketika nilai azimuth Matahari berubah melewati 180° (after = az > 180), sehingga state berubah menuju kondisi setelah transit.
    <br><br>
    Dengan demikian, waktu Zuhur yang dihasilkan merupakan waktu saat Matahari tepat berada di sekitar meridian.
    Jika pengguna mengaktifkan opsi <i>ihtiyath</i>, maka aplikasi akan menambahkan nilai ihtiyath (dalam menit) pada seluruh hasil jadwal waktu salat sebagai bentuk kehati-hatian.
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
    Awal waktu Maghrib dimulai ketika Matahari terbenam, yaitu saat seluruh piringan Matahari menghilang dari ufuk pengamat. 
    Dalam fiqh, masuknya waktu Maghrib ditandai dengan hilangnya piringan Matahari secara sempurna.
    <br><br>
    Karena Maghrib berpatokan pada terbenamnya piringan Matahari, maka penentuan altitude Matahari saat terbenam perlu mempertimbangkan koreksi astronomis, yaitu:
    <br>
    1) Refraksi atmosfer (R)<br>
    2) Semi diameter Matahari (SD)<br>
    3) Kerendahan ufuk (Dip) akibat elevasi lokasi pengamat
    <br><br>
    Dalam aplikasi Salat_F, tinggi Matahari saat terbenam ditentukan menggunakan rumus:
    <br><br>
    <b>h = −(R + SD + Dip)</b>
    <br><br>
    dengan nilai R = 34' (0,5667°) dan SD = 16' (0,2667°).
    Adapun nilai Dip dihitung menggunakan pendekatan:
    <br><br>
    <b>Dip = 0,0293 × √(elevasi)</b>
    <br><br>
    Elevasi (ketinggian tempat) dimasukkan oleh pengguna dalam satuan meter. 
    Koreksi elevasi menjadi signifikan terutama pada lokasi yang memiliki ketinggian besar seperti daerah pegunungan atau bangunan tinggi.
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

# --- TERBIT & DUHA ---
st.markdown("### Waktu Terbit dan Duha")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Waktu Terbit dalam aplikasi Salat_F ditentukan ketika Matahari mulai muncul dari ufuk timur.
    Untuk mendapatkan hasil yang sesuai dengan ufuk mar’i, aplikasi menggunakan batas altitude yang sama dengan terbenam Matahari, yaitu:
    <br><br>
    h = −(R + SD + Dip)
    <br><br>
    sehingga koreksi refraksi, semi diameter, dan dip horizon juga berlaku pada waktu terbit.
    <br><br>
    Adapun waktu Duha ditentukan ketika Matahari telah berada pada ketinggian:
    <br><br>
    h₀ = 4.5°
    <br><br>
    Nilai ini digunakan sebagai pendekatan praktis yang umum dipakai dalam kajian hisab falak untuk menandai masuknya waktu Duha.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- INFORMASI UMUM ---
st.markdown("## Informasi Umum")
st.markdown(
    """
    <div style="text-align: justify; line-height: 1.8;">
    <ul>
        <li>Hasil perhitungan waktu salat menyesuaikan zona waktu lokasi (timezone) yang dideteksi secara otomatis berdasarkan koordinat lintang dan bujur.</li>
        <li>Aplikasi menggunakan data ephemeris Skyfield (DE421) sehingga perhitungan posisi Matahari dilakukan secara astronomis.</li>
        <li>Fitur <i>ihtiyath</i> bersifat opsional. Jika diaktifkan, nilai ihtiyath akan ditambahkan pada seluruh jadwal waktu salat.</li>
        <li>Waktu Imsak ditampilkan secara otomatis dengan selisih 10 menit sebelum Subuh.</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()


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

