n = int(input())

coordinates = []

for i in range(n):
    x, y = map(int, input().split())
    coordinates.append([y, x])
    

coordinates.sort()

for i in range(n):
    print(f"{coordinates[i][1]} {coordinates[i][0]}")