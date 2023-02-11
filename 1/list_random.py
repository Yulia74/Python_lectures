
# Заполнение списка через рандом



import random

n = int(input('Введите количество элементов множества '))

list_1 = []
for i in range(n):
    list_1.append(random.randint(1, 21))
print(*list_1)





