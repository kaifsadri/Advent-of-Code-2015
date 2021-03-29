import json

line = open("12_input.txt", "r").readline().strip()

# Part 1
S = 0
A = "-0123456789"
r = ""
for c in line:
    if c in A:
        r += c
    else:
        if r != "":
            S += int(r)
            r = ""
print("Part 1: ", S)

# Part 2:
J = json.loads(line)


def calc(j):
    S = 0
    if str(type(j)) == "<class 'int'>":
        return j
    if str(type(j)) == "<class 'list'>":
        for item in j:
            try:
                S += calc(item)
            except ValueError:
                pass
    if str(type(j)) == "<class 'dict'>":
        if "red" in j.values():
            return 0
        for item in j.values():
            try:
                S += calc(item)
            except ValueError:
                pass
    if str(type(j)) == "<class 'set'>":
        if "red" in j:
            return 0
        for item in j:
            try:
                S += calc(item)
            except ValueError:
                pass
    return S


print("Part 2: ", calc(J))