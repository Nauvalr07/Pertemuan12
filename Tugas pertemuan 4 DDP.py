# #program menentukan bilangan ganjil dan genap
# print('## 1. program bilangan ganjil dan genap ##')
# print('=========================================')

# #input bilangan 
# bilangan = int (input('masukan bilangan anda :'))

# if bilangan % 2 == 0:
#     print(bilangan, 'merupakan bilangan genap')
# else:
#     print(bilangan, 'merupakan bilangan ganjil')

# #program menentukan nilai ujian
# print('## 2. program menentukan nilai ujian ')
# print('=========================================')
# #input nilai
# nilai_ujian = int(input('masukan nilai anda : '))

# #proses dan output
# if nilai_ujian >= 75:
#     print('kamu dinyatakan lulus')
# else:
#     print('kamu dinyatakan tidak lulus')

#program menentukan usia dan status
print('## 3. program menentukan usia dan status')
print('=========================================')

#input usia dan status
usia = int(input('menentukan usia anda :'))

if usia >= 18:
    print('kamu dewasa')
elif usia >= 13 and usia <=17:
    print('kamu remaja')
else:
    print('kamu anak anak')

#program mentukan 
print('## 4. program status menentukan keanggotaan ##')
print()

#input: status
status_anggota =input("""daftar keanggotaan di bawah ini
1.gold
2.silver
3.bronze
masukan pilihan kamu: """)

#proses dan output
if status_anggota == 'gold' or status_anggota == 'silver':
    print('selamat anda mendapatkan diskon')
elif status_anggota == 'bronze' :
    print('maaf anda tidak mendapatkan diskon.')
else:
    print('masukan kata dengan benar')