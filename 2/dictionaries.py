# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу.
# в списках и кортежах мы обращаемся к элементам по индексам, в словарях эту роль
# выполняют ключи.

dictionary = {} # создали пустой словарь \ (обратный слэш на второй строке, нужен для того,
                # чтобы не писать все в одну строку)
d = dict()      # также создает пустой словарь
dictionary = \
    {
        'up': '1',
        'left': '2',
        'down': '3',
        'right': '4'
    }
print(dictionary) # {'up': '1', 'left': '2', 'down': '3', 'right': '4'}
print(dictionary['left']) # 2

for k in dictionary.keys(): # проходимся циклом по коллекции ключей
    print(k)                # up
                            # left
                            # down
                            # right
for k in dictionary.values(): # если хотим посмотреть на конкретные значения
    print(k)                #  1
                            # 2
                            # 3
                            # 4          
for v in dictionary: # если хотим пройтись по циклу и увидеть все значения нашего словаря
    print(v)                # up
                            # left
                            # down
                            # right
    print(dictionary[v])  
# up
# 1
# left
# 2
# down
# 3
# right
# 4        

del dictionary['left'] # удаление элемента                          
print(dictionary)      # {'up': '1', 'down': '3', 'right': '4'}

for item in dictionary:
    print('{}: {}'.format(item,dictionary[item]))
# up: 1
# down: 3
# right: 4

d={}                  # создала словарь
d['q'] = 'qwerty'     # в словаре d под ключом 'q' будет находиться значение 'qwerty'
print(d)              # {'q': 'qwerty'}

d['w'] = 'werty'      # добавила еще один элемент словаря
print(d)              # {'q': 'qwerty', 'w': 'werty'}
print(d['w'])         # werty

d[987] = 485609       # добавали ключ другого типа (int) в словарь {'q': 'qwerty', 'w': 'werty', 987: 485609}
print(d)

print(d.items())      # dict_items([('q', 'qwerty'), ('w', 'werty'), (987, 485609)]) получаем список, 
for (k,v) in d.items():  # где каждый элемент является кортежем из двух значений: ключа и элемента словаря
    print(k,v)     