from itertools import product

a = [0,2,4,6]
b = [1,3,5]
c = [7,8]

abc = product(*[a,b,c])

def f(x):
	return x*x

for item in abc:
	# print(item)
	asum = sum(map(f, item))
	print(asum)

print(sum(map(lambda x:x*x, (0,1,2,3))))
