# Suppose you have a list of methods store as strings.
# Use getattr to call them.

alist = []
transforms = [('append', 5), ('append', 6), ('pop', 0)]
for transform in transforms:
	transform, value = transform
	method = getattr(alist, transform)
	method(value)
print(alist)