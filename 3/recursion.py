'''
Пользователь вводит число n. Необходимо вывести n - первых членов 
последовательности Фибоначчи. Решить задачу, используя рекурсию.

'''

def fib(n):           # создаем метод (рекурсию)
    if n in [1, 2]:    # базис рекурсии, т.е. условие выхода из нее
        return 1
    return fib(n-1) + fib(n-2) # сама рекурсия (формула расчета)

list_1 = []              # создаем список, в который будем записывать результат
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)               # [1, 1, 2, 3, 5, 8, 13, 21, 34]