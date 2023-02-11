# типы данных и переменная
# int, float, boolean, str, list, None

a = 123
b = 1.23
print(a)       # показать переменную
print(type(a)) # показать тип данных
print(b)
print(type(b))
value = None
print(type(value))
value = 1234
print(type(value))
s = 'hello world'  # \n - переход на новую строку
print(s)
print(type(s))

print(a, b, s)             # варианты вывода строк
print(a, '-',b, '-', s)    
print('{} - {} - {}'.format(a,b,s))
print(f'{a} - {b} - {s}')  # интерполяция
print('{1} - {2} - {0}'.format(a,b,s)) # менять последовательность вывода

f = True
print(f)
e = False
print(e)

list = [1,2,3]
col = ['hello', 1,2,3,4,True]
print(list)
print(col)
