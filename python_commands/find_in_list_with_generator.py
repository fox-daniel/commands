from time import time
import numpy as np
import tracemalloc

# Also try in the case that the list elements are tuples and one must find the element with a specified second element of the tupel


def timeit(f):
	def wrapper():
		start = time()
		f()
		ellapse = time() - start
		return ellapse, f()
	return wrapper

def memory_use(f):
	def wrapper():
		tracemalloc.start()
		f()
		current, peak = tracemalloc.get_traced_memory()
		print(f"For this approach, current memory usage is {current/ 10 ** 6}MB; peak was {peak / 10**6}MB")
		tracemalloc.stop()
	return wrapper

abiglist = np.random.randint(0,10,10 ** 7)
bbiglist = np.random.randint(0,10,1000)
biglist = list(np.hstack([abiglist, np.array([11]), bbiglist]))
# print(biglist)
# @timeit
@memory_use
def find_item_with_generator():
	"""
	Generator method
	"""
	x = next(i for i, x in enumerate(biglist) if x == 11)
	return x


# @timeit
@memory_use
def find_item_with_list_method():
	"""
	List method
	"""
	x = biglist.index(11)
	return x

# print("generator takes:", find_item_with_generator())


# tracemalloc.start()
# find_item_with_generator()
# current, peak = tracemalloc.get_traced_memory()
# print(f"For generator approach, current memory usage is {current/ 10 ** 6}MB; peak was {peak / 10**6}MB")
# tracemalloc.stop()

print("list method")
find_item_with_list_method()

print("generator")
find_item_with_generator()
# print("list method takes:", find_item_with_list_method())


