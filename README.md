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
