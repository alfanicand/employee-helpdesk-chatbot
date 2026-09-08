from database import get_connection


FAQ_DATA = [
    {
        "intent": "pengajuan_cuti",
        "keywords": "cuti|izin cuti|mengajukan cuti|pengajuan cuti",
        "answer": (
            "Pengajuan cuti dilakukan melalui sistem HR dan "
            "harus memperoleh persetujuan atasan."
        )
    },
    {
        "intent": "prosedur_lembur",
        "keywords": "lembur|overtime|pengajuan lembur",
        "answer": (
            "Pengajuan lembur harus disampaikan kepada atasan "
            "dan memperoleh persetujuan sebelum pelaksanaan."
        )
    },
    {
        "intent": "kendala_absensi",
        "keywords": "absen|absensi|presensi|lupa absen",
        "answer": (
            "Kendala absensi dapat dilaporkan kepada HR dengan "
            "menyertakan tanggal dan alasan."
        )
    },
    {
        "intent": "informasi_penggajian",
        "keywords": "gaji|penggajian|slip gaji|payroll",
        "answer": (
            "Informasi dan slip gaji dapat diperiksa melalui "
            "sistem HR atau dikonfirmasikan kepada bagian payroll."
        )
    },
    {
        "intent": "jadwal_shift",
        "keywords": "shift|jadwal kerja|jadwal masuk|jam masuk",
        "answer": (
            "Jadwal shift dapat diperiksa melalui sistem internal "
            "atau dikonfirmasikan kepada atasan masing-masing."
        )
    },
    {
        "intent": "keselamatan_kerja",
        "keywords": (
            "k3|keselamatan kerja|kecelakaan kerja|"
            "insiden kerja|bahaya kerja"
        ),
        "answer": (
            "Insiden atau potensi bahaya kerja harus segera "
            "dilaporkan kepada atasan dan petugas K3."
        )
    }
]


def create_tables():
    """Membuat tabel FAQ dan riwayat percakapan."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intent TEXT NOT NULL UNIQUE,
            keywords TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            detected_intent TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_faq_data():
    """Memasukkan atau memperbarui data FAQ."""
    connection = get_connection()
    cursor = connection.cursor()

    for faq in FAQ_DATA:
        cursor.execute("""
            INSERT INTO faq (intent, keywords, answer)
            VALUES (?, ?, ?)
            ON CONFLICT(intent) DO UPDATE SET
                keywords = excluded.keywords,
                answer = excluded.answer
        """, (
            faq["intent"],
            faq["keywords"],
            faq["answer"]
        ))

    connection.commit()
    connection.close()


def setup_database():
    """Menjalankan seluruh persiapan database."""
    create_tables()
    insert_faq_data()


if __name__ == "__main__":
    setup_database()
    print("Database dan data FAQ berhasil dibuat.")
