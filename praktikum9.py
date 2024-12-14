#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam
#print(celcius_ke_fahrenheit(0))   # Output: 32.0
#print (celcius_ke-fahrenheit(100)) # Output: 212.0

def celcius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

celcius1 = 0
print(f"hasilnya adalah {celcius_ke_fahrenheit(celcius1)}")
print(celcius_ke_fahrenheit(100))
print(celcius_ke_fahrenheit(1000))

print("======================")

#soal no 2
#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.

def is_genap(angka):
    return angka % 2 == 0

def is_genap(angka):
    hasil = angka % 2 == 0
    return hasil

genap = 4
print(f"output dari bilangan {genap} adalah {is_genap(genap)}")
print(is_genap(13))

#soal no 3
#buatlah fungsi untuk melihat keterangan lulus atau tidak lulus :
#nilai  (80) #lulus
#nilai(60) #gagal

def nilai_kelulusan(nilai):
    print()
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))
    

print("========================")
print("========================")
print("========================")


#soal no 4
#buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#bilangan(20) # 1,3,7,9,11,13,15,17,19
    