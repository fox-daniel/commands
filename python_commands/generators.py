"""
Each time the .next() method of a generator-iterator is invoked, 
the code in the body of the generator-function is executed until 
a yield or return statement (see below) is encountered, or until 
the end of the body is reached.
"""

def counting(n):
	while 1:
		yield n
		n = n + 1

count = counting(-1)

for _ in range(12):
	print(next(count))

for _ in range(12):
	print(count.__next__())

# def not_counting(n):
# 	yield n
# 	print(n)
# 	n = n + 1
# 	print(n)
# 	not_counting(n)

# not_count = not_counting(-1)

# for _ in range(12):
# 	print(next(not_count))

print("Count Down Through a Recursive Generator")
def counting_2(n):
	if n > 0:
		yield n
		for j in counting_2(n-1):
			yield j
	

count = counting_2(10)

for x in count:
	print(x)

print("Counter with function instead of a generator")

count = []
def counter_fn(n):
	if n > 0:
		count.append(n)
		counter_fn(n-1)

counter_fn(10)
for c in count:
	print(c)

