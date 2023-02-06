# Множества - хранилище данных, которое содержит в себе 
# уникальные элементы (может быть как упорядоченным, так и нет)

q = set()           # создаем множество

colors = {'red', 'green', 'blue'}
print(type(colors)) # class 'set'
print(colors)       # {'green', 'blue', 'red'}

colors.add('red')   # добавить элемент ничего не добавит, так как 'red' уже есть
                    # а множество это хранилище уникальных элементов
print(colors)       # {'red', 'blue', 'gray'}


colors.add('gray')  # добавить элемент
print(colors)       # {'red', 'blue', 'gray', 'green'}
colors.remove('red')# удалить элемент
print(colors)       # {'gray', 'green', 'blue'}
#colors.remove('red')# KeyError: 'red'  ошибка, т.к. элемента уже нет
colors.discard('red')# ok функция, которая проверяет наличие элемента в множестве, если
                     # он есть, то удаляет, если нет, то пропускает и дает ошибку
print(colors)        # {'gray', 'blue', 'green'}
colors.clear()       # очистка множества, оно стало пустое
print(colors)        # set() можно продолжить работу с пустым множеством


