n = int(input())

paper = set()

for i in range(n):
    x, y = map(int, input().split())
    
    for a in range(x, x+10):
        for b in range(y, y+10):
            paper.add(f"{a} {b}")

print(len(paper))