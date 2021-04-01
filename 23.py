P = [line.strip() for line in open("23_input.txt", "r").readlines()]


def run(a_val):
    R = {"a": a_val, "b": 0}
    ins = 0
    while True:
        try:
            t = P[ins].split(" ")
            if t[0] == "hlf":
                R[t[1]] //= 2
                ins += 1
            elif t[0] == "tpl":
                R[t[1]] *= 3
                ins += 1
            elif t[0] == "inc":
                R[t[1]] += 1
                ins += 1
            elif t[0] == "jmp":
                ins += int(t[1])
            elif t[0] == "jie":
                if R[t[1][:-1]] % 2 == 0:
                    ins += int(t[2])
                else:
                    ins += 1
            elif t[0] == "jio":
                if R[t[1][:-1]] == 1:
                    ins += int(t[2])
                else:
                    ins += 1
        except IndexError:
            break

    print(f'Part {a_val+1}: {R["b"]}')


run(0)
run(1)