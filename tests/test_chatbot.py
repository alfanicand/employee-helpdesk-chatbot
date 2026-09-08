import sys
from pathlib import Path


# Memungkinkan file test mengakses chatbot.py
PROJECT_FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_FOLDER))

from chatbot import find_answer


TEST_DATA = [
    ("Bagaimana cara mengajukan cuti?", "pengajuan_cuti"),
    ("Saya ingin izin cuti minggu depan", "pengajuan_cuti"),
    ("Bagaimana prosedur lembur?", "prosedur_lembur"),
    ("Saya ingin mengajukan overtime", "prosedur_lembur"),
    ("Saya lupa absen tadi pagi", "kendala_absensi"),
    ("Presensi saya tidak tercatat", "kendala_absensi"),
    ("Di mana saya dapat melihat slip gaji?", "informasi_penggajian"),
    ("Saya ingin menanyakan informasi payroll", "informasi_penggajian"),
    ("Bagaimana cara melihat jadwal shift?", "jadwal_shift"),
    ("Jam masuk saya besok pukul berapa?", "jadwal_shift"),
    ("Bagaimana melaporkan kecelakaan kerja?", "keselamatan_kerja"),
    ("Saya menemukan potensi bahaya kerja", "keselamatan_kerja"),
    ("Apa menu kantin hari ini?", "tidak_dikenali")
]


def run_test():
    """Menjalankan pengujian deteksi intent chatbot."""
    correct_count = 0
    test_results = []

    for question, expected_intent in TEST_DATA:
        predicted_intent, _ = find_answer(question)
        is_correct = predicted_intent == expected_intent

        if is_correct:
            correct_count += 1

        test_results.append({
            "question": question,
            "expected": expected_intent,
            "predicted": predicted_intent,
            "status": "BENAR" if is_correct else "SALAH"
        })

    total_tests = len(TEST_DATA)
    accuracy = correct_count / total_tests * 100

    for result in test_results:
        print(f"Pertanyaan : {result['question']}")
        print(f"Diharapkan : {result['expected']}")
        print(f"Prediksi   : {result['predicted']}")
        print(f"Status     : {result['status']}")
        print("-" * 60)

    print(f"Jumlah pengujian : {total_tests}")
    print(f"Prediksi benar   : {correct_count}")
    print(f"Prediksi salah   : {total_tests - correct_count}")
    print(f"Akurasi pengujian: {accuracy:.2f}%")


if __name__ == "__main__":
    run_test()
