import time
import re

start_time = time.time()

with open('C:\\Users\\peter\\Downloads\\Advent of Code\\Day 4\\input.txt', 'r') as f:
  data = f.read().split("\n\n")
  
counter = 0

for i in data:
  if 'byr' in i and 'iyr' in i and 'hgt' in i and 'eyr' in i and 'ecl' in i and 'pid' in i and 'hcl' in i:
    counter += 1
    
print("Part 1: ", counter)

REQUIREMENTS = [
    ("byr", lambda x: 1920 <= int(x) <= 2002),
    ("iyr", lambda x: 2010 <= int(x) <= 2020),
    ("eyr", lambda x: 2020 <= int(x) <= 2030),
    ("hgt", lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)),
    ("hcl", lambda x: re.fullmatch(r"#[0-9a-f]{6}", x)),
    ("ecl", lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    ("pid", lambda x: re.fullmatch(r"[0-9]{9}", x)),
]

counter = 0

for person in data:
  passport = {}
  person = person.split()
  for section in person:
    key, value = section.split(":")
    passport[key] = value
  test = True
  for key, req in REQUIREMENTS:
    if key not in passport:
      test = False
      break
    if not req(passport[key]):
      test = False
  if test:
    counter += 1

    
print("Part 2: ", counter)

print(f"Time taken: {(time.time() - start_time):.5} seconds")