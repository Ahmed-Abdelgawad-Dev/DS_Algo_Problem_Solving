def bubble_sort(arr):
    sorted_element = False
    while not sorted_element:
        sorted_element = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_element = False
    return arr


print(bubble_sort([5, 4, 3, 2, 1]))
