# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import timeit
matplotlib.use('TkAgg')
import RandomMedian
import QuickSortMedian
import FastMedian
import RandomMedian

"""
    compareTime: computes the average times for running the three 5 Medians algithms
    Parameters:
        parameter1 (sizes = []): array of given sizes of matrices 
"""
def compareTime(sizes):
    repeats = 5
    avg_quick_sort = []
    avg_random = []
    avg_fast3 = []
    avg_fast5 = []
    avg_fast7 = []

# EXAMPLE FROM LAST LAB
# naiveTime = timeit.timeit(lambda: NaiveMxMultiplication.MXMultiply(A, B), setup="pass", number=1)
# nCnt += naiveTime

    for size in sizes:
        quick_sort_count = random_count = fast3_count = fast5_count = fast7_count = 0
        for j in range(repeats):
            arr = np.random.randint(1, size + 1, size=size)
            mid = len(arr) // 2

            # run the quick sort and time
            quick_sort_time = timeit.timeit(lambda: QuickSortMedian.find_median(arr), setup="pass", number=1)
            quick_sort_count += quick_sort_time

            # run the random and time
            random_time = timeit.timeit(lambda: RandomMedian.find_median(arr, mid), setup="pass", number=1)
            random_count += random_time

            # run the medians with 3 and time
            fast3_time = timeit.timeit(lambda: FastMedian.find_median(arr, mid, 3), setup="pass", number=1)
            fast3_count += fast3_time

            # run the medians with 5 and time
            fast5_time = timeit.timeit(lambda: FastMedian.find_median(arr, mid, 5), setup="pass", number=1)
            fast5_count += fast5_time

            # run the medians with 7 and time
            fast7_time = timeit.timeit(lambda: FastMedian.find_median(arr, mid, 7), setup="pass", number=1)
            fast7_count += fast7_time

        # add the averages to their respected lists
        avg_quick_sort.append(round((quick_sort_count / repeats), 5))          # round to 5 decimals
        avg_random.append(round((random_count / repeats), 5))          # round to 5 decimals
        avg_fast3.append(round((fast3_count / repeats), 5))          # round to 5 decimals
        avg_fast5.append(round((fast5_count / repeats), 5))          # round to 5 decimals
        avg_fast7.append(round((fast7_count / repeats), 5))          # round to 5 decimals

    return avg_quick_sort, avg_random, avg_fast3, avg_fast5, avg_fast7

''' ** PLOTTING THE GRAPHS WITH AVERAGE TIMES ** '''
sizes = [5, 10, 20, 50, 100, 500, 1000, 100000, 100000, 1000000]
res = compareTime(sizes)
print("Quicksort: ", res[0], "\nRandom:    ", res[1], "\nFast K=3:  ", res[2], "\nFast K=5:  ", res[3], "\nFast K=7:  ", res[4])


"""
# plot quick sort
plt.plot(sizes, res[0], label='QuickSort', color='red', linestyle='-')
# plot random
plt.plot(sizes, res[1], label='Random', color='blue', linestyle='-')
# plot fast k = 3
plt.plot(sizes, res[1], label='K=3', color='greem', linestyle='-')
# plot fast k = 5
plt.plot(sizes, res[1], label='K=5', color='purple', linestyle='-')
# plot fast k = 7
plt.plot(sizes, res[1], label='K=7', color='yellow', linestyle='-')


# labels
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid = True
plt.legend()

# show plotting
#plt.show()"""