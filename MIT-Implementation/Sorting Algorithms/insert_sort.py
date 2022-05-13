"""
Time Complexity: O(n2)
Usage:
    * a small list is to be sorted
    * cost of swapping does not matter
    * checking of all the elements is compulsory
    * cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
"""
# The process is like sorting cards
#   Index   Element
# [   9   ,    5   ,    1   ,    4   ,    3   ]


def insertion_sort(array):
    for step in range(1, len(array)):  # loop over[1:]
        element = array[step]
        index = step - 1
        while index >= 0 and element < array[index]:
            # [9, 9, 1, 4, 3]
            array[index + 1] = array[index]
            # [INDEX,9, 9, 1, 4, 3]
            index -= 1
        # [INDEX,ELEMENT=5, 9, 1, 4, 3]
        array[index + 1] = element


arr = [9, 5, 1, 4, 3]
insertion_sort(arr)
print(arr)
