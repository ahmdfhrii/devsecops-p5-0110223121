# Task Manager API
Aplikasi REST API sederhana untuk mengelola daftar tugas (tambah, lihat, selesaikan, hapus).

## Teknologi
Python 3.11, Flask, pytest, Bandit, GitHub Actions

## Cara Menjalankan
pip install -r requirements.txt
python main.py        # server di http://127.0.0.1:5000
pytest                # menjalankan unit test

## Pipeline CI/CD
Workflow `.github/workflows/devsecops.yml` terpicu pada push & pull request ke `main`:
1. **build**: install dependency dan jalankan unit test
2. **sast-scan** (needs: build): Bandit SAST + Quality Gate (gagal jika ada temuan HIGH)