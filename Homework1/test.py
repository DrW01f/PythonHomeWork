def quicksort(array):
    if len(array) < 2: #Если остался только один элемент, то сортировка не нужна
        return array
    else: # Иначе берем элемент с индексом 0 
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] #и добавляем в список все остальные элементы меньше нулевого
        greater = [i for i in array[1:] if i > pivot]# больше нулевого
        print(quicksort(less) + [pivot] + quicksort(greater))
        return quicksort(less) + [pivot] + quicksort(greater)# сортируем (возвращаем)  левую половину (которые меньшен нулевого), нулевой элемент и правую половину()


print(quicksort([10, 5, 3, 2]))


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1