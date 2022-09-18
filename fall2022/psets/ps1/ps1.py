from asyncio import base_tasks
from math import log, ceil
from time import time
from random import randint

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

# TODO: implement RadixSort
def radixSort(u, b, a):
    k = ceil(log(u, b))
    n = len(a)
    v = []
    new_a = []
    adict = {}
    for i in range(n):
        kprime = a[i][0]
        vprime = BC(kprime, b, k)
        adict[kprime] = a[i][1]
        v.append(vprime)
    for j in range(k):
        tosort = []
        for i in range(n):
            tosort.append((v[i][j], v[i]))
        result = countSort(b, tosort)
    for i in range(n):
        sum = 0
        for j in range(k):
            sum += (result[i][1][j] * (b ** j))
        new_a.append((sum, adict[sum]))
    return new_a

# TODO: Create Test Experiments

for i in range(2, 3):
    for j in range(1, 21):
        #print("n = " + str(i))
        #print("u = " + str(j))

        n = 2 ** i
        u = 2 ** j
        a = []
        b = n
        for _ in range(n):
            a.append((randint(0, u-1), randint(0, u-1)))

        countstart = time()
        countSort(u, a)
        countend = time()

        radixstart = time()
        radixSort(u, b, a)
        radixend = time()

        mergestart = time()
        mergeSort(a)
        mergeend = time()

        counttime = countend - countstart
        radixtime = radixend - radixstart
        mergetime = mergeend - mergestart

        if counttime > radixtime and counttime > mergetime:
            print("count")
        elif radixtime > counttime and radixtime > mergetime:
            print("radix")
        elif mergetime > radixtime and mergetime > counttime:
            print("merge")


