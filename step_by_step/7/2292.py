n = int(input()) - 1

room = 1
i = 6

while n > 0:
    n -= i
    i += 6
    room += 1
    
print(room)