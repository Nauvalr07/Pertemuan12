nama = "Nauval Ramadhan Krisani"
nim = "0110124171"
rombel = "SI07"
no_telepon = "085717904240"
alamat = """bogor """
print(nama)
print(nim)
print(rombel)
print(no_telepon)
print(alamat)

nama = "fikriyana ferdinand"
nim = "0110124158"
rombel = "SI09"
no_telepon = "089687167497"
alamat = """bogor"""
print('\nnama aku', nama, '\nnim aku', nim, '\nrombel aku', rombel, '\nno_telepon aku', no_telepon, '\nalamat aku', alamat)

berat_badan = int(input('Berat Badan (kg) : '))
tinggi_badan = int(input('Tinggi Badan (cm) : '))


tinggi_badan = tinggi_badan/100


nilai_bmi = berat_badan / (tinggi_badan**2)

print('Nilai BMI anda : ',nilai_bmi)
  
if nilai_bmi < 18.5:
	print('Berat badan anda kurang ')
elif nilai_bmi > 18.5 and nilai_bmi < 24.9:
	print('Berat badan anda normal')
elif nilai_bmi > 25 and nilai_bmi < 29.9:
	print('Anda kelebihan berat badan')
elif nilai_bmi > 30:
	print('Anda obesitas')

#Nilai Celcius
celcius = int(input("Masukan suhu dalam celcius:"))
fahrenheit = (celcius * 9/5) + 32

print("suhu dalam celcius:", celcius, "C")
print("suhu dalam fahrenheit:", fahrenheit, "F" )

r = int(input("Masukkan jari - jari    ="))
t = int(input("Masukkan Tinggi         ="))
la = int(input("Masukkan Luas Alas     ="))
Ka = int(input("Masukkan Keliling Alas ="))

phi =22/7

luas = (2*la)+(Ka*t)
volume = phi*r*r*t

print("Luas Tabung Adalah = ", luas)
print("Volume Tabung Adalah =", volume)