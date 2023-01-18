a, b = map(list, input().split())

reverseA = 0
reverseB = 0

for i in range(3):
    reverseA += int(a[i]) * (10**i)
    reverseB += int(b[i]) * (10**i)
    
print(max(reverseA, reverseB))