n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
josephus = []

d = 0

while len(arr) != 0:
    d += k-1
    if d >= len(arr):
        d = d % len(arr)
    
    josephus.append(arr.pop(d))

print("<", end="")
print(*josephus, sep = ", ", end = "")
print(">")

