"""
List comprehension — это упрощенный подход к созданию списка, который задействует
цикл for, а также инструкции if-else для определения того, что в итоге окажется
в финальном списке.

Задача. Создать список, состоящий из чисел в диапазоне от 1 до 100.



list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)               # [1, 2, 3,..., 100]
"""

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1) 

# Добавляем условие: только четные

list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
print(list_1) 

# Добавляем условие: создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
print(list_1) 

# Можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)           # [0, 4, 8, 12, 16]