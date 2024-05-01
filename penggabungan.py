import pandas as pd

# Buat dua DataFrame contoh
data1 = {'ID': [1, 2, 3, 4],
         'Nama': ['Alice', 'Bob', 'joko', 'Dafa']}
data2 = {'ID': [3, 4, 5, 6],
         'Nilai': [85, 92, 78, 88]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Gabungkan DataFrame berdasarkan kolom 'ID'
df_merged = pd.merge(df1, df2, on='ID', how='inner')  # Inner join

# Cetak hasil penggabungan
print("Hasil Penggabungan:")
print(df_merged)
