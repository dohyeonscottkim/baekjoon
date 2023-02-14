n = int(input())

arr = []

count = [0 for i in range(8000 + 1)]

for i in range(n):
    number = int(input())
    arr.append(number)
    count[number + 4000] += 1

mean = round(sum(arr)/n)
    
arr.sort()
median = arr[n//2]

rangeArr = arr[-1] - arr[0]

maxCount = max(count)

maxArr = [i-4000 for i in range(8000 + 1) if count[i] == maxCount]

if len(maxArr) > 1:
    mode = maxArr[1]
else:
    mode = maxArr[0]
    
print(mean)
print(median)
print(mode)
print(rangeArr)



