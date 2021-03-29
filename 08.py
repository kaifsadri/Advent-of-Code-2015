print(
    "Part 1: ",
    sum([len(line) - 1 - len(eval(line)) for line in open("08_input.txt", "r").readlines()]),
    "\nPart 2: ",
    sum([line.count("\\") + line.count('"') + 2 for line in open("08_input.txt", "r").readlines()]),
)
