import re
from collections import defaultdict

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
    sue = defaultdict(lambda: 0)
    for i in range(len(t) // 2):
        sue[t[2 * i]] = int(t[2 * i + 1])
    match = True
    s = sue.copy()
    s.pop("Sue")
    for k in s.keys():
        if k in {"cats", "trees"}:
            if SUE[k] >= s[k]:
                match = False
        elif k in {"pomeranians", "goldfish"}:
            if SUE[k] <= s[k]:
                match = False
        elif s[k] != SUE[k]:
            match = False
    if match:
        print("Part 2: ", sue["Sue"])
        break
