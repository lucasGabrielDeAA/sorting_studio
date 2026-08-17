MIN_RUN = 32

def insertion_sort_slice(array, left, right):
	for i in range(left + 1, right + 1):
		key = array[i]
		j = i - 1
		while j >= left and array[j] > key:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key

def merge_slices(array, left, mid, right):
	len1 = mid - left + 1
	len2 = right - mid

	left_part = array[left:mid + 1]
	right_part = array[mid + 1:right + 1]

	i, j, k = 0, 0, left

	while i < len1 and j < len2:
		if left_part[i] <= right_part[j]:
			array[k] = left_part[i]
			i += 1
		else:
			array[k] = right_part[j]
			j += 1
		k += 1

	while i < len1:
		array[k] = left_part[i]
		i += 1
		k += 1

	while j < len2:
		array[k] = right_part[j]
		j += 1
		k += 1

def tim_sort(list):
	n = len(list)
	array = list.copy()

	if n <= 1:
		return array

	for i in range(0, n, MIN_RUN):
		insertion_sort_slice(array, i, min(i + MIN_RUN - 1, n - 1))

	size = MIN_RUN
	while size < n:
		for left in range(0, n, 2 * size):
			mid = min(n - 1, left + size - 1)
			right = min(left + 2 * size - 1, n - 1)

			if mid < right:
				merge_slices(array, left, mid, right)

		size *= 2

	return array
