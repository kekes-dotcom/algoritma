berat = int(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))


# Menghitung BMI
bmi = berat / tinggi ** 2

print(bmi)

# Menentukan kategori
if bmi <= 18.5:
   kategori=("kurus(underweight)")
if bmi >= 20.5:
   kategori=("normal(ideal)")
if bmi >= 25.5:
   kategori=("gemuk(overweight)")
   
print(f"Kategori {kategori}")