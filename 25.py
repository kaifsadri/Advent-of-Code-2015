Target = (2981, 3075)

code = 20151125
coord = (1, 1)
while True:
    if coord == Target:
        print("Part 1: ", code)
        break

    if coord[0] == 1:
        coord = (coord[1] + 1, 1)
    else:
        coord = (coord[0] - 1, coord[1] + 1)
    code = (code * 252533) % 33554393
