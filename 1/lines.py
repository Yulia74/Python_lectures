# работа в цикле со строками

text = 'съешь ещё этих мягких французских булок'

print(len(text))      # 39 количество символов (с пробелами!)
print('ещё' in text)  # True наличие слова "еще" в тексте
print(text.isdigit())  # False наличие цифр в тексте
print(text.islower())  # True наличие символов в нижнем регистре
print(text.replace('ещё', 'ЕЩЁ'))  # замена слов

print(text[0])             # вызов 1 символа в тексте
# print(text[len(text)])   # IndexError  нумерация с 0
print(text[len(text)-1])   # к  последний элемент текста
print(text[-5])            # б отстчет в обратную сторону с конца текста
print(text[:])             # выводит весь текст (сахар)
print(text[:2])            # съ  интервал символов (0 можно не писать)
print(text[len(text)-2:])  # ок
print(text[2:9])           # ешь ещё
print(text[6:-18])         # еще этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6])           # сеикакл
text = text[2:9] + text[-5] + text[:2]
