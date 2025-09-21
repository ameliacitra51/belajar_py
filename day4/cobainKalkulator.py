#buat fungsinya
def tambah(a, b):
    return a + b

def kurang(c, d):
    return c - d

def kali(e, f):
    return e * f

def bagi(g, h):
    if h == 0:
        return "Tidak bisa dibagi 0 weyy!"
    return g / h

print("Pilih operasi:")
print("1. +")
print("2. -")
print("3. x")
print("4. /")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == "2":
    print("Hasil:", kurang(angka1, angka2))
elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil:", bagi(angka1, angka2))
else:
    print("Tidak ada pilihan lain")