n = int(input())

coordinates = []

for i in range(n):
    x, y = map(int, input().split())
    coordinates.append([x, y])

coordinates.sort()

for i in range(n):
    print(*coordinates[i])