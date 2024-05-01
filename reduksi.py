import pandas as pd

# Buat DataFrame contoh
data = {'ID': range(1, 101), 'Nilai': range(101, 201)}
df = pd.DataFrame(data)

# Mengambil sampel data
sample_size = 20  # Jumlah sampel yang ingin diambil
df_sample = df.sample(n=sample_size, random_state=42)  # Mengambil sampel acak dengan seed 42

# Cetak hasil reduksi data
print("Sampel Data:")
print(df_sample)
