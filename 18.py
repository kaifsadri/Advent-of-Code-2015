from collections import defaultdict

L = [line.strip() for line in open("18_input.txt", "r").readlines()]
P = defaultdict(lambda: 0)

for i in range(len(L)):
    for j in range(len(L)):
        if L[i][j] == "#":
            P[(i, j)] = 1

P2 = P.copy()


def iterate1():
    global P
    p = P.copy()
    for i in range(len(L)):
        for j in range(len(L)):
            n = 0
            for k in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if P[(i + k[0], j + k[1])] == 1:
                    n += 1
            if P[(i, j)] == 1:
                if n in {2, 3}:
                    p[(i, j)] = 1
                else:
                    p[(i, j)] = 0
            else:
                if n == 3:
                    p[(i, j)] = 1
    P = p


for i in range(100):
    iterate1()
print("Part 1: ", sum(P.values()))


P = P2
P[(0, 0)] = 1
P[(0, 99)] = 1
P[(99, 99)] = 1
P[(99, 0)] = 1


def iterate2():
    global P
    p = P.copy()
    for i in range(len(L)):
        for j in range(len(L)):
            if (i, j) not in [(0, 0), (0, 99), (99, 99), (99, 0)]:
                n = 0
                for k in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if P[(i + k[0], j + k[1])] == 1:
                        n += 1
                if P[(i, j)] == 1:
                    if n in {2, 3}:
                        p[(i, j)] = 1
                    else:
                        p[(i, j)] = 0
                else:
                    if n == 3:
                        p[(i, j)] = 1
    P = p


for i in range(100):
    iterate2()
print("Part 2: ", sum(P.values()))