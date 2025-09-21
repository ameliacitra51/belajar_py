def tambah(a, b):
    return a + b

hasil = tambah(4, 7)
print ("hasilnya adalahh", hasil)


def pengurangan(c, d):
    return c - d

samadengan = pengurangan(13, 8)
print ("hasilnya", samadengan)


def kali(i, j):
    return i * j

hasilkali = kali(7, 8)
print ("hasil perkaliannya", hasilkali)

#mengecek genap atau ganjil
def cek_angka(r):
    if r % 2 == 0:
        return "ini angka genap ya"
    else:
        return "ini angka ganjil ya"
print("jadi", cek_angka(9))

#konversi suhu
def konversi(c):
    return (c * 9/5) + 32 #rumus tetap celcius ke fahrenheit
print("30 c =", konversi(30), "f")

def konversi2(f):
    return (f - 32) * 5/9 #rumus tetap fahrenheit ke celcius
print("86 f =", konversi2(86), "c")

def konversi3(celcius):
    return (celcius + 273.15) #rumus tetap celcius ke kelvin
print("30 c =", konversi3(30), "k")

def konversi4(k):
    return (k - 273.15) #rumus tetap kelvin ke celcius
print("303 k =", konversi4(303), "c")

def konversi5(fahrenheit):
    return (fahrenheit + 459.67) * 5/9 #rumus tetap fahrenheit ke kelvin
print("86 f =", konversi5(86), "k")

def konversi6(kelvin):
    return (kelvin * 9/5) - 459.67 #rumus tetap kelvin ke fahrenheit
print("303 k =", konversi6(303), "f")

#banyak parameter
def dataku(nama, umur, keinginan):
    print("Nama:", nama)
    print("Umur:", umur)
    print("Keinginan:")
    for k in keinginan:
        print("-", k)
dataku("citra", 18, ["jadi selebgram", "jadi programmer", "jadi artis"])