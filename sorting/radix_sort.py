def counting_sort_for_radix(list, decimal_radix):
	n = len(list)
	result = [0] * n
	count = [0] * 10

	for i in range(n):
		digit = (list[i] // decimal_radix) % 10
		count[digit] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	
	while i >= 0:
		digit = (list[i] // decimal_radix) % 10
		pos = count[digit] - 1
		result[pos] = list[i]
		count[digit] -= 1
		i -= 1

	for i in range(n):
		list[i] = result[i]

def radix_sort(list):
	if not list:
		return []

	array = list.copy()

	max_number = max(array)

	decimal_radix = 1

	while max_number // decimal_radix > 0:
		counting_sort_for_radix(array, decimal_radix)
		decimal_radix *= 10

	return array