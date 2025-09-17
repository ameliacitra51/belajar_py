print (26)
print (3.14)
print(False)
print(1, 2, 3)
print([1, 2, 3]) #tipe data List
print((1, 2, 3)) #tipe data Tuple
print({"Nama" : "Citra", "kelas" : 12}) #tipe data Dictionary

#tipe data Dictionary dimasukan ke dalam variabel biodata
biodata = {"Nama" : "Citra", "Kelas" : 11}
print(biodata)
print(type(biodata)) #fungsi untuk mengecek jenis tipe data. akan tampil <class 'dict'> yang berarti dict adalah tipe data dictionary

#tipe data string
name = "citra ameli"
message = "citra belajar python"
print ("name[1]", name[1])
print ("message[2:5]", message[2:5])

#mengupdate string
pesan = "haii galang"
print ("update nih : ", pesan[:6] + "python")
