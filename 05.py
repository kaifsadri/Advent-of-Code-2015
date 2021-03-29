L = open("05_input.txt", "r").readlines()

# Part 1
def isnice1(s):
    if sum([s.count(c) for c in "aeiou"]) < 3:
        return False
    if sum([s.count(c + c) for c in "abcdefghijklmnopqrstuvwxyz"]) == 0:
        return False
    if sum([s.count(c) for c in ["ab", "cd", "pq", "xy"]]) != 0:
        return False
    return True


N = 0
for line in L:
    if isnice1(line.strip()):
        N += 1

print("Part 1: ", N)

# Part 2
def isnice2(s):
    if (
        max(
            [
                s.count(c + d)
                for c in "abcdefghijklmnopqrstuvwxyz"
                for d in "abcdefghijklmnopqrstuvwxyz"
            ]
        )
        < 2
    ):
        return False
    if (
        max(
            [
                s.count(c + d + c)
                for c in "abcdefghijklmnopqrstuvwxyz"
                for d in "abcdefghijklmnopqrstuvwxyz"
            ]
        )
        == 0
    ):
        return False
    return True


N = 0
for line in L:
    if isnice2(line.strip()):
        N += 1

print("Part 2: ", N)