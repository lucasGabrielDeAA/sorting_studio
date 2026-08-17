def merge_sort(list):
	if len(list) <= 1:
		return list

	half = len(list) // 2
	left_part = list[:half]
	right_part = list[half:]

	ordered_left = merge_sort(left_part)
	ordered_right = merge_sort(right_part)

	return merge(ordered_left, ordered_right)

def merge(left, right):
	result = []
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[j:])

	return result