from math import prod

L = open("15_input.txt", "r").readlines()

G = list()  # ingredients
for line in L:
    t = line.split(" ")
    G.append(list(map(int, (t[2][:-1], t[4][:-1], t[6][:-1], t[8][:-1], t[10][:-1]))))

MX = 0
MX500 = 0
for f in range(101):
    for c in range(101):
        for b in range(101):
            if (f + c + b) <= 100:
                s = 100 - f - c - b
                A = [f, c, b, s]
                F = [sum([G[i][j] * A[i] for i in range(len(A))]) for j in range(len(G))]
                if any(map(lambda x: x <= 0, F)):
                    P = 0
                else:
                    P = prod(F)
                    if MX < P:
                        MX = P
                    cals = sum([A[i] * G[i][4] for i in range(len(A))])
                    if cals == 500 and MX500 < P:
                        MX500 = P

print("Part 1: ", MX, "\nPart 2: ", MX500)
