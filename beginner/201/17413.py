s = list(str((input())))

reversedS = []
reverse = []

while len(s) != 0:
    l = s.pop(0)
    if l == "<":
        reversedS += reverse[::-1]
        reverse = []
        reversedS.append(l)
        while True:
            pop = s.pop(0)
            if pop == ">":
                reversedS.append(pop)
                break
            reversedS.append(pop)
    elif l == " ":
        reversedS += reverse[::-1]
        reverse = []
        reversedS.append(l)
    else:
        reverse.append(l)

reversedS += reverse[::-1]

print(*reversedS, sep = "")