# def fib(n):
# 	fibo = {0:0,1:1}
# 	try:
# 		return fibo[n]
# 	except KeyError:
# 		fibo[n] = fib(n-1)+fib(n-2)
# 	return fibo[n]

def fiblist(n):

	def fib(n):
		fibo = {0:0,1:1}
		try:
			return fibo[n]
		except KeyError:
			fibo[n] = fib(n-1)+fib(n-2)
		return fibo[n]

	return [fib(i) for i in range(n)]


	

print(fiblist(9))