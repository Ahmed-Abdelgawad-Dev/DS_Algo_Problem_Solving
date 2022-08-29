# Quick sort good approach
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr = [-1, 3, 6, 9, 1, 4, 7, 0, 99, 1, -5]
print(quick_sort(arr))
