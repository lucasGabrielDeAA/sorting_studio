def counting_sort(list):
	if not list:
		return []

	max_val = max(list)

	count = [0] * (max_val + 1)

	for number in list:
		count[number] += 1

	ordered_list = []

	for i, frequency in enumerate(count):
		ordered_list.extend([i] * frequency)

	return ordered_list