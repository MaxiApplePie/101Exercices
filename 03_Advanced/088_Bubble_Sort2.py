def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort) - 1, 0, -1):
        for j in range(i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort


l = [40, 16, 80, 2, 90]
print(l)
print(bubble_sort(l))
