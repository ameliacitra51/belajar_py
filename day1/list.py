#mengakses nilai dalam list
list1 = ['matematika', 'ppkn', 2007, 1996]
list2 = [1, 2, 3, 4, 5, 6]

print("list1:", list1[1]) #munculnya ppkn karena index nya 1
print("list2:", list2[2:5]) #munculnya 3, 4, 5 karena mulainya dari index 2

#update nilai dalam list
list = ['mtk', 'arab', 2008, 1990]
print ('nilai ada pada index 3:', list[3])

list[2] = 2010
print('nilai baru ada pada index 2:', list[2])
print(list)

#menghapus nilai dalam list
list3 = ["citra", "amelia", 2006, 2003, 2009]
print(list3)

del list3[3]
print("nilai yang dihapus adalah index 3:", list3)