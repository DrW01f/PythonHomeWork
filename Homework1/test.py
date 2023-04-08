# def quicksort(array):
#     if len(array) < 2: #Если остался только один элемент, то сортировка не нужна
#         return array
#     else: # Иначе берем элемент с индексом 0 
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot] #и добавляем в список все остальные элементы меньше нулевого
#         greater = [i for i in array[1:] if i > pivot]# больше нулевого
#         print(quicksort(less) + [pivot] + quicksort(greater))
#         return quicksort(less) + [pivot] + quicksort(greater)# сортируем (возвращаем)  левую половину (которые меньше нулевого), нулевой элемент и правую половину()


# print(quicksort([10, 5, 3, 2]))


def merge_sort(nums):
    if len(nums) > 1: #Если больше одного элемента, то сортируем
        mid = len(nums) // 2
        left = nums[:mid] #берем левую половину
        right = nums[mid:]  #берем правую половину
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: #Если элемент левой половины меньше, то записываем в новый массив 
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j] #Если элемент ПРАВОЙ половины меньше, то записываем в новый массив 
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


mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')