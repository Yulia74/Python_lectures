# Списки: введение
# list = list если тип данных range, то его надо
# трансформировать в list

numbers = [1, 2, 3, 4, 5]  # инициируем переменную с типом список
print(numbers)            # [1, 2, 3, 4, 5]
ran = range(1, 6)         # инициируем переменную с типом range
print(range)              # <class 'range'> выведет в консоль
print(type(ran))          # смотрим тип данных переменной ran
num = list(ran)           # команда, меняющая тип данных с range на list
print(num)
print(type(num))

print(numbers)                # [1, 2, 3, 4, 5]
print(len(numbers))           # 5 размер списка через функцию len
print(f'{len(numbers)} len')  # вывести размер списка через интерполяцию
print(numbers[0])             # обращение к элементу списка по индексу
numbers[0]=10                 # присваиваем новое значение 1 элементу списка
print(numbers)                # [10, 2, 3, 4, 5]

for i in numbers:             # при работе со списком в цикле
    i*=2                      # элементам присваивается новое значение
    print(i)                  # [20, 4, 6, 8, 10]
print(numbers)                # [10, 2, 3, 4, 5]
                              # при выходе из цикла возвращаются первоначальные          
                              # значения элементов
colors = ['red', 'green', 'blue']
for e in colors:
    print(e)                  # red green blue

for e in colors:              # redred greengreen blueblue
    print(e*2)

colors.append('gray')         # добавить в конец
print(colors)                 # red green blue gray
print(colors == ['red', 'green', 'blue', 'gray']) # True

# colors.remove('red')         # удалить элемент 1 вариант кода
del colors[0]          
print(colors)   
