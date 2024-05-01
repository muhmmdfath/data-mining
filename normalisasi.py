import numpy as np

# Data contoh (misalnya, data tinggi dalam sentimeter)
data_tinggi = [160, 170, 155, 180, 150]

# Normalisasi Min-Max
def min_max_normalisasi(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data

normalized_tinggi = min_max_normalisasi(data_tinggi)

# Cetak hasil normalisasi
print("Data Tinggi Asli:", data_tinggi)
print("Data Tinggi Setelah Normalisasi Min-Max:", normalized_tinggi)

# Normalisasi Z-Score
def z_score_normalisasi(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    normalized_data = [(x - mean) / std_dev for x in data]
    return normalized_data

normalized_tinggi_z_score = z_score_normalisasi(data_tinggi)

# Cetak hasil normalisasi Z-Score
print("Data Tinggi Setelah Normalisasi Z-Score:", normalized_tinggi_z_score)
