from itertools import groupby

astring = 'aaabbfferrrc'

groups = groupby(astring)

for k,v in groups:
	print(k,len(list(v)))

# print(len(astring))