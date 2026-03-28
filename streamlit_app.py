import streamlit as st

# ---SETUP PAGE ---

about_page = st.Page(
    page="views/about_me.py",
    title="Tentang Aplikasi",
    icon= ":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/waktu_salat.py",
    title="Perhitungan Waktu Salat",
    icon= ":material/apps:",
)
project_2_page = st.Page(
    page="views/penetapan_waktu_salat.py",
    title="Penetapan Waktu Salat",
    icon= ":material/smart_toy:",
)
# --- NAVIGATION ---
pg = st.navigation(
    {
            "info": [about_page],
            "projects": [project_1_page, project_2_page],
    }
)

pg.run()

# --- SHARE ALL ON PAGE---
st.logo("assets/Logo_Website.png")


st.sidebar.write("© 2026 Fathiyah Zahrah Arifin")
st.sidebar.caption("Mahasiswa Ilmu Falak-UIN Walisongo Semarang")