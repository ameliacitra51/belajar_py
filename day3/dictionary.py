orang = {"nama": "lia", "umur": 18, "hobi": ["halu, scroll ige"]}
print("nama: ", orang["nama"])
print("umur: ", orang["umur"])
print("hobi: ", orang["hobi"])

#menambahkan data pada dictionary
orang["cita-cita"] = "sukses"
print(orang)

#looping key value pada dictionary
for key, value in orang.items():
    print(key, ":", value)

#line 2-4 untuk munculin secara manual, kalo pake looping jadi cepatt ga ribert