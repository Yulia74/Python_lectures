''''
В списке хранятся числа. Нужно выбрать только чётные числа и составить
список пар (число; квадрат числа).

Input:  [1, 2, 3, 5, 8, 15, 23, 38]

Output: [(2, 4), (8, 64), (38, 1444)]


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []       #  а можно list(); 
#                #  создали список res, в который будем выводить результа
# for i in data :
#     if i % 2 == 0:
#         res.append((i, i ** 2)) # передаем в список в виде кортежей
# print(res)

# запишем код с помощью применения lambda функции

def select(f, col):            # функция, в которую передаем фукнцию f и какое-то значение col
    return[f(x) for x in col]  # она будет возращать список, в котором каждому элементу будем применять
                               # функцию f(x), но мы должны будем пройти по всем элементам col
                               # (мы передаем список и функцию, она ко всем элементам применяет функцию)
def where(f, col):
    return[x for x in col if f(x)] # функция возвращает список из x,если мы пройдемся по всем элементам col                              
                                   # но возращать только те элементы, которые прошли проверку условия функции f(x)
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)           # список res создается вызовом функции select (int)-указывает, что мы желаем  
                                  # привести все к целочисленному типу, на вход принимает список data
print(res)   # [1, 2, 3, 5, 8, 15, 23, 38] возрващает все элементы списка

res = where(lambda x: x % 2 == 0, res) # вновь обращаемся к списку res, но уже будем делать выборку через вызов
                                   #  функции where. Cоздаем функцию lambda, которая принимает значение x  
                                   # и возвращает либо thrue либо false, условии деления на 2 на цело и так же передаем res
print(res) #[2, 8, 38] возвращает только четные значения x, но без возведения в квадрат
res = list(select(lambda x: (x, x**2), res))   # для того чтобы все ^2, вновь обращаемся к списку res и изменяем его
                                         # вновь обращаемся к функции select, в которую передаем первый аргумент:
                                         # функция lambda х, для кортежа из x и x**2 (х возведенный в квадрат), 
                                         # не забываем передать в функцию select список res
                                         # говоря проще: мы хотим преобразовать список res и вернуть значения в виде 
                                         # кортежей добавляем впереди select list(), чтобы получить в виде типа список
print(res)     # [(2, 4), (8, 64), (38, 1444)]


# c помощью map() можно сделать этот код лучше, он позволит избавиться от функции select()

# удалим строки, где мы задаем функцию select(), в оставшихся строках заменим функцию select()
# на map(). Map() это встроенная функция Python
# по сути функция select() эта таже функция map(), просто функцию select() мы прописали явно, 
# а функция map() прописана в модулях.

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
'''
# фукнция where() похожа на функцию filter(), упростим вышенаписанный код

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = filter(lambda x: x % 2 == 0, data)
res = list(map(lambda x: (x, x ** 2), res))
print(res)         # [(2, 4), (8, 64), (38, 1444)]