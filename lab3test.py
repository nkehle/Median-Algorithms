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
import RandomMedian

RandomMedian.into_groups([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)

"""
    compareTime: computes the average times for running the three 5 Medians algithms
    Parameters:
        parameter1 (sizes = []): array of given sizes of matrices 
"""
def compareTime(sizes):
    repeats = 5
    avgQuickSort = []
    avgRandom = []
    avgMedians3 = []
    avgMedians5 = []
    avgMedians7 = []


# EXAMPLE FROM LAST LAB
# naiveTime = timeit.timeit(lambda: NaiveMxMultiplication.MXMultiply(A, B), setup="pass", number=1)
# nCnt += naiveTime

    for size in sizes:
        for j in range(repeats):
            A = np.random.randint(low=0, high=100, size=(size, size))
            B = np.random.randint(low=0, high=100, size=(size, size))

            # run the quick sort and time

            # run the random and time

            # run the medians with 3 and time

            # run the medians with 5 and time

            # run the medians with 7 and time

        # add the averages to their respected lists

    return avgQuickSort, avgRandom, avgMedians3, avgMedians5, avgMedians7

''' ** PLOTTING THE GRAPHS WITH AVERAGE TIMES ** '''

sizes = []
res = compareTime(sizes)

print("Naive:    ", res[0], "\nDNC:      ", res[1], "\nStrassen: ", res[2], '\n')

# plot quick sort
plt.plot(sizes, res[0], label='QuickSort', color='red', linestyle='-')

# plot random
plt.plot(sizes, res[1], label='Random', color='blue', linestyle='--')


# labels
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid = True
plt.legend()

# show plotting
plt.show()