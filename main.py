#!/usr/bin/env python3

import requests
import sqlite3
import pandas as pd

# 1. ambil data dari API
url = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&daily=temperature_2m_max&timezone=auto"
response = requests.get(url)
data = response.json()

# 2. bersihkan data
df = pd.DataFrame(data["daily"])
df["date"] = pd.to_datetime(df["time"])

# 3. simpan ke database SQLite
conn = sqlite3.connect("weather.db")
df.to_sql("weather", conn, if_exists="replace", index=False)

print("data berhasil disimpan")