def hitung_pangkat(pangkat):
    def pangkat_dari(angka):
        return angka ** pangkat

    return pangkat_dari

pangkat_dua = hitung_pangkat(2)

pangkat_tiga = hitung_pangkat(3)

hasil_pangkat_dua = pangkat_dua(4)
hasil_pangkat_tiga = pangkat_tiga(5)

print("Hasil pangkat dua dari 4:", hasil_pangkat_dua)
print("Hasil pangkat tiga dari 5:", hasil_pangkat_tiga)
