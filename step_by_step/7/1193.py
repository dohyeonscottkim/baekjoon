x = int(input())

fraction = "1/1"
i = 1
straight = 1

while x - i > 0:
    x -= i
    i += 1
    straight *= -1

if straight == 1:
    print(f"{i-x+1}/{x}")
else:
    print(f"{x}/{i-x+1}")