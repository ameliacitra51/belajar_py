#membaca file csv dan nampilih 10 data
import pandas as pd

datanya = pd.read_csv('contohData.csv')

print(datanya.head(7))

#coba ambil data dari file json
cobain = pd.read_json('cobaData.json')
print(cobain.head(3))