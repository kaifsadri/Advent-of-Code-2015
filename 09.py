from itertools import permutations

L = open("09_input.txt", "r").readlines()

# parse distances in a dict like this: D[(A,B)]=D[(B,A)]=X
D = dict()  # distances
Stars = set()  # Stars
for line in L:
    s, d = line.strip().split(" = ")
    s1, s2 = s.split(" to ")
    D[(s1, s2)] = int(d)
    D[(s2, s1)] = int(d)
    Stars.add(s1)
    Stars.add(s2)

Mn = 1e6  # just some large number to overwrite immediately
Mx = 0

DONE = set()
for order in permutations(Stars):
    if order in DONE:
        continue
    DONE.add(order)
    DONE.add(reversed(order))
    m = 0
    for i in range(1, len(order)):
        m += D[(order[i], order[i - 1])]
    if m < Mn:
        Mn = m
    if m > Mx:
        Mx = m

print("Part1: ", Mn, "\nPart2: ", Mx)
