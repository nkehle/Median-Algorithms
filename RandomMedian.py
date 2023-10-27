import QuickSortMedian

''' Purpose: Sort the arr and pick middle element
    Parameter1 -> Array
    Return     -> Median   '''

def find_median(arr, k):
    if len(arr) <= 5:
        QuickSortMedian.merge_sort(arr)
        return arr[len(arr) // 2]

    pivot = arr[k]     # random element in the middle

    left = list()
    right = list()

    for num in arr:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)

    print("Left: ", left)
    print("Right: ", right)
    pivot_index = len(left)

    if pivot_index < k:
        return find_median(right, k)
    elif pivot_index > k:
        return find_median(left, k)
    else:
        return arr[pivot]
