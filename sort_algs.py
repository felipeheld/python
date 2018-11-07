#!/usr/bin/env python3
"""quick_sort"""
def quick_sort(unordered_list, start, end):
    if end - start <= 0:
        return
    else:
        partition_point = partition(unordered_list, start, end)
        quick_sort(unordered_list, start, partition_point - 1)
        quick_sort(unordered_list, partition_point + 1, end)

def partition(unordered_list, start, end):
    pivot_index = start
    pivot = unordered_list[pivot_index]
    greater_than_pivot_index = start + 1
    less_than_pivot_index = end

    while True:
        while unordered_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < end:
            greater_than_pivot_index += 1
        while unordered_list[less_than_pivot_index] > pivot and less_than_pivot_index > pivot_index:
            less_than_pivot_index -= 1
        if greater_than_pivot_index < less_than_pivot_index:
            unordered_list[greater_than_pivot_index], unordered_list[less_than_pivot_index] = unordered_list[less_than_pivot_index], unordered_list[greater_than_pivot_index]
        else:
            break

    unordered_list[pivot_index], unordered_list[less_than_pivot_index] = unordered_list[less_than_pivot_index], unordered_list[pivot_index]
    print(list)
    return less_than_pivot_index

# quick sort test #
list = [45,2,14,12,43,415,342,1,41]
#quick_sort(list, 0, len(list) - 1)
#print(list)
#quick_sort(list, 0, len(list) - 1)
#print(list)
# quick sort test #

"""merge_sort"""
def merge_sort(unordered_array):
    if len(unordered_array) == 1:
        return unordered_array
    mid_point = len(unordered_array) // 2
    left_half = unordered_array[:mid_point]
    right_half = unordered_array[mid_point:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def merge(left, right):
    l = r = 0
    result_array = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result_array.append(left[l])
            l += 1
        else:
            result_array.append(right[r])
            r += 1
    if l < len(left):
        result_array.extend(left[l:len(left)])
    elif r < len(right):
        result_array.extend(right[r:len(right)])
    return result_array

# merge sort test #
#ordered_list = merge_sort(list)
#print(ordered_list)
# merge sort test #
