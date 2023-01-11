a = int(input())
b = map(int, list(input()))
b1, b2, b3 = b


print(a * b3)
print(a * b2)
print(a * b1)
print(a * (b1*100 + b2*10 + b3))