def selection_sort(list):
	n = len(list)
	array = list.copy()

	for i in range(n):
		smaller_index = i

		for j in range(i + 1, n):
			if array[j] < array[smaller_index]:
				smaller_index = j

		if smaller_index != i:
			array[i], array[smaller_index] = array[smaller_index], array[i]
	
	return array