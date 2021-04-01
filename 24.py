from itertools import combinations
from math import prod

P = sorted([int(line.strip()) for line in open("24_input.txt", "r").readlines()])

# establish a min for size of each set:
for i in range(len(P)):
    if sum(P[i:]) < sum(P) // 3:
        MN = len(P) - i + 1
        break

# This is a hack but it works:
# find the smallest group that makes the target and print it:
found = False
for i in range(MN, len(P)):
    for s in combinations(P, i):
        if sum(s) == sum(P) // 3:
            print("Part 1: ", prod(s))
            found = True
        if found:
            break
    if found:
        break

for i in range(len(P)):
    if sum(P[i:]) < sum(P) // 3:
        MN = len(P) - i + 1
        break

found = False
for i in range(MN, len(P)):
    for s in combinations(P, i):
        if sum(s) == sum(P) // 4:
            print("Part 2: ", prod(s))
            found = True
        if found:
            break
    if found:
        break
