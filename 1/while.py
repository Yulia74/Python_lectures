# Получить инвертированное (перевернутое) число

original = 123
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

ori = 123
inv = 0
while ori != 0:
    inv = inv * 10 + (ori % 10)
    ori //= 10
    print(ori)
else:
    print('Пожалуй')
    print('хватит ')
print(inv)
