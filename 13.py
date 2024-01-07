# TODO 1: Tambahkan library yang dibutuhkan
import matplotlib.pyplot as plt

# Setiap tupel berisi informasi sebagai berikut:
# (jenis_kendaraan, penggunaan_energi_per_km, biaya_operasional_per_km)
data = [
    ('Bus', 5, 200),
    ('Trem', 8, 150),
    ('Kereta', 12, 300),
    ('Minibus', 6, 180),
    ('Tram', 9, 220)
]

# TODO 2: Pisahkan Data masing-masing (dapat menggunakan pemetaan)
jenis_kendaraan, penggunaan_energi, biaya_operasional = zip(*data)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
# TODO 3: Lengkapi kode untuk visualisasi data penggunaan energi
plt.bar(jenis_kendaraan, penggunaan_energi, color='skyblue')
plt.title('Penggunaan Energi per KM')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Penggunaan Energi per KM')

plt.subplot(1, 3, 2)
# TODO 4: Lengkapi kode untuk visualisasi data biaya operasional
plt.bar(jenis_kendaraan, biaya_operasional, color='lightcoral')
plt.title('Biaya Operasional per KM')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Biaya Operasional per KM')

plt.subplot(1, 3, 3)
# TODO 6: Lengkapi kode untuk menggambar Scatter plot
# TODO 7: Memberikan label pada tiap titik
plt.scatter(penggunaan_energi, biaya_operasional, color='green', label='Data Kendaraan')
plt.title('Scatter Plot: Penggunaan Energi vs Biaya Operasional')
plt.xlabel('Penggunaan Energi per KM')
plt.ylabel('Biaya Operasional per KM')

# TODO 7: Menambahkan label pada tiap titik
for i, jenis in enumerate(jenis_kendaraan):
    plt.annotate(jenis, (penggunaan_energi[i], biaya_operasional[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Menambahkan legenda
plt.legend()

# Tampilkan plot
plt.tight_layout()
plt.show()
