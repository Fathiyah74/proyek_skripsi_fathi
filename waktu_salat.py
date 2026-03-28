import streamlit as st
import folium
import numpy as np
import requests

from streamlit_folium import st_folium
from streamlit_javascript import st_javascript

from skyfield.api import load, wgs84
from skyfield.searchlib import find_discrete

from datetime import datetime, timedelta
from pytz import timezone
from datetime import datetime
from timezonefinder import TimezoneFinder 

# =============================
# PAGE CONFIG
# =============================

st.set_page_config(
    page_title="Salat_F - Waktu Salat Find Discrete",
    layout="wide"
)

# =============================
# STYLE
# =============================

st.markdown("""
<style>

.title{
font-size:48px;
font-weight:700;
text-align:center;
margin-bottom:5px;
}

.subtitle{
text-align:center;
color:#cbd5e1;
margin-bottom:30px;
font-size:16px
}

.location-card{
background:linear-gradient(135deg,#4f46e5,#6366f1);
padding:18px;
border-radius:12px;
text-align:center;
box-shadow:0 6px 15px rgba(0,0,0,0.1);
transition:0.2s;
}

.prayer-box:hover{
    transform:translateY(-5px);
}

.prayer-title{
    font-size:16px;
    color:#64748b;
}

.prayer-time{
    font-size:28px;
    font-weight:bold;
    color:#fffff;
}

/* === SPACING FIX === */
.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title"> Salat_F </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Perhitungan waktu salat menggunakan Find Discrete Skyfield</div>', unsafe_allow_html=True)

# =============================
# LOAD EPHEMERIS
# =============================

@st.cache_resource
def load_ephemeris():
    ts = load.timescale()
    eph = load('de421.bsp')
    return ts, eph['earth'], eph['sun']

ts, earth, sun = load_ephemeris()

# =============================
# SESSION STATE
# =============================

if "location" not in st.session_state:

    st.session_state.location = {
        "lat": -6.97,
        "lon": 110.42,
        "city": "Semarang",
        "tz": "Asia/Jakarta",
        "alt": 10
    }

# =============================
# GPS BROWSER
# =============================

@st.cache_data(ttl=3600)  # Cache 1 jam
def get_auto_location():
    """Ambil lokasi otomatis + nama kota"""
    try:
        # IP API - dapat lat/lon/timezone
        ip_resp = requests.get(
            "http://ip-api.com/json/?fields=status,message,lat,lon,city,regionName,country,timezone",
            timeout=5
        ).json()
        
        if ip_resp["status"] == "success":
            lat, lon = ip_resp["lat"], ip_resp["lon"]
            
            # Reverse geocoding - nama kota akurat
            rev_resp = requests.get(
                f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&addressdetails=1",
                headers={"User-Agent": "Salat_F/1.0"},
                timeout=5
            ).json()
            
            city_name = rev_resp.get("display_name", f"{ip_resp['city']}, {ip_resp['regionName']}")
            city_short = rev_resp.get("address", {}).get("city") or ip_resp["city"]
            
            return {
                "lat": lat, "lon": lon,
                "city": city_short,
                "full_city": city_name,
                "tz": ip_resp["timezone"],
                "country": ip_resp["country"],
                "source": "IP+OSM",
                "accuracy": "Kota"
            }
    except:
        pass
    return None



# =============================
# PERHITUNGAN WAKTU SALAT
# =============================

def hitung_salat(lat, lon, elev, tanggal, tz_name):

    tz = timezone(tz_name)

    lokasi = earth + wgs84.latlon(lat, lon, elevation_m=elev)
    tanggal_dt = datetime(tanggal.year, tanggal.month, tanggal.day)

    t0 = ts.from_datetime(tz.localize(tanggal_dt))
    t1 = ts.from_datetime(tz.localize(tanggal_dt + timedelta(days=1)))

    lat_rad = np.radians(lat)

    def state_func(t):

        ast = lokasi.at(t).observe(sun).apparent()

        alt, az, _ = ast.altaz()

        alt = alt.degrees
        az = az.degrees

        dec = ast.radec()[1].radians

        after = az > 180

        term = 1 + np.tan(abs(dec - lat_rad))
        h_asar = np.degrees(np.arctan(1/term))

        s = np.zeros_like(alt)

        s[(~after) & (alt >= -20)] = 1
        s[(~after) & (alt >= -1)] = 2
        s[(~after) & (alt >= 4.5)] = 3

        s[(after)] = 4
        s[(after) & (alt <= h_asar)] = 5
        s[(after) & (alt <= -1)] = 6
        s[(after) & (alt <= -18)] = 7

        return s

    state_func.step_days = 1/1440

    times, states = find_discrete(t0, t1, state_func)

    label = {
        1:"Subuh",
        2:"Terbit",
        3:"Duha",
        4:"Dzuhur",
        5:"Asar",
        6:"Maghrib",
        7:"Isya"
    }

    hasil = {}

    for t,s in zip(times,states):

        if s in label:

            waktu = t.astimezone(tz)

            if s == 1:
                hasil["Imsak"] = (waktu - timedelta(minutes=10)).strftime("%H:%M")

            hasil[label[s]] = waktu.strftime("%H:%M:%S")

    return hasil

# =============================
# TAB LOKASI
# =============================

tab1, tab2 = st.tabs(["📍 Lokasi GPS", "✏️ Input Manual"])

# =============================
# GPS TAB
# =============================

def get_timezone(lat, lon):
    tf = TimezoneFinder()
    tz_name = tf.timezone_at(lat=lat, lng=lon)

    if tz_name is None:
        return "UTC"  # fallback

    return tz_name 

with tab1:

    if st.button("Ambil Lokasi GPS Otomatis"):

        loc = get_auto_location()

        if loc:
            st.session_state.location["lat"] = loc["lat"]
            st.session_state.location["lon"] = loc["lon"]
            st.session_state.location["tz"] = get_timezone(loc["lat"], loc["lon"])

            st.success("Lokasi berhasil diperbarui dari GPS")

# =============================
# MANUAL TAB
# =============================

with tab2:

    lat = st.number_input("Latitude", value=st.session_state.location["lat"])

    lon = st.number_input("Longitude", value=st.session_state.location["lon"])

    alt = st.number_input("Ketinggian (meter)", value=st.session_state.location["alt"])

    if st.button("Gunakan Lokasi Manual"):

        st.session_state.location["lat"] = lat
        st.session_state.location["lon"] = lon
        st.session_state.location["alt"] = alt
        st.session_state.location["tz"] = get_timezone(lat, lon)

# =============================
# LOKASI AKTIF
# =============================

loc = st.session_state.location

st.markdown(f"""
<div class="location-card">

📍 <b>Lokasi Aktif</b><br>
            
Latitude : {loc['lat']}<br>
Longitude : {loc['lon']}<br>
Elevation : {loc['alt']} m<br>
Timezone : {loc['tz']}

</div>
""", unsafe_allow_html=True)

# =============================
# PETA
# =============================

m = folium.Map(
    location=[loc["lat"], loc["lon"]],
    zoom_start=12,
    tiles="CartoDB positron"
)

folium.Marker(
    [loc["lat"], loc["lon"]],
    tooltip="Lokasi Anda"
).add_to(m)

st_folium(m, height=450, use_container_width=True)

# =============================
# INPUT TANGGAL
# =============================

tanggal = st.date_input("Pilih Tanggal")

# =============================
# HITUNG
# =============================

if st.button("Hitung Waktu Salat"):

    jadwal = hitung_salat(
        loc["lat"],
        loc["lon"],
        loc["alt"],
        tanggal,
        loc["tz"]
    )

    st.subheader("Jadwal Salat")

    cols = st.columns(4)

    for i, (k, v) in enumerate(jadwal.items()):
        col = cols[i % 4]

        col.markdown(f"""
        <div class="prayer-box">
            <div class="prayer-title">{k}</div>
            <div class="prayer-time">{v}</div>
        </div>
        """, unsafe_allow_html=True)