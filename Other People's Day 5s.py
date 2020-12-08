import time

start_time = time.time()

inputList = [int(line.translate("".maketrans('FBLR', '0101')), 2) for line in open('C:\\Users\\peter\\Downloads\\Advent of Code\\Day 5\\input.txt')]

# Part I
print(f'Highest seat-id: {max(inputList)}')

# Part II
print(f'Missing seat-id: {set(range(min(inputList), max(inputList))) - set(inputList)}')

print(f"Time taken: {(time.time() - start_time):.5} seconds")

######### BREAK #########

import fileinput

start_time = time.time()

t = str.maketrans("FBLR", "0101")
s = set(int(l.translate(t), 2) for l in fileinput.input('C:\\Users\\peter\\Downloads\\Advent of Code\\Day 5\\input.txt'))
lo, hi = min(s), max(s)

print(hi)
print(next(i for i in range(lo + 1, hi) if i not in s))

print(f"Time taken: {(time.time() - start_time):.5} seconds")
