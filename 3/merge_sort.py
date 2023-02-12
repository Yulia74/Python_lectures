# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1: # не создаем базис рекурсии, а показываем условие когда она выполняется (пока не останется по 1 элементу)
        mid = len(nums) // 2 # создаем переменную, путем деления размера списка на цело на 2
        left = nums[:mid]    # срез списка (левая часть от mid)
        right = nums[mid:]   # срез списка (правая часть от mid)
        merge_sort(left)     # создаем рекурсию для левой части (деление на 2)
        merge_sort(right)    # создаем рекурсию для правой части (деление на 2)
        i = j = k = 0        # создаем 3 переменных: i для left, j для rigth, k для общего списка
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i] # cоздаем пары чисел
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):   # если в каком-либо списке остались значения без пары
            nums[k] = left[i]  # c помощью двух этих условий добавляем их в конец
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)