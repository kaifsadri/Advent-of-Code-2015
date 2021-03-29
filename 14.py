from collections import Counter

L = open("14_input.txt", "r").readlines()

R = dict()  # Reindeer parameters
for line in L:
    t = line.split(" ")
    R[t[0]] = list(map(int, (t[3], t[6], t[13])))

N = 2503
D = Counter()  # distance for each deer
P = Counter()  # points accumulated
for t in range(N):
    for r in R:
        rem = t % (R[r][1] + R[r][2])
        if rem < R[r][1]:  # deer moves if it is not tired
            D[r] += R[r][0]
    # now find who's ahead and divide points:
    M = max(D.values())
    for r in R:
        if D[r] == M:
            P[r] += 1

print("Part 1:", max(D.values()))
print("Part 2:", max(P.values()))