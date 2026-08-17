def heapify(list, heap_size, upper_index):
	bigger = upper_index
	left_child = 2 * upper_index + 1
	right_child = 2 * upper_index + 2

	if left_child < heap_size and list[left_child] > list[bigger]:
		bigger = left_child

	if right_child < heap_size and list[right_child] > list[bigger]:
		bigger = right_child

	if bigger != upper_index:
		list[upper_index], list[bigger] = list[bigger], list[upper_index]

		heapify(list, heap_size, bigger)

def heap_sort(list):
	n = len(list)
	array = list.copy()

	for i in range(n // 2 - 1, -1, -1):
		heapify(array, n, i)

	for i in range(n - 1, 0, -1):
		array[i], array[0] = array[0], array[i]

		heapify(array, i, 0)

	return array