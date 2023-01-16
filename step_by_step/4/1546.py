n = int(input())

a = list(map(int, input().split()))

maxA = max(a)

meanA = sum(a)/maxA*100/n

print(meanA)