from collections import Counter

L = open("06_input.txt", "r").readlines()

# Format:
# toggle 461,550 through 564,900
# turn off 370,39 through 425,839
# turn off 464,858 through 833,915
# turn off 812,389 through 865,874
# turn on 599,989 through 806,993

# some shapin'
for i, line in enumerate(L):
    if line[0:4] == "turn":
        L[i] = line[0:4] + "_" + line[5:]

# Part 1
G = Counter()

for line in L:
    inst, start, through, finish = line.strip().split(" ")
    start = tuple(map(int, start.split(",")))
    finish = tuple(map(int, finish.split(",")))
    for i in range(start[0], finish[0] + 1):
        for j in range(start[1], finish[1] + 1):
            if inst == "toggle":
                G[(i, j)] = 1 - G[(i, j)]
            elif inst == "turn_on":
                G[(i, j)] = 1
            elif inst == "turn_off":
                G[(i, j)] = 0
print("Part 1: ", sum(G.values()))

# Part 2
G = Counter()

for line in L:
    inst, start, through, finish = line.strip().split(" ")
    start = tuple(map(int, start.split(",")))
    finish = tuple(map(int, finish.split(",")))
    for i in range(start[0], finish[0] + 1):
        for j in range(start[1], finish[1] + 1):
            if inst == "toggle":
                G[(i, j)] += 2
            elif inst == "turn_on":
                G[(i, j)] += 1
            elif inst == "turn_off":
                G[(i, j)] -= 1
                if G[(i, j)] < 0:
                    G[(i, j)] = 0
print("Part 2: ", sum(G.values()))