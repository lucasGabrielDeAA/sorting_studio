import time

def calculate_execution_time(func, params, verbose=True):
	start_time = time.perf_counter()
	result = func(params)
	end_time = time.perf_counter()
	execution_time = end_time - start_time

	if verbose:
		print(f"Execution time: {execution_time:.6f} seconds")

	return result, execution_time