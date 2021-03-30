L = [line.strip() for line in open("19_input.txt", "r").readlines()]
M = L.pop(-1)
L.pop(-1)

R = list()
for line in L:
    t = line.split(" => ")
    R.append((t[0], t[1]))

S = set()
# now parse the rplacements:
for e in R:
    f = M.find(e[0], 0)
    while f != -1:
        S.add(M[:f] + e[1] + M[f + len(e[0]) :])
        f = M.find(e[0], f + 1)

print("Part 1: ", len(S))

# fortunately, element mappnigs are such that the length is reduced
# for each transformation.
step = 0
m = M
while m != "e":
    for e in R:
        if e[1] not in m:
            continue
        m = m.replace(e[1], e[0], 1)
        step += 1

print("Part 2: ", step)