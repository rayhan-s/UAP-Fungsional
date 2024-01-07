from functools import reduce

def kelipatan_tiga(angka):
    return angka % 3 == 0

tiga = list(filter(kelipatan_tiga, range(51)))

total = reduce(lambda x, y: x + y, tiga)

print(total)
