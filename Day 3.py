import time
from functools import reduce

start_time = time.time()

with open('input.txt', 'r') as f:
  hill = f.readlines()
  
# PART ONE # 
  
def ski(x,y):
  '''Input angle (x,y), output # trees hit'''
  counter = 0
  #Start at 0,0
  horizontal = 0
  vertical = 0
  while (vertical + y) < len(hill):
    horizontal += x  #Move right x indices
    horizontal %= 31 #Keep position on the slope of width = 31
    vertical += y    #Move down y indices
    if hill[vertical][horizontal] == '#':
      counter += 1
  return counter

print("Part one: ", ski(3,1))

# PART TWO #

routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

deaths = []

for x in routes:
  deaths.append(ski(x[0],x[1]))

print("Part two: ", reduce(lambda x,y: x*y, deaths))

print(f"Time taken: {(time.time() - start_time):.5} seconds")
