c = int(input())

for i in range(c):
    a = list(map(int, input().split()))
    n, score = a[0], a[1:]
    meanScore = sum(score)/n
    aboveAverage = 0
    for j in score:
        if j > meanScore:
            aboveAverage += 1
    print(f"{aboveAverage/n*100:.3f}%")
    