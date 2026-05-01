import streamlit as st

st.set_page_config(page_title="SVARA AI PRO", page_icon="🎙️")

# CSS untuk mempercantik tampilan hasil lirik
st.markdown("""
    <style>
    .lirik-box {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎙️ SVARA AI PRO")
st.markdown("### *Sound's Vital Aspiration: Revolutionary Audio*")

with st.sidebar:
    st.header("Pilar Kreatif")
    genre = st.radio("Pilih Genre:", ["Pop Rock (Manly Love)", "Alt Rock (Satire)"])
    st.info("Catatan: Gunakan API Key untuk hasil maksimal.")

# Fungsi Generator Lirik Lengkap
def generate_full_lyrics(topik, genre):
    if genre == "Pop Rock (Manly Love)":
        return f"""
[JUDUL: {topik.upper()}]

[INTRO: Clean Electric Guitar, Atmospheric Reverb]
[RIFF: Steady Drum Beat, Warm Bass Entry]

[VERSE 1]
Langkah kaki ini takkan pernah ragu
Menopang bebanmu di setiap waktu
Bukan rayuan kosong yang aku beri
Tapi janji setia yang kukunci di hati.

[CHORUS]
Aku adalah karang di tengah ombakmu
Takkan hancur meski badai menderu
Cintaku tak menye, cintaku itu nyata
Berdiri tegak menjaga setiap luka.

[RIFF / TRANSITION]

[VERSE 2]
Dunia mungkin berisik dengan dusta
Tapi bahuku adalah tempatmu bertahta
Diamku bukan berarti aku tak ada
Aku menjagamu dalam setiap doa.

[BRIDGE: Emotional Peak, Powerful Vocals]
Biarkan mereka bicara tentang kemewahan
Kita bicara tentang keteguhan...

[CHORUS]
Aku adalah karang di tengah ombakmu
Takkan hancur meski badai menderu...

[OUTRO: Fade out with lingering guitar chords]
"""
    else:
        return f"""
[JUDUL: SINDIRAN {topik.upper()}]

[INTRO: Feedback, Gritty Fuzz Distortion]
[RIFF: Aggressive Bassline, Odd Time Signature Drumming]

[VERSE 1]
Lampu kota mati, tapi egomu tetap nyala
Mengejar mimpi yang sebenarnya hanyalah gala
Kau bilang revolusi tapi hanya di layar kaca
Realita kau abaikan, hanya angka yang kau baca.

[CHORUS]
Selamat datang di roda tikus yang berputar
Lari di tempat sampai tulangmu bergetar
Kau tertawa di atas pasir yang mulai amblas
Jiwa terjual, tapi merasa sudah bebas!

[RIFF: Chaos Glitch Sound]

[VERSE 2]
Kau rakit istana dari janji yang membusuk
Hati nuranimu pelan-pelan mulai menusuk
Berhenti pamer lelah di dunia yang maya
Jika kakimu sendiri tak pernah tahu arahnya.

[BRIDGE: Slow Tempo, Heavy Distorted Vocals]
Bangun... Bangun dari tidur panjangmu...
Cermin takkan pernah berbohong padamu...

[CHORUS]
Selamat datang di roda tikus yang berputar...

[OUTRO: Sudden silence, single feedback note]
"""

# Tampilan Utama
if genre == "Pop Rock (Manly Love)":
    st.info("💡 Karakter: Maskulin, Tenang, Setia, Tidak Lebay.")
    topik = st.text_input("Topik Lagu Cinta:", placeholder="Contoh: Kesetiaan dalam diam")
    if st.button("Generate Full Structure"):
        hasil = generate_full_lyrics(topik, "Pop Rock (Manly Love)")
        st.markdown(f'<div class="lirik-box"><pre>{hasil}</pre></div>', unsafe_allow_html=True)

elif genre == "Alt Rock (Satire)":
    st.error("💡 Karakter: Kritik Sosial, Distorsi, Tajam.")
    topik = st.text_input("Apa yang ingin disindir?", placeholder="Contoh: Orang sibuk pamer lelah")
    if st.button("Generate Satire Structure"):
        hasil = generate_full_lyrics(topik, "Alt Rock (Satire)")
        st.markdown(f'<div class="lirik-box"><pre>{hasil}</pre></div>', unsafe_allow_html=True)

# ... (Fitur Musik & Visual tetap di bawah)
