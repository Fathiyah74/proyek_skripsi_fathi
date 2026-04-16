import os
import time
import streamlit as st
import folium
import numpy as np
import requests

from streamlit_folium import st_folium
from skyfield.api import load, wgs84
from skyfield.searchlib import find_discrete

from datetime import datetime, timedelta
from pytz import timezone
from timezonefinder import TimezoneFinder

from geopy.geocoders import Nominatim
from streamlit_js_eval import get_geolocation


# =============================
# PAGE CONFIG
# =============================

st.set_page_config(
    page_title="Salat_F — Waktu Salat Astronomis",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =============================
# STYLE — tema-adaptive (light & dark)
# Semua warna pakai CSS var Streamlit agar ikut tema pengguna.
# =============================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 2rem 3rem 4rem 3rem;
    max-width: 1200px;
}

/* ── Hero ── */
.hero-wrap {
    text-align: center;
    padding: 2.5rem 0 1.8rem 0;
    border-bottom: 1px solid rgba(128,128,128,0.18);
    margin-bottom: 2rem;
}
.hero-arabic {
    font-family: 'Amiri', serif;
    font-size: 2.8rem;
    color: #b8922a;
    letter-spacing: 0.04em;
    line-height: 1.2;
    margin-bottom: 0.3rem;
}
.hero-title {
    font-size: 0.88rem;
    font-weight: 400;
    letter-spacing: 0.32em;
    text-transform: uppercase;
    opacity: 0.55;
}

/* ── Section label ── */
.section-label {
    font-size: 0.67rem;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    opacity: 0.55;
    margin: 1.5rem 0 0.55rem 0;
    border-bottom: 1px solid rgba(128,128,128,0.15);
    padding-bottom: 0.38rem;
}

/* ── Gold divider ── */
.gold-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, rgba(184,146,42,0.32), transparent);
    margin: 1.4rem 0;
}

/* ── Location card ── */
.loc-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128,128,128,0.2);
    border-radius: 12px;
    padding: 1.1rem 1.4rem;
    margin-bottom: 1.4rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.loc-dot {
    flex-shrink: 0;
    width: 9px; height: 9px;
    background: #b8922a;
    border-radius: 50%;
    box-shadow: 0 0 7px rgba(184,146,42,0.5);
}
.loc-name {
    font-size: 0.92rem;
    font-weight: 500;
}
.loc-meta {
    font-size: 0.76rem;
    margin-top: 0.12rem;
    opacity: 0.6;
}

/* ── Prayer card ── */
.prayer-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128,128,128,0.2);
    border-radius: 12px;
    padding: 1.1rem 0.9rem;
    text-align: center;
    transition: border-color 0.2s, transform 0.18s;
    margin-bottom: 0.1rem;
}
.prayer-card:hover {
    border-color: rgba(184,146,42,0.38);
    transform: translateY(-2px);
}
.prayer-card.active {
    border-color: #b8922a;
    box-shadow: 0 0 18px rgba(184,146,42,0.14);
}
.prayer-label {
    font-size: 0.64rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.5;
    margin-bottom: 0.45rem;
}
.prayer-time-hm {
    font-size: 1.8rem;
    font-weight: 600;
    letter-spacing: -0.02em;
    line-height: 1;
}
.prayer-time-sec {
    font-size: 1rem;
    font-weight: 400;
    opacity: 0.5;
}
.prayer-card.active .prayer-time-hm { color: #b8922a; }
.prayer-card.active .prayer-time-sec { color: #b8922a; opacity: 0.65; }
.prayer-card.missing .prayer-time-hm,
.prayer-card.missing .prayer-time-sec { opacity: 0.25; }
.prayer-note {
    font-size: 0.63rem;
    margin-top: 0.35rem;
    opacity: 0.45;
    font-style: italic;
}

/* ── Next prayer banner ── */
.next-prayer {
    background: var(--secondary-background-color);
    border: 1px solid rgba(184,146,42,0.32);
    border-radius: 12px;
    padding: 1rem 1.4rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.next-label {
    font-size: 0.66rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    opacity: 0.5;
}
.next-name { font-size: 1.05rem; font-weight: 600; color: #b8922a; margin-top: 0.1rem; }
.next-countdown { font-size: 1.5rem; font-weight: 300; letter-spacing: -0.01em; }

/* ── Ihtiyath badge ── */
.ihtiyath-badge {
    display: inline-block;
    background: rgba(184,146,42,0.1);
    border: 1px solid rgba(184,146,42,0.3);
    color: #b8922a;
    border-radius: 20px;
    padding: 0.14rem 0.72rem;
    font-size: 0.69rem;
    font-weight: 500;
    margin-left: 0.4rem;
    vertical-align: middle;
}

/* ── Buttons ── */
.stButton > button {
    background: #b8922a !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.04em !important;
    transition: opacity 0.18s !important;
}
.stButton > button:hover { opacity: 0.82 !important; }

/* ── Folium iframe ── */
iframe { border-radius: 12px !important; border: 1px solid rgba(128,128,128,0.2) !important; }

/* ── Footer ── */
.footer-note {
    font-size: 0.7rem;
    text-align: center;
    line-height: 1.9;
    opacity: 0.45;
}
</style>
""", unsafe_allow_html=True)


# ── Hero ──
st.markdown("""
<div class="hero-wrap">
    <div class="hero-arabic">وَأَقِيمُوا الصَّلَاةَ</div>
    <div class="hero-title">Salat_F &nbsp;·&nbsp; Waktu Salat Astronomis</div>
</div>
""", unsafe_allow_html=True)


# =============================
# LOAD EPHEMERIS
# =============================

@st.cache_resource(show_spinner=False)
def load_ephemeris():
    ts = load.timescale()
    if not os.path.exists("de421.bsp"):
        with st.spinner("Mengunduh data ephemeris (sekali saja, ~17MB)..."):
            eph = load("de421.bsp")
    else:
        eph = load("de421.bsp")
    return ts, eph["earth"], eph["sun"]

ts, earth, sun = load_ephemeris()


# =============================
# HELPERS
# =============================

@st.cache_resource(show_spinner=False)
def get_geolocator():
    return Nominatim(user_agent="salat_f_app_v2", timeout=6)


@st.cache_data(ttl=86400, show_spinner=False)
def get_location_name(lat: float, lon: float) -> str:
    geolocator = get_geolocator()
    try:
        time.sleep(0.3)
        location = geolocator.reverse((lat, lon), language="id")
        if location:
            return location.address
    except Exception as e:
        st.toast(f"Geocode gagal: {e}", icon="⚠️")
    return f"{lat:.4f}, {lon:.4f}"


@st.cache_data(ttl=86400, show_spinner=False)
def search_location(query: str):
    geolocator = get_geolocator()
    try:
        time.sleep(0.3)
        location = geolocator.geocode(query)
        if location:
            return location.latitude, location.longitude, location.address
    except Exception as e:
        st.toast(f"Pencarian gagal: {e}", icon="⚠️")
    return None, None, None


@st.cache_data(ttl=86400, show_spinner=False)
def get_timezone(lat: float, lon: float) -> str:
    tf = TimezoneFinder()
    tz_name = tf.timezone_at(lat=lat, lng=lon)
    return tz_name if tz_name else "UTC"


@st.cache_data(ttl=86400, show_spinner=False)
def get_elevation(lat: float, lon: float) -> float:
    try:
        url = f"https://api.opentopodata.org/v1/srtm90m?locations={lat},{lon}"
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        data = r.json()
        elev = data["results"][0]["elevation"]
        return float(elev) if elev is not None else 0.0
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return 0.0


# =============================
# SESSION STATE
# =============================

DEFAULT_LOC = {
    "lat": -6.9747,
    "lon": 110.4229,
    "city": "Semarang, Jawa Tengah",
    "tz": "Asia/Jakarta",
    "alt": 10.0,
}

if "location" not in st.session_state:
    st.session_state.location = DEFAULT_LOC.copy()


# =============================
# KONSTANTA IHTIYATH
# =============================

# Waktu yang ihtiyath-nya DIKURANGI (dimajukan/lebih awal):
#   Terbit : merupakan batas akhir Subuh, memajukan Terbit memberi
#             sinyal lebih awal bahwa waktu Subuh hampir habis.
#   Duha   : juga informasi astronomis; dimajukan agar lebih konservatif.
IHTIYATH_KURANG = {"Terbit", "Duha"}


# =============================
# PERHITUNGAN WAKTU SALAT
# =============================

def hitung_salat(lat: float, lon: float, elev: float,
                 tanggal, tz_name: str, ihtiyath: int = 0) -> dict:
    """
    Menghitung waktu salat menggunakan find_discrete Skyfield.

    Aturan ihtiyath:
      • Salat wajib (Subuh, Dzuhur, Asar, Maghrib, Isya) + Imsak : + ihtiyath
      • Terbit & Duha : - ihtiyath  (dimajukan lebih awal)
    Format output : HH:MM:SS
    """
    tz     = timezone(tz_name)
    lokasi = earth + wgs84.latlon(lat, lon, elevation_m=elev)
    tgl_dt = datetime(tanggal.year, tanggal.month, tanggal.day)

    t0 = ts.from_datetime(tz.localize(tgl_dt))
    t1 = ts.from_datetime(tz.localize(tgl_dt + timedelta(days=1)))

    lat_rad = np.radians(lat)

    R         = 34.0 / 60.0
    SD        = 16.0 / 60.0
    Dip       = 0.0293 * np.sqrt(max(elev, 0.0))
    h_horizon = -(R + SD + Dip)

    def state_func(t):
        ast = lokasi.at(t).observe(sun).apparent()
        alt, az, _ = ast.altaz()

        alt_deg = np.atleast_1d(np.array(alt.degrees, dtype=float))
        az_deg  = np.atleast_1d(np.array(az.degrees,  dtype=float))
        dec_rad = np.atleast_1d(np.array(ast.radec()[1].radians, dtype=float))

        after = az_deg > 180.0

        # h_asar per-elemen (Syafi'i)
        term   = 1.0 + np.tan(np.abs(dec_rad - lat_rad))
        h_asar = np.degrees(np.arctan(1.0 / term))

        n = len(alt_deg)
        s = np.zeros(n, dtype=int)

        for i in range(n):
            a   = alt_deg[i]
            aft = after[i]
            ha  = h_asar[i]

            if not aft:
                if a >= 4.5:
                    s[i] = 3       # Duha
                elif a >= h_horizon:
                    s[i] = 2       # Terbit
                elif a >= -20.0:
                    s[i] = 1       # Subuh
            else:
                if a >= ha:
                    s[i] = 4       # Dzuhur
                elif a >= h_horizon:
                    s[i] = 5       # Asar
                elif a >= -18.0:
                    s[i] = 6       # Maghrib
                else:
                    s[i] = 7       # Isya

        return s

    state_func.step_days = 1.0 / 1440.0

    times, states = find_discrete(t0, t1, state_func)

    label = {
        1: "Subuh", 2: "Terbit", 3: "Duha",
        4: "Dzuhur", 5: "Asar", 6: "Maghrib", 7: "Isya",
    }

    delta = timedelta(minutes=ihtiyath)
    hasil = {}
    found_subuh = False

    for t, s_val in zip(times, states):
        if s_val not in label:
            continue

        nama = label[s_val]

        # Terbit & Duha: dikurangi (dimajukan) — memberi ruang lebih
        if nama in IHTIYATH_KURANG:
            waktu = t.astimezone(tz) - delta
        else:
            waktu = t.astimezone(tz) + delta

        if s_val == 1:
            found_subuh = True
            hasil["Imsak"] = (waktu - timedelta(minutes=10)).strftime("%H:%M:%S")

        hasil[nama] = waktu.strftime("%H:%M:%S")

    if not found_subuh:
        hasil.setdefault("Imsak", "-")
        hasil.setdefault("Subuh", "-")

    return hasil


def waktu_sekarang_tz(tz_name: str) -> datetime:
    return datetime.now(timezone(tz_name))


def next_prayer(jadwal: dict, tz_name: str):
    ORDER = ["Imsak", "Subuh", "Terbit", "Duha", "Dzuhur", "Asar", "Maghrib", "Isya"]
    now   = waktu_sekarang_tz(tz_name)
    today = now.date()

    for name in ORDER:
        v = jadwal.get(name, "-")
        if v == "-":
            continue
        try:
            t = datetime.strptime(v, "%H:%M:%S").replace(
                year=today.year, month=today.month, day=today.day,
                tzinfo=timezone(tz_name)
            )
            if t > now:
                sisa = int((t - now).total_seconds())
                return name, f"{sisa//3600:02d}:{(sisa%3600)//60:02d}:{sisa%60:02d}"
        except ValueError:
            continue
    return None, None


# =============================
# TABS LOKASI
# =============================

st.markdown('<div class="section-label">Pilih Lokasi</div>', unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["🗺️  Klik di Peta", "✏️  Input Manual", "📡  GPS Otomatis"])

with tab1:
    st.caption("Klik pada peta untuk memilih lokasi, atau cari menggunakan kotak di bawah.")

    col_s, col_b = st.columns([4, 1])
    with col_s:
        query = st.text_input("Cari lokasi",
                              placeholder="Contoh: Yogyakarta, Jakarta Selatan, Banda Aceh…",
                              label_visibility="collapsed")
    with col_b:
        cari_klik = st.button("Cari", key="btn_cari")

    if cari_klik and query:
        with st.spinner("Mencari lokasi…"):
            lat_s, lon_s, addr = search_location(query)
        if lat_s is not None:
            st.session_state.location.update({
                "lat": lat_s, "lon": lon_s,
                "tz":  get_timezone(lat_s, lon_s),
                "alt": get_elevation(lat_s, lon_s),
                "city": addr,
            })
            st.success(f"Ditemukan: {addr}")
            st.rerun()
        else:
            st.error("Lokasi tidak ditemukan. Coba kata kunci lebih spesifik.")

    m_pick = folium.Map(
        location=[st.session_state.location["lat"], st.session_state.location["lon"]],
        zoom_start=12,
        tiles="CartoDB positron",
    )
    folium.Marker(
        [st.session_state.location["lat"], st.session_state.location["lon"]],
        tooltip="Lokasi Aktif",
        icon=folium.Icon(color="orange", icon="star"),
    ).add_to(m_pick)

    map_data = st_folium(m_pick, height=420, use_container_width=True)

    if map_data and map_data.get("last_clicked"):
        clat = map_data["last_clicked"]["lat"]
        clon = map_data["last_clicked"]["lng"]
        if (abs(clat - st.session_state.location["lat"]) > 1e-5 or
                abs(clon - st.session_state.location["lon"]) > 1e-5):
            with st.spinner("Memuat informasi lokasi…"):
                st.session_state.location.update({
                    "lat":  clat, "lon": clon,
                    "tz":   get_timezone(clat, clon),
                    "alt":  get_elevation(clat, clon),
                    "city": get_location_name(clat, clon),
                })
            st.success(f"Lokasi dipilih: {st.session_state.location['city']}")
            st.rerun()

with tab2:
    st.caption("Masukkan koordinat secara manual.")
    c1, c2, c3 = st.columns(3)
    with c1:
        m_lat = st.number_input("Latitude",
                                value=float(st.session_state.location["lat"]),
                                format="%.6f", step=0.0001)
    with c2:
        m_lon = st.number_input("Longitude",
                                value=float(st.session_state.location["lon"]),
                                format="%.6f", step=0.0001)
    with c3:
        m_alt = st.number_input("Ketinggian (m)",
                                value=float(st.session_state.location["alt"]),
                                min_value=0.0, step=1.0)

    if st.button("Gunakan Koordinat Ini", key="btn_manual"):
        if not (-90 <= m_lat <= 90) or not (-180 <= m_lon <= 180):
            st.error("Koordinat tidak valid. Latitude −90…90, Longitude −180…180.")
        else:
            with st.spinner("Memuat informasi lokasi…"):
                st.session_state.location.update({
                    "lat": m_lat, "lon": m_lon, "alt": m_alt,
                    "tz":  get_timezone(m_lat, m_lon),
                    "city": get_location_name(m_lat, m_lon),
                })
            st.success("Lokasi manual berhasil diterapkan.")
            st.rerun()

with tab3:
    st.caption("Gunakan lokasi GPS dari browser Anda.")
    st.info("Pastikan Anda mengizinkan akses lokasi pada browser.")

    geo = get_geolocation()

    if geo:
        lat_gps = geo["coords"]["latitude"]
        lon_gps = geo["coords"]["longitude"]
        acc_gps = geo["coords"].get("accuracy", "?")
        st.success(f"GPS terdeteksi — Akurasi ≈ {acc_gps:.0f} m")
        st.caption(f"Lat: {lat_gps:.6f}  |  Lon: {lon_gps:.6f}")

        if st.button("Gunakan Lokasi GPS Ini", key="btn_gps"):
            with st.spinner("Memuat informasi lokasi…"):
                st.session_state.location.update({
                    "lat":  lat_gps, "lon": lon_gps,
                    "tz":   get_timezone(lat_gps, lon_gps),
                    "alt":  get_elevation(lat_gps, lon_gps),
                    "city": get_location_name(lat_gps, lon_gps),
                })
            st.success("Lokasi GPS berhasil diterapkan.")
            st.rerun()
    else:
        st.warning("Sinyal GPS belum diterima. Izinkan akses lokasi lalu muat ulang halaman.")


# =============================
# LOKASI AKTIF
# =============================

loc = st.session_state.location
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="loc-card">
    <div class="loc-dot"></div>
    <div>
        <div class="loc-name">{loc['city']}</div>
        <div class="loc-meta">
            {loc['lat']:.6f}°, {loc['lon']:.6f}°
            &nbsp;·&nbsp; ↑ {loc['alt']:.0f} m
            &nbsp;·&nbsp; {loc['tz']}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# =============================
# INPUT TANGGAL & IHTIYATH
# =============================

st.markdown('<div class="section-label">Pengaturan Perhitungan</div>', unsafe_allow_html=True)

col_d, col_i, col_im = st.columns([2, 2, 3])
with col_d:
    tanggal = st.date_input("Tanggal", value=datetime.today())
with col_i:
    use_ihtiyath = st.checkbox(
        "Ihtiyath", value=True,
        help=(
            "Salat wajib & Imsak: ditambah (diundur).\n"
            "Terbit & Duha: dikurangi (dimajukan) — lebih konservatif."
        )
    )
with col_im:
    ihtiyath_menit = 0
    if use_ihtiyath:
        ihtiyath_menit = st.slider(
            "Nilai ihtiyath (menit)",
            min_value=1, max_value=5, value=2,
            help="Standar Kemenag: 1–2 menit"
        )

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)


# =============================
# HITUNG
# =============================

if st.button("⬡  Hitung Waktu Salat", use_container_width=True):
    with st.spinner("Menghitung posisi matahari secara astronomis…"):
        jadwal = hitung_salat(
            loc["lat"], loc["lon"], loc["alt"],
            tanggal, loc["tz"],
            ihtiyath=ihtiyath_menit,
        )
    st.session_state["jadwal"]         = jadwal
    st.session_state["jadwal_tanggal"] = str(tanggal)
    st.session_state["jadwal_tz"]      = loc["tz"]
    st.session_state["jadwal_iht"]     = ihtiyath_menit


# =============================
# TAMPILKAN JADWAL
# =============================

if "jadwal" in st.session_state:
    jadwal  = st.session_state["jadwal"]
    tz_name = st.session_state["jadwal_tz"]
    iht     = st.session_state["jadwal_iht"]

    ORDER = ["Imsak", "Subuh", "Terbit", "Duha", "Dzuhur", "Asar", "Maghrib", "Isya"]

    missing = [n for n in ORDER if n not in jadwal]
    if missing:
        st.warning(
            f"Waktu berikut tidak ditemukan: {', '.join(missing)} "
            "— kemungkinan lokasi lintang ekstrem."
        )

    iht_badge = (f'<span class="ihtiyath-badge">±{iht} mnt ihtiyath</span>'
                 if iht > 0 else "")
    tgl_fmt = datetime.strptime(
        st.session_state["jadwal_tanggal"], "%Y-%m-%d"
    ).strftime("%d %B %Y")

    st.markdown(f"""
    <div class="section-label">
        Jadwal Salat &nbsp;·&nbsp; {tgl_fmt} &nbsp;{iht_badge}
    </div>
    """, unsafe_allow_html=True)

    # ── Banner waktu berikutnya ──
    is_today = (st.session_state["jadwal_tanggal"] == str(datetime.today().date()))
    if is_today:
        np_name, np_countdown = next_prayer(jadwal, tz_name)
        if np_name:
            st.markdown(f"""
            <div class="next-prayer">
                <div>
                    <div class="next-label">Waktu Salat Berikutnya</div>
                    <div class="next-name">{np_name}</div>
                </div>
                <div class="next-countdown">{np_countdown}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Tentukan waktu aktif ──
    now_str = waktu_sekarang_tz(tz_name).strftime("%H:%M:%S")

    def is_active(name: str) -> bool:
        if not is_today:
            return False
        idx = ORDER.index(name)
        cur = jadwal.get(name, "-")
        if cur == "-" or now_str < cur:
            return False
        for nxt in ORDER[idx + 1:]:
            nv = jadwal.get(nxt, "-")
            if nv != "-" and now_str >= nv:
                return False
        return True

    # ── Kartu jadwal ──
    cols_row1 = st.columns(4)
    cols_row2 = st.columns(4)

    for i, name in enumerate(ORDER):
        col = cols_row1[i % 4] if i < 4 else cols_row2[i % 4]
        val = jadwal.get(name, "-")
        css = "active" if is_active(name) else ("missing" if val == "-" else "")

        # Pisah HH:MM dan :SS
        if val != "-":
            hm  = val[:5]   # "HH:MM"
            sec = val[5:]   # ":SS"
        else:
            hm  = "–"
            sec = ""

        # Catatan ihtiyath per kartu
        if iht > 0:
            if name in IHTIYATH_KURANG:
                note = f"−{iht} mnt (dimajukan)"
            elif name == "Imsak":
                note = "Subuh − 10 mnt"
            else:
                note = f"+{iht} mnt ihtiyath"
        else:
            note = ""

        with col:
            st.markdown(f"""
            <div class="prayer-card {css}">
                <div class="prayer-label">{name}</div>
                <div>
                    <span class="prayer-time-hm">{hm}</span><span class="prayer-time-sec">{sec}</span>
                </div>
                <div class="prayer-note">{note}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Footer ──
    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="footer-note">
        Perhitungan menggunakan <b>Skyfield find_discrete</b> · Data ephemeris DE421 NASA
        &nbsp;·&nbsp; Kriteria: Subuh −20°, Isya −18°, Asar Syafi'i
        &nbsp;·&nbsp; Terbit &amp; Duha: ihtiyath dikurangi (dimajukan lebih awal)
    </div>
    """, unsafe_allow_html=True)
