"""
Usage: Security & Embedded system like linux kernel
Time complexity: O(n log n)

Heaps Formula to detect index:
    i => chosen element => 2
    i*2 => next element => 4
    (i*2)+1 => next after next => 5
    i//2 => parent element => 2
       4
       /\
      7   9
     /\   /\
    1  3 6  5
"""


def heapify(array, arr_length, index):
    # Set largest index to index in a max-heap
    largest = index
    left_index = (2 * index) + 1
    right_index = (2 * index) + 2
    # If there is left_index & left element > index=largest
    if left_index < arr_length and array[left_index] > array[largest]:
        # Set largest to left_index
        largest = left_index
        # If there is right_index & right element > index=largest
    if right_index < arr_length and array[right_index] > array[largest]:
        # Set largest to right_index
        largest = right_index
    # If largest value changed and does not equal index as b4
    if largest != index:
        # Swap largest value(child) with original index value(parent)
        array[index], array[largest] = array[largest], array[index]
        # Reheapify after swapping or shifting both values
        heapify(array, arr_length, largest)


# Insert a node
def insert(array, node):
    length = len(array)
    if length == 0:
        array.append(node)
    else:
        array.append(node)
        # Loop over every index
        for i in range(length):
            # Reheapify
            heapify(array, length, i)

# Delete a node


def delete(array, node):
    length = len(array)
    for index in range(0, length):
        # Found the node we want to remove
        if node == array[index]:
            # Swap the node to delete with the last node
            array[index], array[-1] = array[-1], array[index]
    # Remove the node
    array.remove(array[-1])
    # Loop over every node index
    for i in range(len(array)):
        # Reheapify
        heapify(array, len(array), i)


def heap_sort(A):
    length = len(A)  # =7
    """
       4
       /\
      7   9
     /\   /\
    1  3 6  5
    """
    """
    start from -1{5}, up to parents(n//2-1)
    Means => Looping over 9,7,4 & decrease by 1
    """
    for i in range(length//2-1, -1, -1):
        # Heapify
        heapify(A, length, i)
    """
    Result: Max-Heap Array:
       9
       /\
      6   7
     /\   /\
    5  3 1  4
    """
    """ 
    start from -1{4}, up to index one after zero{6} excluding index 0
    Looping over 4,1,3,5,7,6 in reversing order
    excluding parent{9}==index 0
    """
    for i in range(length-1, 0, -1):
        """
         4
         /\
        6     7
        /\    /\
        5  3  1  9
        Swap parent with the last node and reheapify ...etc
        """
        arr[0], arr[i] = arr[i], arr[0]
        heapify(A, i, 0)


heap = []

insert(heap, 4)
insert(heap, 7)
insert(heap, 9)
insert(heap, 1)
insert(heap, 3)
insert(heap, 6)
insert(heap, 5)

print("Max-Heap Array:          ", heap)
delete(heap, 4)
print('Heap after deleted item: ', heap)
print()

arr = [4, 7, 9, 1, 3, 6, 5]
heap_sort(arr)
print("Sorted array: ")
for i in range(len(arr)):
    print(arr[i], end='    ')
