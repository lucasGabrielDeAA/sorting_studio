import argparse

from helpers import calculate_execution_time
from sorting.bubble_sort import bubble_sort
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insertion_sort
from sorting.cocktail_shaker_sort import cocktail_shaker_sort
from sorting.gnome_sort import gnome_sort
from sorting.comb_sort import comb_sort
from sorting.shell_sort import shell_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.heap_sort import heap_sort
from sorting.tim_sort import tim_sort
from sorting.counting_sort import counting_sort
from sorting.radix_sort import radix_sort
from sorting.bucket_sort import bucket_sort
from gui import launch_gui


def run_cli(vector):
	print("Initial vector: ", vector)

	print("\n--- Sorting algorithms O(n^2) ---")
	print("Bubble sort: ")
	calculate_execution_time(bubble_sort, vector)
	print("Selection sort: ")
	calculate_execution_time(selection_sort, vector)
	print("Insertion sort: ")
	calculate_execution_time(insertion_sort, vector)
	print("Cocktail Shaker sort: ")
	calculate_execution_time(cocktail_shaker_sort, vector)
	print("Gnome sort: ")
	calculate_execution_time(gnome_sort, vector)

	print("\n--- Sorting algorithms O(n log n) / Sub-Quadratic ---")
	print("Merge sort: ")
	calculate_execution_time(merge_sort, vector)
	print("Quick sort: ")
	calculate_execution_time(quick_sort, vector)
	print("Heap sort: ")
	calculate_execution_time(heap_sort, vector)
	print("Tim sort: ")
	calculate_execution_time(tim_sort, vector)
	print("Shell sort: ")
	calculate_execution_time(shell_sort, vector)
	print("Comb sort: ")
	calculate_execution_time(comb_sort, vector)

	print("\n--- Sorting algorithms O(n + k) (Linear / Distribution) ---")
	print("Counting sort: ")
	calculate_execution_time(counting_sort, vector)
	print("Radix sort: ")
	calculate_execution_time(radix_sort, vector)
	print("Bucket sort: ")
	calculate_execution_time(bucket_sort, vector)


def main():
	parser = argparse.ArgumentParser(description="Sorting Algorithms Visualizer & Suite")
	parser.add_argument(
		'--list',
		nargs="*",
		type=int,
		help='A list of numbers (e.g. --list 120 30 45 99 12 5)',
		default=[120, 30, 45, 99, 12, 5],
	)
	parser.add_argument(
		'--cli',
		action='store_true',
		help='Run in terminal CLI mode instead of launching the GUI',
	)
	args = parser.parse_args()

	if args.cli:
		run_cli(args.list)
	else:
		launch_gui(initial_list=args.list)


if __name__ == "__main__":
	main()
