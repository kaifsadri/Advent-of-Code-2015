import re

L = open("16_input.txt", "r").readlines()

# Output:
SUE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for line in L:
    t = re.split(", |: | ", line.strip())
    # Build the sue and compare now:
    sue = dict()
    for i in range(len(t) // 2):
        sue[t[2 * i]] = int(t[2 * i + 1])
    s = sue.copy()
    s.pop("Sue")
    if s.items() <= SUE.items():
        print("Part 1: ", sue["Sue"])
