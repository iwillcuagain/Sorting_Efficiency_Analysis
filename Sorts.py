import random
import time
import sys
"""""
Author: Eliejah Walker
Class: CSC 2400
purpose: The purpose of this code is to measure and record the runtime of 
different sorting algorithms with different sizes and order of arrays.
Date: 10/27/2023
"""



# takes in the length of the array (N= 10,100,1000,...) and the type of array
def generate_array(length_of_array, array_type):
    # Check the specified 'array_type' and generate the corresponding array
    if array_type == 'random':
        # If 'random' is selected, create an array of random integers between 1 and 1000
        return [random.randint(1, 1000) for _ in range(length_of_array)]
    elif array_type == 'increasing':
        # If 'increasing' is selected, create an array with values from 1 to 'length_of_array'
        return [i for i in range(1, length_of_array + 1)]
        # If 'decreasing' is selected, create an array with values from 'length_of_array' down to 1
    elif array_type == 'decreasing':
        return [i for i in range(length_of_array, 0, -1)]

#takes in the array generated by the generate_array function stored in the array variable
def insertion_sort(array):
    # get length of the array
    n = len(array)
    # Iterate over the array starting from the second element (index 1)
    for i in range(1, n):
        # Store the current element in a temporary variable
        j = i
    # Continue to move the current element (array[j]) leftwards until it's in its correct position
    while j > 0 and array[j - 1] > array[j]:
        # Swap the current element with the element on its left if it's smaller
        temp = array[j]
        array[j] = array[j - 1]
        array[j - 1] = temp
        # Decrement j to check the next element to the left
        j = j - 1

#takes in the array generated by the generate_array function stored in the array variable
def bubble_sort(array):
    # get the length of the input array
    global swapped
    n = len(array)
    # Outer loop to iterate through each element in the array
    for i in range(n):
        # Inner loop to compare adjacent elements and swap them if they are in the wrong order
        for j in range(n - i - 1):
            # Compare the current element with the next element
            if array[j] > array[j + 1]:
                # If the current element is greater than the next element, swap them
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

#takes in the array generated by the generate_array function stored in the array variable
def selection_sort(array):
    n = len(array)
    for j in range(n - 1):
        # initialize the minimum index
        min_index = j;
    # find the index of the minimum element in the unsorted part of the array
    for i in range(j + 1, n):
        if array[i] < array[min_index]:
            min_index = i
    # Swap the minimum element with the first element in the unsorted part
    if min_index != j:
        temp = array[min_index]
        array[min_index] = array[j]
        array[j] = temp

#takes in the array generated by the generate_array function stored in the array variable
def shell_sort(array):
    n = len(array)
    # Initialize the gap as half the length of the array
    gap = n // 2

    # continue until gap becomes 0
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            # Compare and shift elements to their correct positions
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j = j - gap
            # Place the temporarily stored element into its correct position
            array[i] = temp
        # reduce the gap in half in each iteration
        gap = gap // 2
    return array #retuned sorted array 


# open a file called output.txt for appending the results of runtimes to the file
file = open('output.txt', 'a')
# whenever the print statement is called it will open the file and write to it
sys.stdout = file

# define the array sizes and types to test
N = [10, 100, 1000, 10000, 100000, 1000000]
array_types = ["random", "increasing", "decreasing"]

# Loop through the array sizes and types and measure the runtime of each sorting algorithm
for array_size in N:
    for array_type in array_types:

        # Generate an array with the specified size and type
        array = generate_array(array_size, array_type)

        # Record the start time to measure the sorting runtime
        start_time = time.perf_counter()

        # Call the insertion_sort function to sort the array
        insertion_sort(array)

        # record the end time
        end_time = time.perf_counter()

        # Calculate the runtime by finding the difference between start and end times
        runtime1 = end_time - start_time

        # Round the runtime to 6 decimal places for better readability
        rounded_runtime1 = round(runtime1, 6)

        # Print the sorting runtime for the current array size and type
        print("runtime for insertion sort of array size " + str(array_size) + " is " + str(
            rounded_runtime1) + " seconds for " + str(array_type))

        # Flush the output to the file to ensure it's saved
        file.flush()

for array_size in N:
    for array_type in array_types:
        # Generate an array with the specified size and type
        array = generate_array(array_size, array_type)

        # Record the start time to measure the sorting runtime
        start_time = time.perf_counter()

        # Call the bubble_sort function to sort the array
        bubble_sort(array)

        # record the end time
        end_time = time.perf_counter()

        # Calculate the runtime by finding the difference between start and end times
        runtime1 = end_time - start_time

        # Round the runtime to 6 decimal places for better readability
        rounded_runtime1 = round(runtime1, 6)

        # Print the sorting runtime for the current array size and type
        print("runtime for bubble sort of array size " + str(array_size) + " is " + str(
            rounded_runtime1) + " seconds for " + str(array_type))
        file.flush()

for array_size in N:
    for array_type in array_types:
        # Generate an array with the specified size and type
        array = generate_array(array_size, array_type)

        # Record the start time to measure the sorting runtime
        start_time = time.perf_counter()

        # Call the selection_sort function to sort the array
        selection_sort(array)  

        # record the end time
        end_time = time.perf_counter()

        # Calculate the runtime by finding the difference between start and end times
        runtime1 = end_time - start_time

        # Round the runtime to 6 decimal places for better readability
        rounded_runtime1 = round(runtime1, 6)

        # Print the sorting runtime for the current array size and type
        print("runtime for selection sort of array size " + str(array_size) + " is " + str(
            rounded_runtime1) + " seconds for " + str(array_type))
        file.flush()

for array_size in N:
    for array_type in array_types:
        # Generate an array with the specified size and type
        array = generate_array(array_size, array_type)

        # Record the start time to measure the sorting runtime
        start_time = time.perf_counter()

        # Call the shell_sort function to sort the array
        shell_sort(array)  # 100

        # record the end time
        end_time = time.perf_counter()

        # Calculate the runtime by finding the difference between start and end times
        runtime1 = end_time - start_time

        # Round the runtime to 6 decimal places for better readability
        rounded_runtime1 = round(runtime1, 6)

        # Print the sorting runtime for the current array size and type
        print("runtime for shell sort of array size " + str(array_size) + " is " + str(
            rounded_runtime1) + " seconds for " + str(array_type))
        file.flush()

# Close the output.txt file
file.close()
