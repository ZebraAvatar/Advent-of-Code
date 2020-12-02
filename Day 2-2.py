import time
import re

start_time = time.time()


with open('C:\\Users\\peter\\Downloads\\Advent of Code\\Day 2\\input.txt') as f:
 regex = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
 entries = [regex.match(x).groups() for x in f.readlines()]

counter = [int(a) <= string.count(c) <= int(b) for a,b,c,string in entries]
print(sum(counter))

counter = [(c == string[int(a) - 1]) != (c == string[int(b) - 1]) for a,b,c,string in entries]

print(sum(counter))

print(f"Time taken: {(time.time() - start_time):.5} seconds")