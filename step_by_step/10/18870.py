n = int(input())

coordinates =list(map(int, input().split()))

sortedCoordinates = sorted(list(set(coordinates)))

dictCoordinates = {x:i for i, x in enumerate(sortedCoordinates)}

idxArr = []

for i in range(n):
    idx = dictCoordinates[coordinates[i]]
    idxArr.append(idx)
    
print(*idxArr)