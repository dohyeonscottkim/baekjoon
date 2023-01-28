n = int(input())

numbers = list(map(int, input().split()))

def isPrimeNumber(number:int):
    if number == 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1
    
total = 0

for i in range(n):
    if isPrimeNumber(numbers[i]) == 1:
        total += 1

print(total)