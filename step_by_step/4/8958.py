n = int(input())

for i in range(n):
    a = list(str(input()))
    total = 0
    score = 1
    for j in a:
        if j == 'O':
            total += score
            score += 1
        if j == 'X':
            score = 1
    
    print(total)