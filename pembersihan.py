import pandas as pd

# Buat DataFrame contoh dengan data numerik
data = {'Usia': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]}
df = pd.DataFrame(data)

# Tentukan batasan interval
batas_interval = [0, 30, 40, 50, 60, 100]

# Tentukan label untuk masing-masing interval
label_interval = ['<30', '30-40', '40-50', '50-60', '60+']

# Gunakan pd.cut untuk melakukan binning
df['Kelompok Usia'] = pd.cut(df['Usia'], bins=batas_interval, labels=label_interval)

# Cetak hasil binning
print("Data dengan Binning:")
print(df)
