t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        floor = h
    else:
        floor = n % h
    
    if n % h == 0:
        roomNumber = n // h
    else:
        roomNumber = n // h + 1

    print(str(floor) + str(roomNumber).zfill(2))