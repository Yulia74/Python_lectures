# Функции

def f(x):              # миксуем типы возвращаемых данных
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1                 # <class 'str'>
print(f(arg))           # если arg = 2.3 <class 'int'>
print(type(f(arg)))     # если arg = 2 <class 'NoneType'>
