n = int(input())

for i in range(n):
    sentence = map(str, input().split())
    
    for i in sentence:
        print(i[::-1], end = " ")