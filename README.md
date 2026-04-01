# Chess AI - Projek Akhir Artificial Intelligence

Aplikasi Catur dengan AI menggunakan algoritma Minimax dan Alpha-Beta Pruning. Dibangun dengan Flask (backend) dan JavaScript (frontend).

## 👥 Kelompok 8

| Nama | NIM |
|------|-----|
| Dimas Abdus Syukur | 24051204101 |
| Jonathan | 24051204087 |
| Josua Moreno Silitonga | 24051204091 |

**Mata Kuliah:** Artificial Intelligence  
**Semester:** 3

## 🧠 Algoritma yang Digunakan

- **Minimax Algorithm** – untuk mengevaluasi kemungkinan langkah terbaik
- **Alpha-Beta Pruning** – untuk mengoptimalkan pencarian dengan memangkas cabang yang tidak perlu
- **Fungsi Evaluasi** – berbasis material piece (pawn, knight, bishop, rook, queen, king) + bonus posisional (kontrol tengah, mobilitas)

## 🚀 Fitur

- **Play vs AI** – pemain (putih) melawan AI (hitam)
- **Level Kesulitan** – pilih depth pencarian AI (2, 3, atau 4)
- **Putar Papan** – flip board untuk kenyamanan bermain
- **Riwayat Langkah** – mencatat semua langkah yang telah dimainkan
- **Evaluasi Posisi** – menampilkan skor evaluasi posisi saat ini
- **Informasi AI** – menampilkan waktu berpikir dan jumlah node yang dievaluasi

## 🛠️ Teknologi yang Digunakan

### Backend (Python)

- **Flask** – REST API
- **python-chess** – library untuk logika catur
- **Flask-CORS** – untuk mengatasi CORS

### Frontend (JavaScript)

- **chess.js** – library untuk logika catur di client
- **HTML/CSS** – tampilan antarmuka
- **Fetch API** – komunikasi dengan backend

## 📁 Struktur Proyek

```text
chess-ai-project/
├── app.py              # Flask backend server
├── chess_ai.py         # Implementasi AI (Minimax + Alpha-Beta)
├── index.html          # Frontend UI
└── README.md           # Dokumentasi proyek

🔧 Cara Menjalankan
1. Clone Repository
git clone https://github.com/god1mas/chess-ai-project.git
cd chess-ai-project
2. Masuk ke Folder Backend
cd backend
3. Install Dependencies
pip install -r requirements.txt

Jika requirements.txt belum lengkap, kamu juga bisa install manual:

pip install flask flask-cors python-chess
4. Jalankan Backend Server
python app.py

Server akan berjalan di:

http://localhost:5000
5. Jalankan Frontend

Buka file frontend/index.html di browser, atau jalankan menggunakan Live Server di VS Code.