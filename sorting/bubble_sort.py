def bubble_sort(list):
	n = len(list)
	array = list.copy()

	for i in range(n):
		exchanged = False

		for j in range(0, n - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
				exchanged = True

		if not exchanged:
			break

	return array