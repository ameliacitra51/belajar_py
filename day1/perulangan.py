#while loop
count = 0
while (count < 9):
  print ("Ini angka ke: ", count)
  count = count + 1

print ("Good bye!")

#for loop
#for yang sederhana
number = [1, 2, 3, 4, 5, 6]
for x in number:
  print(x)

fruits = ["alpukat", "jeruk", "nanas", "apel"]
for food in fruits:
  print("citra suka buah", food)

#nested loop
i = 2
while(i < 100):
  j = 2
while(j <= (i/j)):
  j = j + 1
  if(j > i/j) : print(i, "is prime")
  i = i = 1
print("see u!")