# Noa Kehle and Andrew Okerlund
# nkehle@calpoly.edu apokerlu@calpoly.edu
# CSC3-349-01 -- Fall 2023
# Lab 3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import timeit
import QuickSortMedian
import FastMedian
import RandomMedian
matplotlib.use('TkAgg')

"""
    compareTime: computes the average times for running the three 5 Medians algithms
    Parameters:
        parameter1 (sizes = []): array of given sizes of matrices 
"""
def compareTime(sizes):
    repeats = 100

    # store the averages
    avg_quick_sort = []
    avg_random = []
    avg_fast3 = []
    avg_fast5 = []
    avg_fast7 = []

    # store the standard deviations
    stdev_quick_sort = []
    stdev_random = []
    stdev_fast3 = []
    stdev_fast5 = []
    stdev_fast7 = []

    for size in sizes:
        # to store the total time for the average
        quick_sort_count = random_count = fast3_count = fast5_count = fast7_count = 0

        # to store runtimes for each iteration
        quick_sort_runtimes = []
        random_runtimes = []
        fast3_runtimes = []
        fast5_runtimes = []
        fast7_runtimes = []

        for j in range(repeats):
            arr = np.random.randint(1, size + 1, size=size)
            mid = len(arr) // 2

            # run the quick sort and time
            quick_sort_time = timeit.timeit(lambda: QuickSortMedian.find_median(arr), setup="pass", number=1)
            quick_sort_count += quick_sort_time
            quick_sort_runtimes.append(quick_sort_time)

            # run the random and time
            random_time = timeit.timeit(lambda: RandomMedian.find_median(arr, mid), setup="pass", number=1)
            random_count += random_time
            random_runtimes.append(random_time)

            # run the medians with 3 and time
            fast3_time = timeit.timeit(lambda: FastMedian.find_median(arr, mid, 3), setup="pass", number=1)
            fast3_count += fast3_time
            fast3_runtimes.append(fast3_time)

            # run the medians with 5 and time
            fast5_time = timeit.timeit(lambda: FastMedian.find_median(arr, mid, 5), setup="pass", number=1)
            fast5_count += fast5_time
            fast5_runtimes.append(fast5_time)

            # run the medians with 7 and time
            fast7_time = timeit.timeit(lambda: FastMedian.find_median(arr, mid, 7), setup="pass", number=1)
            fast7_count += fast7_time
            fast7_runtimes.append(fast7_time)

        # add the averages to their respected lists
        avg_quick_sort.append(round((quick_sort_count / repeats), 5))  # round to 5 decimals
        avg_random.append(round((random_count / repeats), 5))  # round to 5 decimals
        avg_fast3.append(round((fast3_count / repeats), 5))  # round to 5 decimals
        avg_fast5.append(round((fast5_count / repeats), 5))  # round to 5 decimals
        avg_fast7.append(round((fast7_count / repeats), 5))  # round to 5 decimals

        # add the standard deviations to the list
        stdev_quick_sort.append(round(np.std(quick_sort_runtimes), 5))
        stdev_random.append(round(np.std(random_runtimes), 5))
        stdev_fast3.append(round(np.std(fast3_runtimes), 5))
        stdev_fast5.append(round(np.std(fast5_runtimes), 5))
        stdev_fast7.append(round(np.std(fast7_runtimes), 5))

    return avg_quick_sort, avg_random, avg_fast3, avg_fast5, avg_fast7, stdev_quick_sort, stdev_random, stdev_fast3, stdev_fast5, stdev_fast7


''' ** PLOTTING THE GRAPHS WITH AVERAGE TIMES ** '''
sizes = [5, 10, 20, 50, 100, 200, 400, 500, 1000, 10000, 100000]
res = compareTime(sizes)
print("Quicksort AVG: ", res[0], "\nRandom AVG:    ", res[1], "\nFast K=3 AVG:  ", res[2], "\nFast K=5 AVG:  ", res[3],
      "\nFast K=7 AVG:  ", res[4])
print("-" * 90, "\n")
print("Quicksort STDEV: ", res[5], "\nRandom STDEV:    ", res[6], "\nFast K=3 STDEV:  ", res[7], "\nFast K=5 STDEV:  ",
      res[8], "\nFast K=7 STDEV:  ", res[9])

# plot quick sort
plt.plot(sizes, res[0], label='QuickSort', color='red', linestyle='-')
# plot random
plt.plot(sizes, res[1], label='Random', color='blue', linestyle='-')
# plot fast k = 3
plt.plot(sizes, res[2], label='K=3', color='green', linestyle='-')
# plot fast k = 5
plt.plot(sizes, res[3], label='K=5', color='purple', linestyle='-')
# plot fast k = 7
plt.plot(sizes, res[4], label='K=7', color='yellow', linestyle='-')

# labels
plt.xlabel('Size of the Array')
plt.ylabel('Average Time for in (Seconds)')
plt.title('Average Runtime of Median Algorithms ')
plt.grid = True
plt.legend()

# show plotting
plt.show()
