"""
Two's Complement: ~x+1
"""

# to extract the rightmost 1 in the binary representation:
n = 10
print("n:", n)
print("n in bits:", bin(n))
print("the right most 1 is kept and the rest set to zero:", bin(n & -n))