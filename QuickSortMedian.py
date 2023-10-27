# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import numpy as np

''' Purpose: Sort the arr and pick middle element
    Parameter1 -> Array
    Return     -> Median   '''
def find_median(arr):
    sorted = merge_sort(arr)
    return sorted[len(arr) // 2]       # middle (median)

''' Purpose: Sort the arr 
    Parameter1 -> Array
    Return     -> none   '''
def merge_sort(arr):
    # base case -> when there is one element
    if len(arr) <= 1:
        return arr

    # find the middle index to split array into two
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # call the sort on the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the two
    return merge(left, right)


''' Purpose: to combine the two arrays
    Parameter1 -> Array
    Return     -> Median   '''
def merge(left, right):
    res = []

    # for indexing the left right and res
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res
