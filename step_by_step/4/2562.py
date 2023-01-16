a = []

for i in range(9):
    a.append(int(input()))
maxA = max(a)

print(maxA)
print(a.index(maxA) + 1)