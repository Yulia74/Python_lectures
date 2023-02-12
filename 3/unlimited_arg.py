'''
Передача неограниченного количества аргументов в функцию


def sum_str(*args):       # указание *, позваляет добавлять 
    res = ''              # неограниченное количество аргументов
    for i in args:
        res += i
    return res

print(sum_str('q', 'w', 'e', 'r', 't' ))
print(sum_str('q', 'w', 'e', 'r', 't', 'y' ))
'''
# работа с int

def sum_num(*args):       # указание *, позваляет добавлять 
    res = 0               # неограниченное количество элементов
    for i in args:
        res += i
    return res


print(sum_num(1, 2, 3, 4)) # 10
print(sum_num(1, 2, 3, 4, 5)) # 15