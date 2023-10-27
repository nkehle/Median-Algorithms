# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import numpy as np

import QuickSortMedian

''' Purpose: Sort the arr and pick middle element
    Parameter1 -> Array
    Return     -> Median   '''
def find_median(arr, target):
    if len(arr) <= 5:
        QuickSortMedian.merge_sort(arr)
        return arr[len(arr) // 2]

    pivot = arr[target]  # random element in the middle

    left = list()
    right = list()

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num >= pivot:
            right.append(num)

    pivot_index = len(left)

    if target < pivot_index:
        return find_median(left, target)
    elif target > pivot_index:
        return find_median(right, target - pivot_index - 1)
    else:
        return pivot

