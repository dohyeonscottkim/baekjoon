t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    numberOfPeople = [[i+1 for i in range(n)] for j in range(k+1)]
    
    for i in range(1, k):
        for j in range(n):
            numberOfPeople[i][j] = sum(numberOfPeople[i-1][:j+1])
    
    print(sum(numberOfPeople[k-1][:n+1]))