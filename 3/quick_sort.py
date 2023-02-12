# Алгоритм "быстрая сортировка". Отсортировать массив [10, 5, 3, 2]

def quick_sort(array):
    if len(array) <=1:   # базис рекурсии
       return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    # print(array)       # можно включить строку и посмотреть этапы рекурсии
    return quick_sort(less) + [pivot] + quick_sort(greater)
# pivot из int преобразовали в [] чтобы не показывало ошибку

print(quick_sort([5, 10, 3, 2])) # [2, 3, 5, 10]

'''
1-е повторение рекурсии:
    array = [5, 10, 3, 2]
    pivot = 5
    less = [3, 2]
    greater = [10]
    return quick_sort([3, 2] + [5] + quick_sort[10]) # [3, 2] [5] [10]
2-е повторение рекурсии:
    array = [3, 2]
    pivot = 3
    less = [2]
    greater = []
    return quick_sort([2] + [3] + quick_sort[]) # [2] [3] [5] [10]
# Важно! Помимо вызова рекурсии добавляются списки [5] и [10]
3- е повторение рекурсии:
    array = [2]
    return [2] # сработал базовый случай рекурсии и она остановилась
получаем список
[2, 3, 5, 10]  



'''
