'''
# 1 способ записи данных

colors = ['red', 'green', 'blue'] # в качестве источника данных выступает список
data = open('file.txt', 'a')      # создаем текстовую переменную data и связываем ее с текстовым файлом
data.writelines(colors)           # будем записывать colors (разделителей не будет)
data.close()                      # закрываем связанный файл

# запускаем код и создается file.txt в нем добавлена запись redgreenblue
# повторный запуск скрипта добавить еще раз redgreenblueredgreenblue
# модификатор w перезаписывает запись


data.write('\nLINE 2\n') добавит запись с новой строки

# 2 способ записи данных

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n') # запуск привел к перезаписи текста в file.txt
'''
    

