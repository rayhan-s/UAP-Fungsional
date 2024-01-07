def generate_kelipatan_tiga(batas):
    for angka in range(batas):
        if angka % 3 == 0:
            yield angka

angka_generator = generate_kelipatan_tiga(50)

for angka in angka_generator:
    print(angka)
