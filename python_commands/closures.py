"""Closures in Python are defined using an outer function to define the 
namespace from which an inner function (the closure) can store data.

- Closures are defined as a nested function that is returned by an outer function
- Closures can save data from the enclosing namespace even if that data goes out 
	of scope

An example follows:
"""

# Example:
def times_n(n):
	def multiply_x(x):
		return n * x
	return multiply_x

times3 = times_n(3)
times5 = times_n(5)

del times_n

try:
	times_n(4)
except NameError:
	print("times_n is deleted.")

# But times3 and times5 are valid, having stored the 3 and 5.
assert times3(4) == 12
assert times5(2) == 10

try:
	assert times3(4) == 13
except AssertionError:
	print("3*4 is not 13")

# We can access the data still:
assert times3.__closure__[0].cell_contents == 3
assert times5.__closure__[0].cell_contents == 5
