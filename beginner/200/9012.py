n = int(input())

for i in range(n):
    stack = []
    ps = str(input())
    isVPS = 1
    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            try:
                stack.pop(-1)
            except:
                isVPS = 0
                break
    if isVPS == 0:
        print("NO")
    elif len(stack) != 0:
        print("NO")
    else:
        print("YES")