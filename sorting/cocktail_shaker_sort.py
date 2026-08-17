def cocktail_shaker_sort(list):
	n = len(list)
	array = list.copy()
	start = 0
	end = n - 1
	swapped = True

	while swapped:
		swapped = False

		for i in range(start, end):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True

		if not swapped:
			break

		swapped = False
		end -= 1

		for i in range(end - 1, start - 1, -1):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				swapped = True

		start += 1

	return array
