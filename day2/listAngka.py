angkaa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
semuanya = 0
for iniAngka in angkaa:
    semuanya += iniAngka
print("semua angka: ", semuanya) #hasilnyaa 136 karna di jumlahkan semua angka yg ada di variabel angkaa


#looping angak ganjil
for citra in range(1, 35):
    if (citra % 2) != 0:
        print("inilah angka ganjil citra: ", citra)

#kenapa yg line 5 dan 11 berbeda padahal sama" print
#karna line 5 itu menjumlahkan semua angka
#dan line 11 itu melakukan looping untuk nampilin angka ganjil