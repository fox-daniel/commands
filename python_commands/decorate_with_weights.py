from functools import wraps

astring = "back out of all this now too much for us back in a time made distant by the loss of details burned dissolved and broken off"


def wrap_with_weights(fn):
	@wraps(fn)
	def wrapper(some_string):
		data = fn(some_string)
		for i in range(len(data)):
			data[i] = (data[i], len(data[i]))
		return data
	wrapper.__doc__ = f"{fn.__doc__} And add weights given by the length of the word"
	return wrapper

@wrap_with_weights
def create_text_data(some_string):
	"""Generate a list of words."""
	words = some_string.split(" ")
	return words

data = create_text_data(astring)
for datum in data:
	print(datum)

print(f"We have preserved the name and docstring: {create_text_data.__name__} and {create_text_data.__doc__}")

print("\n Now wrap a function with arbitrary args and kwards\n")
# Now for arbitrary args and kwargs

def wrap_with_weights(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		data = fn(*args, **kwargs)
		for i in range(len(data)):
			data[i] = (data[i], len(data[i]))
		return data
	wrapper.__doc__ = f"{fn.__doc__} And add weights given by the length of the word"
	return wrapper

@wrap_with_weights
def create_text_data(some_string, capitalize=False):
	"""Generate a list of words."""
	if capitalize == True:
		some_string = some_string.upper()
	print("The string:", some_string)
	words = some_string.split(" ")
	return words

data = create_text_data(astring, capitalize=True)
for datum in data:
	print(datum)

print(f"We have preserved the name and docstring: {create_text_data.__name__} and {create_text_data.__doc__}")

