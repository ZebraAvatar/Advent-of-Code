# Advent of Code Day 2

import time

start_time = time.time()

file = open('C:\\Users\\peter\\Downloads\\Advent of Code\\Day 2\\input.txt', 'r')
data = file.read().splitlines()

data = [part.split(" ") for part in data]
for i in range(len(data)):
  data[i][0] = data[i][0].split("-")
  data[i][0] = list(map(int, data[i][0]))

counter = 0
for i in data:
  y = "".join(sorted(i[2]))
  if i[1][0]*i[0][0] in y and i[1][0]*(i[0][1] + 1) not in y:
    counter += 1

print("Part one: ", counter)

counter = 0

for i in data:
  if (i[2][(i[0][0]-1)] == i[1][0]) is not (i[2][(i[0][1]-1)] == i[1][0]):
    counter += 1
  
print("Part two: ", counter)

print(f"Time taken: {(time.time() - start_time):.5} seconds")