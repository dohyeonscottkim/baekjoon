m = []
maxRow = []
for i in range(9):
    row = list(map(int, input().split()))
    
    m.append(row)
    maxRow.append(max(row))
    
maxNumber = max(maxRow)
print(maxNumber)

maxRowIndex = maxRow.index(maxNumber)
maxColumnIndex = m[maxRowIndex].index(maxNumber)

print(f"{maxRowIndex+1} {maxColumnIndex+1}")

