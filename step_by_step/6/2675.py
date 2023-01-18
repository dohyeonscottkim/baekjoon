t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    s = list(s)
    
    newS = []
    
    for j in s:
        newS.append(j*r)
    
    print(*newS, sep="")