a, b, c = map(int, input().split())

if b >= c:
    print("-1")
else:
    be_point = a // (c-b) + 1
    print(be_point)