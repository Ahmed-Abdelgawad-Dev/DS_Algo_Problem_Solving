# Select sort implementation
def insert_sort(arr):
	# loop over the array and leave the first index
	for i in range(1, len(arr)):
		# key node to use in comparison with the node b4
		key_node = arr[i]
		# storing the [0] index as a j
		j_index = i - 1
		# while index 0 > =  0 && while key node value < the node[j]
		while j_index >= 0 and key_node < arr[j_index]:
			# move the j index node to the next one
			arr[j_index + 1] = arr[j_index]
			# Reassign the j value to be in the start as it was
			j_index -= 1
		# move the key node to be after the j node by one position forward
		arr[j_index + 1] = key_node

	return arr


print(select_sort([5, 5, 4, 3, 2, 1]))
