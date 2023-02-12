# передача неограниченного количество аргументов: требуется поставить * перед аргументами

def concatenatio(*params):
    res: str = ""      # тип данных строка
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(concatenatio(1, 2, 3, 4))        # TypeError

# если нужно работать с числами, тогда 4 строка должна иметь вид:
# res: int = 0 или res = 0
# print(concatenatio(1, 2, 3, 4))      уже не будет ошибки а выдаст 10