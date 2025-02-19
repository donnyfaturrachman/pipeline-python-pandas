# pipeline-python-pandas
Data Pipelines dengan Python &amp; Pandas

Deskripsi: Ambil data dari API, bersihkan, dan simpan ke database.

> Alat yang Digunakan:
  - Python (requests, pandas, sqlite3)
  - SQLite → Database untuk menyimpan data

> Langkah-langkah:
  - Install env & packages python terlebih dahulu
  - Ambil data dari API publik (misalnya, data cuaca dari OpenWeatherMap)
  - Bersihkan data menggunakan Pandas
  - Simpan ke database SQLite
  - Buat script Python untuk otomatisasi


= Install env & packages python =
sudo apt install python3-venv
python3 -m venv python-env
source python-env/bin/activate
pip install requests
pip install pandas
