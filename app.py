import streamlit as st

# Konfigurasi Tampilan
st.set_page_config(page_title="SVARA AI PRO", page_icon="🎙️")
st.title("🎙️ SVARA AI PRO")
st.markdown("### *Sound's Vital Aspiration: Revolutionary Audio*")

# Pilihan Genre
with st.sidebar:
    st.header("Pilar Kreatif")
    genre = st.radio("Pilih Genre:", ["Pop Rock (Manly Love)", "Alt Rock (Satire)"])

# Logika Fitur
if genre == "Pop Rock (Manly Love)":
    st.info("💡 Karakter: Maskulin, Tenang, Setia, Tidak Lebay.")
    fitur = st.selectbox("Pilih Bantuan:", ["Lirik Cinta Manly", "Komposisi Musik", "Visual"])
    
    if fitur == "Lirik Cinta Manly":
        if st.button("Generate Lirik"):
            st.code("Tak perlu banyak kata untuk membuktikan\nLangkahku tetap di sampingmu saat badai datang\nBukan tentang janji manis yang memudar\nTapi tentang punggung yang siap menahan beban.")
            
    elif fitur == "Komposisi Musik":
        st.success("Chord: G - D - Em - C (Powerful Clean)")
        st.write("Saran: Vokal berat & tegas. Gitar elektrik clean.")

elif genre == "Alt Rock (Satire)":
    st.error("💡 Karakter: Kritik Sosial, Distorsi, Tajam.")
    fitur = st.selectbox("Pilih Bantuan:", ["Lirik Sindiran", "Komposisi Musik", "Visual"])
    
    if fitur == "Lirik Sindiran":
        if st.button("Generate Sindiran"):
            st.code("Kau rakit istana dari pasir yang rapuh\nKarena logikamu sudah lama lumpuh.\nBerhenti sejenak, lihat ke dalam\nAtau kau 'kan tenggelam di waktu yang kelam.")

    elif fitur == "Komposisi Musik":
        st.warning("Chord: Bm - G - F# (Gritty & Dark)")
        st.write("Saran: Fuzz distortion & drum industrial.")

if fitur == "Visual":
    lirik_vis = st.text_area("Masukkan lirik untuk prompt video:")
    if st.button("Generate Visual Prompt"):
        style = "Soft Cinematic" if genre == "Pop Rock (Manly Love)" else "Analog Glitch"
        st.write(f"**Prompt AI Video:**\n`{style} style, 16:9, depicting: {lirik_vis}`")
