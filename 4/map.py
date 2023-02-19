'''
Функция map() принимает на вход 2 аргумента: 1 - сама функция, которую мы передаем;
2 - объект. Функция map() применяет указанную функцию к каждому элементу
итерируемого объекта и возвращает итератор с новыми объектами.
'''

list_1 = [x for x in range(1, 20)] # заполним через генератор списков
print(list_1)  
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

list_1 = list(map(lambda x: x + 10, list_1)) 
# list_1 равен новому списку list в котором мы будем вызывать функцию map()
# и применять к ней функцию, которую мы опишем через функцию lambda
print(list_1)  
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]