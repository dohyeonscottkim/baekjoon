n = int(input())

arr = list(map(int, input().split()))

f = [0] * 1000001

for i in arr:
    f[i] += 1

answer = [-1] * n
stack = []


stack.append(0)

for i in range(1, n):
    while stack and f[arr[i]] > f[arr[stack[-1]]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)