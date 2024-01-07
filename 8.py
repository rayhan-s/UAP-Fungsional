def kelipatan_tiga(angka):
    return angka % 3 == 0
tiga = list(filter(kelipatan_tiga, range(50)))

print(tiga)
