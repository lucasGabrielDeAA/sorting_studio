def gnome_sort(list):
	n = len(list)
	array = list.copy()
	index = 0

	while index < n:
		if index == 0 or array[index] >= array[index - 1]:
			index += 1
		else:
			array[index], array[index - 1] = array[index - 1], array[index]
			index -= 1

	return array
