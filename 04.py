import hashlib

L = "bgvyzdsv"

# Part 1 & 2
i = 1
inp = str.encode(L + str(i))
result = hashlib.md5(inp).hexdigest()

P1 = P2 = False

while True:
    if P1 and P2:
        break
    elif not P1 and result[0:5] == "00000" and result[0:6] != "000000":
        print("Part 1: ", i)
        P1 = True
    elif result[0:6] == "000000":
        print("Part 2: ", i)
        P2 = True
    i += 1
    inp = str.encode(L + str(i))
    result = hashlib.md5(inp).hexdigest()
