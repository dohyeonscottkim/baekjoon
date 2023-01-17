def hansoo(n:int):
    if n <= 99:
        return True
    
    a = list(map(int, str(n)))
       
    diff = []
    
    for i in range(len(a) - 1):
        diff.append(a[i]-a[i+1])
    
    diff = set(diff)
    
    if len(diff) == 1:
        return True
    else:
        return False
    

n = int(input())

count = 0

for i in range(1, n+1):
    if hansoo(i) == True:
        count += 1

print(count)