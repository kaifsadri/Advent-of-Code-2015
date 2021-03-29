L = open("07_input.txt", "r").readlines()
# Format:
# lf AND lq -> ls
# iu RSHIFT 1 -> jn
# bo OR bu -> bv
# gj RSHIFT 1 -> hc
# et RSHIFT 2 -> eu
# bv AND bx -> by
# is OR it -> iu
# b OR n -> o
# gf OR ge -> gg
# NOT kt -> ku
# ea AND eb -> ed
# kl OR kr -> ks


# Parse into a dictionary of equations:
# for example: kl OR kr -> ks becomes O["ks"] = ["kl", "OR", "kr"]
D = dict()
for line in L:
    eq, res = line.strip().split(" -> ")
    D[res] = eq.split(" ")

# Part 1
R = dict()  # A dict for the known signals and their values. This cuts recursion time.


def calculate(signal: str):
    try:
        return int(signal)
    except ValueError:
        pass  # do the rest
    if signal in R:
        return R[signal]
    else:
        result = 0
        eq = D[signal]
        if len(eq) == 1:  # This is a hard wire
            result = calculate(eq[0])
        else:
            if eq[-2] == "NOT":
                result = ~calculate(eq[1]) & 0xFFFF  # unsigned operation
            elif eq[-2] == "AND":
                result = calculate(eq[0]) & calculate(eq[2])
            if eq[-2] == "OR":
                result = calculate(eq[0]) | calculate(eq[2])
            if eq[-2] == "RSHIFT":
                result = calculate(eq[0]) >> int(eq[2])
            if eq[-2] == "LSHIFT":
                result = calculate(eq[0]) << int(eq[2])
        R[signal] = result
    return R[signal]


part1 = calculate("a")
print("Part 1: ", part1)

# part 2 starts with a known "b"
R = {"b": part1}
print("Part 2: ", calculate("a"))