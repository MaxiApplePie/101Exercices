import sys
import time


def bubble_sort(list_to_sort):
    success = False
    while not success:
        success = True
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                # Permutation
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                # print(f'Permutation efectuée avec i = {i}.')
                # print(list_to_sort)
                # time.sleep(2)
                success = False
                break
    return list_to_sort


l = [40, 16, 80, 2, 90]
print(l)
print(bubble_sort(l))
