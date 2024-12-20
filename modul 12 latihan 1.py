#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:39:02 2024

@author: adesintia
"""

import pandas as pd

# Membaca data dari file CSV
file_path = "Negara.csv"  # Nama file CSV
df = pd.read_csv(file_path)

# Menampilkan data
print("Data Negara:")
print(df)

# Menghitung Mean (Rata-rata)
mean_values = df.mean(numeric_only=True)
print("\nRata-rata (Mean):")
print(mean_values)

# Menghitung Standar Deviasi
std_dev_values = df.std(numeric_only=True)
print("\nStandar Deviasi:")
print(std_dev_values)