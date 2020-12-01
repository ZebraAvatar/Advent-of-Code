# Advent of Code Day 1

import time
from functools import reduce

start_time = time.time()

expenses = open('C:\\Users\\peter\\Downloads\\Advent of Code\\Day 1\\input.txt', 'r')
data = expenses.readlines()

for i in range(len(data)):
  data[i] = int(data[i].strip())
  
##########
#Part One#
##########

SUM = 0
eye = 0
jay = 0

for i in data:
  if 2020 - i in data:
    eye = i
    jay = 2020 - i

print(f"\n{{{eye}, {jay}}}")
print(f"i * j = {eye*jay}\n")

##########
#Part Two#
##########

three = []

for i in data:
  for j in data:
    if 2020 - i - j in data:
      three.append(i)

print(set(three))
print("x * y * z = ", reduce(lambda x,y: x*y, [x for x in set(three)]))

print(f"Time taken: {(time.time() - start_time):.5} seconds")
