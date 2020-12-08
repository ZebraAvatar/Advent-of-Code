import time

start_time = time.time()

with open('input.txt', 'r') as f:
  data = f.readlines()

maxSeat = 0
seats = []

for i in data:
  seat = '0b'
  for j in i:
    if j == "F":
      seat += '0'
    elif j == 'B':
      seat += '1'
    elif j == "L":
      seat += '0'
    elif j == 'R':
      seat += '1'
  if int(seat, 2) > maxSeat:
    maxSeat = int(seat, 2)
  seats.append(int(seat,2))

print(maxSeat)

for i in range(850):
  if i not in seats and i + 1 in seats and i - 1 in seats:
    print(i)

print(f"Time taken: {(time.time() - start_time):.5} seconds")
