from itertools import groupby

p = "1113122113"

for i in range(50):
    p = "".join(str(len(list(g))) + str(k) for k, g in groupby(p))
    if i == 39:
        print("Part1: ", len(p))
print("Part2: ", len(p))
