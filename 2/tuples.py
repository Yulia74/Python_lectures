# Кортеж - это некий неизменяемый список. Используется в случае задиты каких-либо
# данных от изменений (намеренных или случайных). Кортеж по сравнению со списком
# занимает меньше места и работает быстрее.

a, b = 3, 4      # это множественное присваивание значения переменных
(a) = (3, 4)     # а если все обрамим в скобочки, то получим кортеж
print(a)         # (3, 4)
print(a[0])      # можно обратиться по индексу, получим 3
(b) = (3, 1, 41, 4)
print(b[-2])     # 41

# но если мы пожелаем присвоить какому-то элементу другое значение,
# то это не получится, потому что это неизменяемый список !
# a[0] = 12 # не получится

t = ()
print(type(t))    # class 'tuple'
# если хотим создать кортеж из одного элемента, иначе t = (1) будет число
t = (1, )
print(type(t))    # class 'tuple'
t = (1)
print(type(t))    # class 'int'
t = (28, 9, 1990)
print(type(t))    # class 'tuple'
colors = ['red', 'green', 'blue']
print(colors)     # ['red', 'green', 'blue']
t = tuple(colors)
print(type(t))    # class 'tuple
print(t)          # ('red', 'green', 'blue')

# работа с кортежами в циклах

c = (3, 4, 5)
for item in c:
    print(item)
# 3 
# 4
# 5

# действия с кортежами из текстовых данных

t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green

for e in t:
    print(e)
# red
# green
# blue

# t[0] = 'black' # не даст переименовать так как это кортеж

# двойное преобразование (возможность "распаковать" кортеж в отдельные переменные)
t = tuple(['red', 'green', 'blue']) # создаем список [] преобразуем его в кортеж ()
red, green, blue = t # распаковываем кортеж, переводим в независимые переменные
# и далее с ними работаем, как с отдельными переменными
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# преобразование списка в кортеж
v = [1,8,9]
print(v)           # [1, 8, 9]
print(type(v))     # class 'list'

v=tuple(v)
print(v)           # (1, 8, 9)
print(type(v))     # class 'tuple'

# распаковка кортежа на переменные
a, b, c = v  
print(a,b,c)       # 1 8 9
print(type(a))     # class 'int'
