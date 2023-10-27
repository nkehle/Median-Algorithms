import QuickSortMedian
import statistics

"""
arr --> array of ints
target --> the target index
k --> the split into groups of k size 
"""
def find_median(arr, target, k):
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


def small_medians(groups):
    res = list()
    for group in groups:
        tmp = QuickSortMedian.merge_sort(group)
        mid = len(group) // 2
        res.append(tmp[mid])
    return res


def gps(arr, k):
    res = []
    idx = 0
    while idx + k < len(arr) - 1:
        res.append(arr[idx:idx + k])
        idx += k
    res.append(arr[idx:])
    return res

"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(len(arr)//2)
print("Real : ", int(statistics.median(arr)))
print("Noa 3: ", find_median(arr, (len(arr) // 2), 3))
print("Noa 5: ", find_median(arr, (len(arr) // 2), 5))
print("Noa 7: ", find_median(arr, (len(arr) // 2), 7))
"""
# Andrews implementation

"""n is the size of the subarrays 3, 5, 7
k is the desired value
l is the length"""


def fastMedian(Arr, k, n):
    groups = into_groups(Arr, n)
    medians = list()

    if len(Arr) <= n:
        median = QuickSortMedian.find_median(Arr)
        return median

    for group in groups:
        medians.append(QuickSortMedian.find_median(group))  # This line may need to be altered
    pivot = fastMedian(medians, len(medians) // 2, n)

    smaller = [element for element in arr if element < pivot]
    larger = [element for element in arr if element > pivot]
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


