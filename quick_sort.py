#!/usr/bin/env python3

def quick_sort(list, start, end):
    if end <= start:
        return
    mid_point = partition(list, start, end)
    quick_sort(list, start, mid_point - 1)
    quick_sort(list, mid_point + 1, end)
    return list



def partition(list, start, end):

    pivot_index = start
    pivot = list[start]
    start = pivot_index + 1

    while True:

        while list[start] < pivot and start < end:
            start += 1
        while list[end] > pivot and end > pivot_index:
            end -= 1
        if end <= start:
            list[pivot_index], list[end] = list[end], list[pivot_index]
            break

        list[start], list[end] = list[end], list[start]

    return end


list = [23,12,42,45,231,423,142,245,3]
       #[23,12,3,45,231,423,142,245,42]
       #[3,12,23,45,231,423,142,245,42]
       #[3,12] [45,231,423,142,245,42]
       #[]

quick_sort(list, 0, len(list) - 1)
print(list)
#print(partition(list, 0, len(list) - 1))
