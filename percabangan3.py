# Contoh: Syarat Kelulusan dengan 2 kondisi
nilai = int(input("Nilai ujian  : "))
absen = int(input("Jumlah absen  : "))

if nilai >= 75:
    if absen <= 5:
        print("LULUS - Selamat!")
    else:
        print("TIDAK LULUS - Absen terlalu banyak")
else:
    print("TIDAK LULUS - Nilai di bawah KKM")