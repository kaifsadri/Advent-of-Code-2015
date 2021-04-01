# To continue, please consult the code grid in the manual.  Enter the code at row 2981, column 3075.
Target = (2981, 3075)


def next_code(code):
    return (code * 252533) % 33554393


def next_coord(c):
    if c[0] == 1:
        return (c[1] + 1, 1)
    else:
        return (c[0] - 1, c[1] + 1)


code = 20151125
coord = (1, 1)
while True:
    nextcoord = next_coord(coord)
    nextcode = next_code(code)
    if coord == Target:
        print("Part 1: ", code)
        break
    code = nextcode
    coord = nextcoord
