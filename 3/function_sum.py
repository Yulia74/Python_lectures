'''
Создать функцию sum_numbers которая будет считать сумму всех элементов от 1 до n.


решение без return (внутри функции)



def sum_numbers(n):      # def - указание на функцию, sum_numbers - название фукции, 
    sum = 0              # n - принимаемая переменная
    for i in range(1, n+1):
        sum += i
    print(sum)           # выводим результат


n = int(input('Введите n: '))  # запрашиваем переменную

sum_numbers(n)           # вызываем функцию
'''


# решение через return

def sum_numbers(n):       
    sum = 0              
    for i in range(1, n+1):
        sum += i
    return sum           # return возвращает значение и завершает работу функции


n = int(input('Введите n: ')) 

print(sum_numbers(n))    # следовательно результат выводим через print (иначе мы его не увидим), 
                         # после завершения работы функции

# a = sum_numbers(5)     # другой вариант вывода результата
# print(a)