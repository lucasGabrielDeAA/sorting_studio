from sorting.insertion_sort import insertion_sort

def bucket_sort(list):
	if len(list) <= 1:
		return list.copy()

	array = list.copy()
	min_val = min(array)
	max_val = max(array)

	if min_val == max_val:
		return array

	bucket_count = len(array)
	buckets = [[] for _ in range(bucket_count)]

	for number in array:
		normalized = (number - min_val) / (max_val - min_val)
		bucket_index = int(normalized * (bucket_count - 1))
		buckets[bucket_index].append(number)

	ordered_list = []
	for bucket in buckets:
		if bucket:
			ordered_list.extend(insertion_sort(bucket))

	return ordered_list
