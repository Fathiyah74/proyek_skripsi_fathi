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
st.subheader("Batasan Waktu Salat", anchor=False)

st.markdown(
    """
    <div style="text-align: justify; line-height: 1.8;">
    Penentuan awal waktu salat dalam aplikasi ini mengacu pada dua pendekatan utama, yaitu pendekatan fiqh dan pendekatan astronomi.
    Dalam fiqh, awal waktu salat ditentukan berdasarkan tanda-tanda alam seperti tergelincirnya Matahari, panjang bayangan, terbenamnya Matahari,
    serta munculnya fajar. Sedangkan dalam astronomi, tanda-tanda tersebut diterjemahkan menjadi parameter posisi Matahari terhadap ufuk,
    khususnya nilai ketinggian (altitude) Matahari dalam satuan derajat.
    <br><br>
    Karena terdapat perbedaan pendapat ulama dan lembaga hisab dalam menetapkan batas sudut Matahari, maka nilai yang digunakan dalam aplikasi ini
    mengikuti standar yang umum digunakan di Indonesia berpatokan pada perhitungan Kementerian Agama RI.
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

# --- ZUHUR ---
st.markdown("### Waktu Zuhur")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Waktu Zuhur dimulai ketika Matahari tergelincir dari titik kulminasi (zawal), yaitu saat Matahari melewati posisi tertinggi di langit
    dan mulai bergerak ke arah barat. Secara astronomis, peristiwa ini berkaitan dengan transit Matahari pada meridian lokal.
    <br><br>
    Dalam praktik hisab, waktu Zuhur sering diberikan tambahan beberapa menit sebagai bentuk kehati-hatian (ihtiyath) agar benar-benar masuk waktu.
    Waktu Zuhur berakhir ketika panjang bayangan suatu benda sama dengan tinggi bendanya, ditambah panjang bayangan saat kulminasi.
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

# --- ASAR ---
st.markdown("### Waktu Asar")
st.markdown(
    """ 
    <div style="text-align: justify; line-height: 1.8;">
    Waktu Asar dimulai ketika panjang bayangan suatu benda sama dengan tinggi bendanya, ditambah bayangan saat kulminasi (menurut jumhur ulama).
    Perhitungan ini dipengaruhi oleh lintang tempat dan deklinasi Matahari, sehingga waktu Asar dapat berubah-ubah sepanjang tahun.
    <br><br>
    Dalam astronomi, kondisi tersebut dapat dihitung berdasarkan sudut elevasi Matahari yang menyebabkan bayangan mencapai nilai tertentu.
    Beberapa mazhab memiliki perbedaan dalam menentukan batas bayangan, sehingga hasil hisab dapat berbeda tergantung metode yang digunakan.
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

