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
st.subheader("Awal Waktu Salat dalam Perspektif Ilmu ", anchor=False)

st.markdown(
    """
    <div style="text-align: justify; line-height: 1.8;">
    Penentuan awal waktu salat dalam aplikasi ***Salat_F*** disusun berdasarkan prinsip-prinsip Ilmu Falak yang menjadikan fenomena harian Matahari sebagai dasar utama dalam penentuan waktu ibadah. 
    Para ulama falak dalam menyusun jadwal waktu salat berangkat dari hadis-hadis Nabi yang menjelaskan bahwa awal waktu salat ditandai oleh perubahan posisi Matahari, seperti tergelincirnya Matahari dari meridian,
    perubahan panjang bayangan, terbenamnya Matahari, hilangnya syafak, serta munculnya fajar.
    <br><br>
    Dengan demikian aplikasi ***Salat_F*** memanfaatkan konsep astronomi praktis untuk menerjemahkan tanda-tanda syar’i tersebut ke dalam bentuk perhitungan yang dapat diterapkan dengan menggunakan fungsi ***find discrete***.
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
    Dalam aplikasi ini digunakan prinsip perhitungan:
    <br><br>
    **cot h = tan |φ – δ| + 1**
    <br><br>
    dengan:<br>
    h = altitude Matahari saat Asar<br>
    φ = lintang tempat<br>
    δ = deklinasi Matahari<br>
    <br><br>
    Dalam implementasi aplikasi, nilai altitude Asar dihitung secara dinamis berdasarkan lintang tempat dan deklinasi Matahari yang diperoleh dari ephemeris (DE).
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- MAGHRIB ---
st.markdown("### Waktu Maghrib")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Waktu Maghrib dimulai saat Matahari terbenam, yaitu ketika seluruh piringan Matahari telah berada di bawah ufuk barat.
    Dalam perhitungan astronomi, fenomena ini dipengaruhi oleh refraksi atmosfer dan diameter Matahari,
    sehingga ketinggian Matahari pada saat terbenam tidak tepat berada di 0°.
    <br><br>
    Secara umum, waktu terbenam Matahari dalam hisab dihitung saat posisi Matahari berada sekitar -1° di bawah ufuk.
    Waktu Maghrib berakhir ketika cahaya merah di langit barat (syafaq) telah hilang.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- ISYA ---
st.markdown("### Waktu Isya")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Waktu Isya dimulai saat hilangnya cahaya merah di langit barat (syafaq ahmar), yang menandakan masuknya malam.
    Dalam astronomi, kondisi ini berkaitan dengan berakhirnya senja astronomi, yaitu ketika Matahari berada pada posisi tertentu di bawah ufuk.
    <br><br>
    Di Indonesia, standar yang umum digunakan adalah ketika Matahari berada sekitar -18° di bawah ufuk.
    Perbedaan standar sudut dapat menyebabkan perbedaan hasil beberapa menit antar metode hisab.
    Waktu Isya berlangsung hingga pertengahan malam.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- SUBUH ---
st.markdown("### Waktu Subuh")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Waktu Subuh dimulai sejak terbitnya fajar shadiq, yaitu cahaya putih yang muncul secara horizontal di ufuk timur sebelum Matahari terbit.
    Dalam astronomi, peristiwa ini ditentukan berdasarkan posisi Matahari yang berada beberapa derajat di bawah ufuk timur.
    <br><br>
    Dalam praktik di Indonesia, awal Subuh umumnya menggunakan standar Matahari sekitar -20° di bawah ufuk.
    Nilai ini dapat berbeda antar negara atau lembaga falak. Waktu Subuh berakhir saat Matahari mulai terbit.
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

