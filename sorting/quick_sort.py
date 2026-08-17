def quick_sort(list):
	if len(list) <= 1:
		return list

	half = len(list) // 2
	pivot = list[half]

	smallers = []
	equals = []
	biggers = []

	for number in list:
		if number < pivot:
			smallers.append(number)
		elif number == pivot:
			equals.append(number)
		else:
			biggers.append(number)

	return quick_sort(smallers) + equals + quick_sort(biggers)