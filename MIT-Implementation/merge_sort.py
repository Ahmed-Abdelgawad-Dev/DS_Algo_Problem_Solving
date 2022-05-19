"""
Time Complexity: O(n log N)
Usage: ( Inversion count problem, External sorting, E-commerce applications)
"""


def merge_sort(array):
    if len(array) > 1:
        # Divide array into two parts
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        # Sorting left & right
        merge_sort(left)
        merge_sort(right)
        # Counters for left, right & origin array
        # i4left, j4right, k4array
        i = j = k = 0
        # Loop over two lists(left & right)
        while i < len(left) and j < len(right):
            # If first element in left list < first element in right list
            if left[i] < right[j]:
                # Put the left list element in the main list.
                array[k] = left[i]
                # Increase counter i by 1
                i += 1
            else:
                # Put the right list element in the main list.
                array[k] = right[j]
                # Increase counter j by 1
                j += 1
            # Increase counter k of main list by 1
            k += 1
        # Loop once again in case of remaining elements separately:
        # Over left list
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        # Over right list
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


array = [7, 4, 5, 6, 91, 0, 99, 4, 77, 43]
merge_sort(array)
print(array)
