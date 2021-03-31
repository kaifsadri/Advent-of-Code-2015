from itertools import combinations


Weapons = [
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0],
]

# [0,0,0] added to simulate chooosing nothing
Armor = [
    [0, 0, 0],
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5],
]

# [0,0,0] added to simulate chooosing nothing
Rings = [
    [0, 0, 0],
    [0, 0, 0],
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3],
]


def play():
    global P, B
    while True:
        # player plays:
        B["HitPoints"] -= max(1, P["Damage"] - B["Armor"])
        if B["HitPoints"] <= 0:
            return "P"
        # boss plays:
        P["HitPoints"] -= max(1, B["Damage"] - P["Armor"])
        if P["HitPoints"] <= 0:
            return "B"


Wins = set()  # this holds the money spent on each win
Losses = set()
# simulate various scenarios
for w in Weapons:
    for a in Armor:
        for r1, r2 in combinations(Rings, 2):
            dosh = r1[0] + r2[0] + w[0] + a[0]
            B = {"HitPoints": 100, "Damage": 8, "Armor": 2}
            P = {
                "HitPoints": 100,
                "Damage": sum([x[1] for x in (a, w, r1, r2)]),
                "Armor": sum([x[2] for x in (a, w, r1, r2)]),
            }
            if "P" == play():
                Wins.add(dosh)
            else:
                Losses.add(dosh)
print("Part 1: ", min(Wins), "\nPart 2: ", max(Losses))
