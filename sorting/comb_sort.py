def comb_sort(list):
	n = len(list)
	array = list.copy()
	gap = n
	shrink_factor = 1.3
	sorted_state = False

	while not sorted_state:
		gap = int(gap / shrink_factor)
		if gap <= 1:
			gap = 1
			sorted_state = True

		for i in range(n - gap):
			if array[i] > array[i + gap]:
				array[i], array[i + gap] = array[i + gap], array[i]
				sorted_state = False

	return array
