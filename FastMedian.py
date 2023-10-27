# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import QuickSortMedian
import statistics

''' Purpose: Using select() algorithm pick middle element by 
    splitting into groups and using the median from the groups
    Parameter1 -> Array
    Parameter2 -> target = index(middle for the median)
    Parameter3 -> k = size of the groups 
    Return     -> Median   '''
def find_median(arr, target, k):  # K = size of the groups (3,5, or 7)
    if len(arr) <= k:
        res = QuickSortMedian.merge_sort(arr)
        return res[len(arr) // 2]

    groups = list(gps(arr, k))
    medians = small_medians(groups)
    pivot = find_median(medians, len(medians) // 2, k)

    left = list()
    right = list()

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num >= pivot:
            right.append(num)

    pivot_index = len(left)

    if target < pivot_index:
        return find_median(left, target, k)
    elif target > pivot_index:
        return find_median(right, target - pivot_index - 1, k)
    else:
        return pivot


''' Purpose: Sort the small arr and pick middle element
    Parameter1 -> Array
    Return     -> Median   '''
def small_medians(groups):
    res = list()
    for group in groups:
        tmp = QuickSortMedian.merge_sort(group)
        mid = len(group) // 2
        res.append(tmp[mid])
    return res


''' Purpose: split into groups
    Parameter1 -> Array
    Parameter2 -> k - Size of the groups
    Return     -> array of groups   '''
def gps(arr, k):
    res = []
    idx = 0
    while idx + k < len(arr) - 1:
        res.append(arr[idx:idx + k])
        idx += k
    res.append(arr[idx:])
    return res


# Andrews implementation
# infinite recursion for large arrays
def fastMedian(Arr, k, n):
    groups = into_groups(Arr, n)
    medians = list()

    if len(Arr) <= n:
        median = QuickSortMedian.find_median(Arr)
        return median

    for group in groups:
        medians.append(QuickSortMedian.find_median(group))  # This line may need to be altered
    pivot = fastMedian(medians, len(medians) // 2, n)

    smaller = [element for element in Arr if element < pivot]
    larger = [element for element in Arr if element > pivot]
    equal = [pivot]

    if k < len(smaller):
        return fastMedian(smaller, k, n)
    elif k < (len(smaller) + len(equal)):
        return pivot
    return fastMedian(larger, (len(Arr) - len(smaller)), n)


def into_groups(arr, n):
    groups = list()
    length = len(arr)

    for i in range(n):
        start = i * n
        end = (i + 1) * n
        group = arr[start:end]

        if end > length + 1:
            if len(group) != 0:
                groups.append(group)
            return groups

        groups.append(group)

    return groups


"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(len(arr)//2)
print("Real : ", int(statistics.median(arr)))
print("Noa 3: ", find_median(arr, (len(arr) // 2), 3))
print("Noa 5: ", find_median(arr, (len(arr) // 2), 5))
print("Noa 7: ", find_median(arr, (len(arr) // 2), 7))
"""
