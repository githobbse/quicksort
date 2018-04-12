####################################################################################
# Description: An implementation of QuickSort in which the pivot is selected randomly from #		the (sub-)array.
# File: README.txt
####################################################################################

PURPOSE
To purpose of quicksort_first.py and quicksort_random.py is to sort the contents of a file using quick sort. 


DESCRIPTION
The programs quicksort_first.py and quicksort_random.py are implementations of quick sort, but with a twist. These programs compute (i) the sorted set and (ii) the total number of comparisons used to sort the given input file by quick sort. 

The difference between the two programs are their pivoting rules. The first implementation of quick sort (quicksort_first.py) uses the first item in the (sub-)array as the pivot value, while the second implementation (quicksort_random.py) uses a random pivot value from the (sub-)array.


EXECUTION INSTRUCTIONS
To compile/run the quicksort_first.py and quicksort_random.py files, one must simple navigate to the directoy containing the programs, and run the following command:

"python quicksort_first.py inFile.in outFile.out"

or

"python quicksort_random.py inFile.in outFile.out"

Where inFile.in is the input file containing an unsorted set of newline-separated integers and outFile.out is where the sorted contents will be written.

Upon executing one of the above commands with a valid input file, the program will write the now sorted set of newline-separated integers to the output file. Additionally, the program will output the total number of comparisons used to sort the given input file by quick sort.