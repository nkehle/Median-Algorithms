import QuickSortMedian

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
        else:
            right.append(num)

    pivot_index = len(left)+1

    if pivot_index == target:
        return arr[pivot_index]
    elif pivot_index < target:
        return find_median(right, target - pivot_index - 1, k)
    else:
        return find_median(left, target, k)

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


#Andrews implementation

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
        medians.append(QuickSortMedian.find_median(group)) #This line may need to be altered
    pivot = fastMedian(medians, len(medians) // 2, n)

    smaller = [element for element in arr if element < pivot]
    larger = [element for element in arr if element > pivot]
    equal = [pivot]

    if k < len(smaller):
        return fastMedian(smaller, k, n)
    elif k < (len(smaller) + len(equal)):
        return pivot
    return fastMedian(larger, (len(Arr) - len(smaller), n))

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

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Noa: ", find_median(arr, len(arr) // 2, 5))
print("Andrew: ", fastMedian(arr, len(arr) // 2, 5))