n = int(input())

arr = [i for i in range(n, 0, -1)]
stack = []
operations = []
isOperatable = 1
for i in range(n):
    number = int(input())
    try:
        if len(stack) == 0:
            stack.append(arr.pop(-1))
            operations.append('+')
        
        while stack[-1] != number:
            if stack[-1] < number:
                stack.append(arr.pop(-1))
                operations.append('+')
            elif stack[-1] > number:
                stack.pop(-1)
                operations.append('-')
        
        stack.pop(-1)
        operations.append('-')
    except:
        isOperatable = 0

if isOperatable == 0:
    print("NO")
else:
    for i in operations:
        print(i)