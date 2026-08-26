# Contoh menggabungkan operator
akhlak = 30
nilai = input("50")
hadir = True

# Menggunakan operator aritmatika
nilai_akhir = akhlak + nilai
print(nilai_akhir)

# Lulus jika nilai >= 75 DAN hadir
lulus = nilai >= 75 and hadir
print("Lulus?", lulus)          # True

# Mendapat beasiswa jika nilai >= 90 ATAU juara lomba
beasiswa = nilai >= 90 or akhlak > 20
print("Dapat beasiswa?", beasiswa)