import sys

left = list(str(sys.stdin.readline().rstrip()))

n = int(sys.stdin.readline())

right = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    
    if cmd[0] == 'L' and len(left) > 0:
        right.append(left.pop(-1))
        
    elif cmd[0] == 'D' and len(right) > 0:
        left.append(right.pop(-1))
    
    elif cmd[0] == 'B' and len(left) > 0:
        left.pop(-1)
    
    elif cmd[0] == 'P':
        left.append(cmd[1])

s = left + right[::-1]
print(*s, sep="")