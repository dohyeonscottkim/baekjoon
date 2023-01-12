a, b = map(int, input().split())
c = int(input())

h = c // 60
m = c % 60

a += h
b += m

if b >= 60:
    b -= 60
    a += 1
    print(a % 24, b)
else:
    print(a % 24, b)