from collections import Counter

N = 33100000  # Pzzle input

P = Counter()  # Present counter
for elf in range(1, N // 20 + 1):
    for house in range(elf, N // 10, elf):
        P[house] += elf * 10
print("Part 1: ", min([i for i in P if P[i] > N]))

P.clear()
for elf in range(1, N // 2 + 1):
    for house in range(elf, min(elf * 50 + 1, N), elf):
        P[house] += elf * 11
print("Part 2: ", min([i for i in P if P[i] > N]))