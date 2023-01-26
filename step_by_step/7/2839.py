n = int(input())

flag = -1

a = n // 5
minBag = 10000

for i in range(a+1):
    r = n - i*5
    if r % 3 == 0 & i + r//3 < minBag:
        minBag = i + r//3
        flag = 1
    
if flag != -1:
    print(minBag)
else:
    print(flag)