L = open("02_input.txt", "r").readlines()

# Part 1
Total = 0
for line in L:
    l, w, h = map(int, line.strip().split("x"))
    Total += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
print(Total)

# Part 2
Total = 0
for line in L:
    l, w, h = map(int, line.strip().split("x"))
    Total += w * h * l + min(l + w, w + h, h + l) * 2
print(Total)
