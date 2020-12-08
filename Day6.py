import time
from functools import reduce

start_time = time.time()

with open('input.txt') as f:
    data = f.read().split('\n\n')
    f.close()

adata = list(data)

for i in range(len(data)):
    data[i] = ''.join(data[i].splitlines())

groupCounts = []

for i in data:
    i = ''.join(set(i))
    groupCounts.append(len(i))

total = sum(groupCounts)

print("Part one solution: ", total)

'##################################'
'##################################'
'##################################'

groupCounts = []

for i in range(len(adata)):
    adata[i] = adata[i].splitlines()

for i in adata:
    groupCounts.append(len(list(reduce(set.intersection, [set(item) for item in i ]))))

total = sum(groupCounts)
print("Part two solutionL ", total)
