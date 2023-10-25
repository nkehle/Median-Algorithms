# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import numpy as np

''' Purpose: Sort the arr and pick middle element
    Parameter1 -> Array
    Return     -> Median   '''
def find_median(arr):
    merge_sort(arr)
    return arr[len(arr) // 2]       # middle (median)

''' Purpose: Sort the arr 
    Parameter1 -> Array
    Return     -> none   '''
def merge_sort(arr):
    # base case -> when there is one element
    if len(arr) <= 1:
        return arr[0]

    # find the middle index to split array into two
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # call the sort on the two halves
    merge_sort(left)
    merge_sort(right)

    # merge the two
    merge(arr, left, right)


''' Purpose: to combine the two arrays
    Parameter1 -> Array
    Return     -> Median   '''
def merge(arr, left, right):
    # for indexing the left right and res
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # clear the rest of both
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while k < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

"""
arr = [5,4,3,2,1,]

print("Array:", arr, "\nMedian --> ", find_median(arr))
"""