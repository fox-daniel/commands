# A "time this" decorator for fns without arguments

from time import time
from collections import Counter
def timethis(f):
	def wrapper():
		start = time()
		f()
		duration = time() - start
		print(duration)
	return wrapper

@timethis
def count_neither():
	for i in range(10 ** 5):
		counts = Counter("To and fro in shadow from inner to outer shadow from inpenetrable self to inpenetrable unself by way of neither")
	print(counts)


count_neither()

