numbers = list(str(input()))

arr = [int(i) for i in numbers]

arr.sort(reverse = True)

print(*arr, sep="")