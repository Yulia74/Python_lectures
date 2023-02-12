# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
print(a)

b = 1 != 2
print(b)

c = 'qwe'
d = 'qwe'
print(a == b)

e = [1, 2]
f = [1, 2]
print(e == f)

func = 1
T = 4
x = 123
print(func < T > x)

i = 1 > 2 or 4 < 6
print(i)

u = [1, 2, 3, 4]
print(u)
print(not 2 in u)

is_odd = not u[0] % 2
print(is_odd)
