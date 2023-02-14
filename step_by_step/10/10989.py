# use counting sort
# numbers are natural numbers but smaller than 10000
# number of digits is between 1 and 10000000

# use sys.stdin.readline & sys.stdout.write instead of input & print

import sys

n = int(sys.stdin.readline())

arr = [0 for i in range(10000 + 1)]

for i in range(n):
    arr[int(sys.stdin.readline())] += 1


for i in range(1, 10000+1):
    for j in range(arr[i]):
        sys.stdout.write(str(i) + '\n')