Smart Lamp IoT (ESP32 + Flask + React)

Project IoT sederhana untuk mengontrol lampu rumah (AC) menggunakan:
- ESP32 (MicroPython)
- Sensor PIR dan LDR
- Relay
- Backend Flask (HTTP API)
- Frontend React + Tailwind CSS

Project ini ditujukan untuk pemula, tugas sekolah, dan demo IoT.


--------------------------------------------------
Arsitektur Sistem
--------------------------------------------------

ESP32 (MicroPython)
   |
   | HTTP (JSON)
   v
Flask Backend (API)
   |
   | REST API
   v
React Dashboard (UI)


--------------------------------------------------
Fitur
--------------------------------------------------

- Deteksi gelap menggunakan LDR
- Deteksi gerakan menggunakan PIR
- Kontrol lampu AC melalui relay
- Mode AUTO dan MANUAL
- Monitoring sensor secara realtime
- Dashboard modern dan responsive


--------------------------------------------------
Persiapan Awal (Laptop Kosongan)
--------------------------------------------------

1. Install Node.js
Digunakan untuk menjalankan React Dashboard

Download:
https://nodejs.org

Pilih versi LTS (Recommended)

Cek instalasi:
node -v
npm -v


2. Install Python
Digunakan untuk menjalankan Flask Backend

Download:
https://www.python.org/downloads/

Saat install:
- Centang "Add Python to PATH"

Cek instalasi:
python --version
pip --version


3. Install Git (Opsional tapi disarankan)

Download:
https://git-scm.com

Cek:
git --version


--------------------------------------------------
Menjalankan Backend (Flask)
--------------------------------------------------

1. Masuk folder backend
cd backend

2. Install dependency
pip install flask flask-cors

3. Jalankan server
python app.py

Jika berhasil, akan muncul:
Running on http://0.0.0.0:5000

Catat IP komputer kamu, contoh:
http://192.168.1.10:5000


--------------------------------------------------
Menjalankan Frontend (React + Tailwind)
--------------------------------------------------

1. Masuk folder frontend
cd frontend

2. Install dependency React
npm install

3. Jalankan React
npm run dev

Buka browser dan akses:
http://localhost:5173


--------------------------------------------------
Konfigurasi API di React
--------------------------------------------------

Buka file:
src/App.jsx

Ubah alamat API menjadi IP komputer kamu:

const API = "http://192.168.1.10:5000";


--------------------------------------------------
Upload Program ke ESP32
--------------------------------------------------

1. Install MicroPython firmware ke ESP32
2. Upload file main.py ke ESP32
3. Pastikan SSID, password WiFi, dan IP server sudah benar
4. ESP32 dan laptop harus berada di jaringan WiFi yang sama


--------------------------------------------------
Catatan Penting
--------------------------------------------------

- Jangan menyambungkan lampu AC langsung ke ESP32
- Gunakan relay module untuk keamanan
- Periksa kabel fasa dan netral dengan benar
- Kalibrasi nilai LDR sesuai kondisi ruangan


--------------------------------------------------
Pengembangan Selanjutnya
--------------------------------------------------

- Menambahkan login user
- Grafik sensor
- Dark mode
- Notifikasi
- Deploy server ke cloud

Project ini cocok sebagai tugas sekolah, project IoT dasar, dan portfolio.
