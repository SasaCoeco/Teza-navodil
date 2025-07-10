import streamlit as st

# Nastavitve strani
st.set_page_config(page_title="Coeco Kalkulator", page_icon="📘")

# Dovoljeni formati v centimetrih
formati = {
    "A6": (10.5, 14.8),
    "A5": (14.8, 21.0),
    "A4": (21.0, 29.7)
}

# Glava
st.markdown("""
<div style='background-color:#1f4e79; padding:16px; border-radius:8px; text-align:center'>
    <h2 style='color:white;'>📘 Kalkulator teže tiskovine</h2>
    <h4 style='color:white;'>Ovitek + jedro | Formati: A6, A5, A4</h4>
</div>
""", unsafe_allow_html=True)

st.info("📌 Vnesi število **strani**, ne listov. Ena polo običajno vsebuje dve strani.")

# --- Ovitek ---
st.subheader("🟦 Ovitka")

col1, col2, col3 = st.columns(3)
with col1:
    format_ovitka = st.selectbox("Format ovitka", list(formati.keys()), index=1)
with col2:
    strani_ovitka = st.number_input("Število strani ovitka", min_value=1, value=4)
with col3:
    gramatura_ovitka = st.number_input("Gramatura ovitka (g/m²)", min_value=1.0, value=60.0)

sirina_o, visina_o = formati[format_ovitka]
teza_stran_o = (sirina_o * visina_o * gramatura_ovitka) / 10000 / 1000 / 2
teza_ovitka = round(teza_stran_o * strani_ovitka, 6)

st.success(f"Teža ovitka: **{teza_ovitka} g**")

# --- Jedro ---
st.subheader("📗 Jedro")

col4, col5, col6 = st.columns(3)
with col4:
    format_jedra = st.selectbox("Format jedra", list(formati.keys()), index=1, key="format_j")
with col5:
    strani_jedra = st.number_input("Število strani jedra", min_value=1, value=200)
with col6:
    gramatura_jedra = st.number_input("Gramatura jedra (g/m²)", min_value=1.0, value=48.8)

sirina_j, visina_j = formati[format_jedra]
teza_stran_j = (sirina_j * visina_j * gramatura_jedra) / 10000 / 1000 / 2
teza_jedra = round(teza_stran_j * strani_jedra, 6)

st.success(f"Teža jedra: **{teza_jedra} g**")

# --- Skupna teža ---
skupna_teza = round(teza_ovitka + teza_jedra, 6)
st.markdown("## 📦 Skupna teža tiskovine")
st.info(f"📘 Skupna teža: **{skupna_teza} g**")

# --- Podpis ---
st.markdown("""
<hr style='margin-top:40px;'>
<p style='font-size:13px; text-align:center; color:gray;'>
Aplikacijo je zasnoval <strong>Saša Rednak | Coeco d.o.o.</strong><br>
Natančen izračun teže natisnjenih strani po formatu, gramaturi in obsegu.
</p>
""", unsafe_allow_html=True)