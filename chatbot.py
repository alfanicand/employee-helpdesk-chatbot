import re

from database import get_all_faq, save_chat_log


FALLBACK_RESPONSE = (
    "Maaf, saya belum memahami pertanyaan tersebut. "
    "Silakan tanyakan mengenai cuti, lembur, absensi, "
    "penggajian, jadwal shift, atau K3."
)


def preprocess_text(text):
    """Membersihkan dan menyeragamkan teks pertanyaan."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def find_answer(question):
    """Menentukan intent dan jawaban berdasarkan keyword."""
    clean_question = preprocess_text(question)
    faq_data = get_all_faq()

    detected_intent = "tidak_dikenali"
    selected_answer = FALLBACK_RESPONSE
    highest_score = 0

    for intent, keywords, answer in faq_data:
        keyword_list = keywords.split("|")
        score = 0

        for keyword in keyword_list:
            clean_keyword = preprocess_text(keyword)

            if clean_keyword in clean_question:
                score += 1

        if score > highest_score:
            highest_score = score
            detected_intent = intent
            selected_answer = answer

    return detected_intent, selected_answer


def get_chatbot_response(question, save_log=True):
    """Menghasilkan respons dan menyimpan riwayat percakapan."""
    detected_intent, answer = find_answer(question)

    if save_log:
        try:
            save_chat_log(
                question,
                detected_intent,
                answer
            )
        except Exception:
            # Chatbot tetap berjalan jika log gagal disimpan.
            pass

    return detected_intent, answer
