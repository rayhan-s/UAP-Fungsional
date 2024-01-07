def sisagold(operation):
    def wrapper(a, b):
        return operation(a, b)
    return wrapper

def kurang(a, b):
    return a - b

hasil_kurang = sisagold(kurang)
result = hasil_kurang(10, 4)
print(result)
