line = list(str(input()))

q = []

slices = 0

while len(line) != 0:
    p = line.pop(0)
    
    if p == "(":
        if line[0] == ")":
            slices += len(q)
            q.append(p)
        else:
            q.append(p)
            slices += 1
    else:
        q.pop()
print(slices)