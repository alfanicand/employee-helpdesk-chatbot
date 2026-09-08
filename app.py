import streamlit as st

from chatbot import get_chatbot_response


st.set_page_config(
    page_title="Employee Helpdesk Chatbot",
    page_icon="💬",
    layout="centered"
)


def get_initial_message():
    """Membuat pesan pembuka chatbot."""
    return {
        "role": "assistant",
        "content": (
            "Halo! Saya siap membantu memberikan informasi mengenai "
            "cuti, lembur, absensi, penggajian, jadwal shift, dan K3."
        )
    }


# Menyiapkan riwayat percakapan
if "messages" not in st.session_state:
    st.session_state.messages = [get_initial_message()]


# Tampilan utama
st.title("💬 Employee Helpdesk Chatbot")

st.write(
    "Chatbot internal sederhana untuk membantu menjawab "
    "pertanyaan umum karyawan."
)

st.info(
    "Seluruh informasi dalam aplikasi ini bersifat fiktif "
    "dan hanya digunakan untuk pembelajaran serta portofolio."
)


# Daftar contoh pertanyaan
with st.expander("Lihat contoh pertanyaan"):
    st.markdown("""
- Bagaimana cara mengajukan cuti?
- Bagaimana prosedur lembur?
- Saya lupa melakukan absen.
- Di mana saya dapat melihat slip gaji?
- Bagaimana cara melihat jadwal shift?
- Bagaimana melaporkan kecelakaan kerja?
""")


# Menampilkan riwayat percakapan
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Menerima pertanyaan pengguna
question = st.chat_input("Tuliskan pertanyaan Anda...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    detected_intent, answer = get_chatbot_response(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)


# Sidebar
with st.sidebar:
    st.header("Tentang Aplikasi")

    st.write(
        "Jawaban chatbot diperoleh dari data FAQ yang "
        "tersimpan dalam database SQLite."
    )

    st.subheader("Topik yang tersedia")

    st.markdown("""
- Pengajuan cuti
- Prosedur lembur
- Kendala absensi
- Informasi penggajian
- Jadwal shift
- Keselamatan kerja
""")

    if st.button("Hapus percakapan", use_container_width=True):
        st.session_state.messages = [get_initial_message()]
        st.rerun()
