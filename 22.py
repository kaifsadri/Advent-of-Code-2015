from random import choice

price = {"m": 53, "d": 73, "s": 113, "p": 173, "r": 229}
timer = {"m": 0, "d": 0, "s": 6, "p": 6, "r": 5}


def play(part):
    global ITERATION
    ITERATION += 1
    t = {"m": 0, "d": 0, "s": 0, "p": 0, "r": 0}
    B = {"H": 55, "D": 8}  # Puzzle input
    P = {"H": 50, "M": 500}
    SPENT = 0
    while True:
        P["H"] -= part - 1
        if P["H"] <= 0:
            return (0, SPENT)
        P["A"] = 0
        for i in "prs":
            if t[i] > 0:
                if i == "s":
                    P["A"] = 7
                elif i == "p":
                    B["H"] -= 3
                elif i == "r":
                    P["M"] += 101
                t[i] -= 1
        if B["H"] <= 0:
            return (1, SPENT)  # win
        # random spell
        try:
            spell = choice([i for i in t if t[i] == 0 and price[i] <= P["M"]])
        except IndexError:
            return (0, SPENT)  # Out of spells
        SPENT += price[spell]
        P["M"] -= price[spell]
        if spell == "m":
            B["H"] -= 4
        elif spell == "d":
            B["H"] -= 2
            P["H"] += 2
        elif spell in "prs":
            t[spell] = timer[spell]
        # boss's turn:
        P["A"] = 0
        for i in "prs":
            if t[i] > 0:
                if i == "s":
                    P["A"] = 7
                elif i == "p":
                    B["H"] -= 3
                elif i == "r":
                    P["M"] += 101
                t[i] -= 1
        if B["H"] <= 0:
            return (1, SPENT)  # win
        # Boss's action:
        P["H"] -= B["D"] - P["A"]


ITERATION = 0
MIN = 1e10
while True:
    r = play(1)
    if ITERATION > 1e5:
        break
    if r[0] == 1 and r[1] < MIN:
        MIN = r[1]
        print(f"Spent {MIN} mana and won after {ITERATION} games.")
        ITERATIONS = 0
print("Part 1: ", MIN)

ITERATION = 0
MIN = 1e10
while True:
    r = play(2)
    if ITERATION > 1e5:
        break
    if r[0] == 1 and r[1] < MIN:
        MIN = r[1]
        print(f"Spent {MIN} mana and won after {ITERATION} games.")
        ITERATIONS = 0
print("Part 2: ", MIN)
