"""
Tugas Praktikum Kecerdasan Buatan-Pert 1
Nama:Rajendra Rangga Priyatama
NIM:H1D024020
Tema:Sistem Analisis Nilai Mahasiswa
"""

import random
import numpy as np

#1.STRUKTUR DATA
info_praktikum={
    "judul":"Analisis Nilai KB",
    "mahasiswa_list":["Jamal","Sumanto","Agree","Wahyu","Putro"]
}
daftar_nilai=[]
print(f"=== {info_praktikum['judul']} ===\n")

#2.STRUKTUR KONTROL
for nama in info_praktikum["mahasiswa_list"]:
    skor=random.randint(65, 95) 
    daftar_nilai.append(skor)
    print(f"Mahasiswa:{nama}|Nilai:{skor}")

#3.IMPLEMENTASI LIBRARY
array_skor=np.array(daftar_nilai)
rata_rata=np.mean(array_skor)
print("-"*30)
print(f"Rata-rata Kelas:{rata_rata:.2f}")

#4.STRUKTUR KONTROL
if rata_rata>=80:
    print("Predikat:Kelas A (Sangat Memuaskan)")
elif rata_rata>=70:
    print("Predikat:Kelas B (Baik)")
else:
    print("Predikat:Kelas C (Cukup)")