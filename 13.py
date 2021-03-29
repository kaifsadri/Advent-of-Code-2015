from itertools import permutations

L = open("13_input.txt", "r").readlines()

# parse distances in a dict like this: D[(A,B)]=D[(B,A)]=X
D = dict()  # happiness dict
G = set()  # guests
M = {"gain": 1, "lose": -1}
for line in L:
    t = line.split(" ")
    D[(t[0][0], t[-1][0])] = M[t[2]] * int(t[3])
    G.add(t[0][0])
    G.add(t[-1][0])

l = len(G)
Mx1 = 0
Mx2 = 0

# For part 1: it is a simple calculation of maximum for all permutations.
# Part 2, when you sit in between, will reset the change for that particular link to 0.
# so for part 2, we need to find the shittiest link and set it to 0 instead.
DONE = set()
for order in permutations(G):
    if order in DONE:
        continue
    DONE.add(order)
    DONE.add(reversed(order))
    m = 0
    shitty = 1e6  # absurd number
    for i in range(1, l + 1):
        s = D[(order[i % l], order[i - 1])] + D[(order[i - 1], order[i % l])]
        m += s
        if s < shitty:
            shitty = s
    if m > Mx1:
        Mx1 = m
        Mx2 = m - shitty

print("Part1: ", Mx1, "\nPart 2: ", Mx2)
