from itertools import combinations
from collections import Counter

L = sorted(int(line.strip()) for line in open("17_input.txt", "r").readlines())
# upper and lower bounds of combinations
lo = 150 // max(L) + 1
hi = sum([1 for i in range(len(L)) if L[i] * (i + 1) <= 150]) + 1

C = 0
D = Counter()
for n in range(lo, hi + 1):
    for c in combinations(L, n):
        if sum(c) == 150:
            C += 1
            D[len(c)] += 1
print("Part 1: ", C, "\nPart 2: ", D[min(D.keys())])
