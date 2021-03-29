L = open("03_input.txt", "r").readline().strip()

# Part 1
H = {(0, 0)}
x, y = 0, 0
for ch in L:
    if ch == "^":
        y += 1
    elif ch == "v":
        y -= 1
    elif ch == ">":
        x += 1
    elif ch == "<":
        x -= 1
    else:
        print("ERROR!")
    H.add((x, y))
print(len(H))

# Part 2
H = {(0, 0)}
x, y = 0, 0
rx, ry = 0, 0
santa = 1  # Santa's turn
robot = 0  # Robot's turn
for ch in L:
    if ch == "^":
        y += santa
        ry += robot
    elif ch == "v":
        y -= santa
        ry -= robot
    elif ch == ">":
        x += santa
        rx += robot
    elif ch == "<":
        x -= santa
        rx -= robot
    else:
        print("ERROR!")
    H.add((x, y))
    H.add((rx, ry))
    santa = 1 - santa
    robot = 1 - robot
print(len(H))