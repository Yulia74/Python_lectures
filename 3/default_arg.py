'''
Очень важно понимать одну вещь, сколько аргументов мы передаем, столько и
принимаем. Или наоборот сколько аргументов мы принимаем, столько и передаем.
В нашем случае функция sum_numbers принимает 1 аргумент(n)



def sum_numbers(n, y='Hello'):  # вводим у по умолчанию, в print(n) не добавляем
    print(y)
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


n = int(input('Введите n: '))

print(sum_numbers(n))                # Hello
                                     # 15         
# print(sum_numbers(n, 'qwerty'))    # TypeError

'''

# а если необходимо добавить и в print(n)

def sum_numbers(n, y='Hello'):  
    print(y)
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


n = int(input('Введите n: '))

print(sum_numbers(n,'qwerty'))        # qwerty
                                      # 15
                                            


