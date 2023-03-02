import sys

n = int(sys.stdin.readline())

items = []

for i in range(n):
    
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        items.append(cmd[1])
    elif cmd[0] == "pop":
        if len(items) != 0:
            print(items.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(items))
    elif cmd[0] == "empty":
        if len(items) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(items) != 0:
            print(items[-1])
        else:
            print(-1)