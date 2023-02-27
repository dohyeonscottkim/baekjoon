import sys

n = int(sys.stdin.readline().rstrip())

q = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        try:
            print(q.pop(0))
        except:
            print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif cmd[0] == "back":
        try:
            print(q[-1])
        except:
            print(-1)
