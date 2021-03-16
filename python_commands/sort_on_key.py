from collections import defaultdict
from operator import itemgetter

astring = "asdfj;alskelkdskadfkajsdfoierfoaidflaksdfaksdflakwefoiefasdlkfj"
counts = defaultdict(int)
for i in range(len(astring)):
	counts[astring[i]] += 1

count_list = list(counts.items())

print(count_list)

# sort on a secondary key
count_list.sort(key = itemgetter(0))
# sort on a primary key: sort is stable so items will be sorted by 
# secondary key if their primaries keys are equal
count_list.sort(key = itemgetter(1), reverse = True)


print(count_list)

