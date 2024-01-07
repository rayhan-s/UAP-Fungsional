data_tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

def data(data_tuple):
    names = [data_tuple[i] for i in range(0, len(data_tuple), 2)]
    prices = [data_tuple[i] for i in range(1, len(data_tuple), 2)]
    return names, prices

def dictionary(names, prices):
    result_dict = dict(zip(names, prices))
    return result_dict

names, prices = separate_data(data_tuple)
result_dict = create_dictionary(names, prices)

print("1. Data tuple:")
print(data_tuple)
print("\n2. Fungsi untuk memisahkan data tuple:")
print(names, prices)
print("\n3. Fungsi untuk membuat dictionary:")
print(result_dict)
