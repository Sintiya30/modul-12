#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:29:28 2024

@author: adesintia
"""

import pandas as pd

# Data awal
data = {
    "Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", 
               "Rusia", "Meksiko", "Nigeria", "Jerman", "Aljazair", "Inggris"],
    "Luas": [1905, 377, 3287, 9597, 9834, 8515, 1709, 1964, 923, 357, 2381, 242],
    "Populasi": [264, 143, 1252, 1357, 329, 210, 146, 126, 200, 83, 43, 66]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung rata-rata dan standar deviasi
mean_data = df[["Luas", "Populasi"]].mean()
std_data = df[["Luas", "Populasi"]].std()

# Membuat DataFrame untuk rata-rata
mean_df = pd.DataFrame({
    "Deskripsi": ["Mean"],
    "Luas": [f"{mean_data['Luas']:.2f}"],
    "Populasi": [f"{mean_data['Populasi']:.2f}"]
})

# Membuat DataFrame untuk standar deviasi
std_df = pd.DataFrame({
    "Deskripsi": ["Standard Deviation"],
    "Luas": [f"{std_data['Luas']:.2f}"],
    "Populasi": [f"{std_data['Populasi']:.2f}"]
})

# Menyimpan ke file CSV
mean_df.to_csv("NegaraMean.csv", index=False)
std_df.to_csv("NegaraStandarDeviasi.csv", index=False)

# Menampilkan hasil di terminal
print("File NegaraMean.csv dan NegaraStandarDeviasi.csv telah dibuat!\n")

print("Isi file NegaraMean.csv:")
print(mean_df.to_markdown(index=False))

print("\nIsi file NegaraStandarDeviasi.csv:")
print(std_df.to_markdown(index=False))