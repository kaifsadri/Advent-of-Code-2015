L = open("01_input.txt", "r").readline().strip()

# Part 1
print(L.count("(") - L.count(")"))

# Part 2
pos = 0
ind = 0
while pos != -1:
    if L[ind] == "(":
        pos += 1
    if L[ind] == ")":
        pos -= 1
    ind += 1
print(ind)