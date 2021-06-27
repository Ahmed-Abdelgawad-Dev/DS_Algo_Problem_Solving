# Select sort implementation
def select_sort(array):
	for i in range(len(array) -1):
		min_index = i
		for j in range(i + 1, len(array)):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] = array[min_index], array[i]
	return array


print(select_sort([50, 84, 43, 222, 11]))
