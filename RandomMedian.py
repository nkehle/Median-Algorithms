# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import numpy as np
import QuickSortMedian

''' Purpose: Sort the arr and pick middle element
    Parameter1 -> Array
    Return     -> Median   '''
def find_median(arr, k):
    if len(arr) <= 5:
        QuickSortMedian.merge_sort(arr)
        return arr[k]

    pivot = arr[k]     # random element in the middle

    left = list()
    right = list()

    for num in arr:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    pivot_index = len(left)+1

    if pivot_index == k:
        return arr[pivot_index]
    elif pivot_index < k:
        find_median(right, k - pivot_index - 1)
    else:
        find_median(left, k)

arr = [3,2,1,4,5]
print("Median: ", find_median(arr, 2))
'''
def into_groups(arr, n):
    groups = list()
    count = 0
    for element in arr:
'''

'''PsedoCode

groups = into_groups(arr, 5)
    medians = list()
    for group in groups:
        medians.append(small_median(group))
    pivot = find_median(medians, len(medians)/2)

function MedianOfMedians(arr, k)
    if length(arr) <= 5
        Sort(arr)
        return arr[k]

    groups = DivideIntoGroups(arr, 5)
    medians = [FindMedian(group) for group in groups]
    pivot = MedianOfMedians(medians, len(medians) / 2)

    smaller = [element for element in arr if element < pivot]
    larger = [element for element in arr if element > pivot]
    equal = [element for element in arr if element == pivot]

    if k < len(smaller)
        return MedianOfMedians(smaller, k)
    else if k < len(smaller) + len(equal)
        return pivot
    else
        return MedianOfMedians(larger, k - len(smaller) - len(equal)

function FindMedian(arr)
    Sort(arr)
    return arr[len(arr) / 2]

function DivideIntoGroups(arr, groupSize)
    groups = []
    for i from 0 to len(arr) step groupSize
        groups.append(arr[i:i + groupSize])
    return groups
'''