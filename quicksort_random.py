#######################################################################################################################################################################
# Description: An implementation of QuickSort in which the pivot is selected randomly from the (sub-)array.
# File: quicksort_random.py
#######################################################################################################################################################################

import sys
import random

def quickSort(alist):
    # Calls the recursive function quickSortHelper.
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        # Add (last - first) to the running total of comparisons.
        global numComps
        numComps += (last - first)

        # Determine a random pivot.
        pivot = random.randint(first, last)

        # Swap the random pivot value to the beginning of the list.
        temp = alist[first]
        alist[first] = alist[pivot]
        alist[pivot] = temp

        # Call the partition function to determine splitpoint and begin the sorting process.
        splitpoint = partition(alist, first, last)

        # QuickSort recursively on the two lists created by the splitpoint.
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    # Sets pivot value.
    pivotvalue = alist[first]
    
    # Sets positions of left and right markers.
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # Increment left marker until value is greater than the pivot value.
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        # Decrement right marker until value is less than the pivot value.
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        # Stop when right marker is less than left marker (meaning they've crossed each other).
        if rightmark < leftmark:
            done = True

        # Exchange value at right marker with value at left marker.
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    #  Exchange value at pivot with value at splitpoint (right marker).
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    
    return rightmark

alist = []

# Inputs files from command line. The first file is the inFile, the second is outFile.
inFile = open(sys.argv[1], 'r')
outFile = open(sys.argv[2], 'w')

# Builds alist from the inFile.
for element in inFile:
    alist.append(int(element.strip()))

# Run QuickSort and count the number of comparisons.
numComps = 0
quickSort(alist)

# Outputs results to stdout and the outFile.
sys.stdout.write(str(numComps) + ' comparisons made')
for element in alist:
    outFile.write(str(element) + '\n')
