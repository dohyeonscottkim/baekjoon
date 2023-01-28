m = int(input())
n = int(input())

def isPrimeNumber(number:int):
    if number == 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1

primeNumber = []

for i in range(m, n+1):
    if isPrimeNumber(i) == 1:
        primeNumber.append(i)

if len(primeNumber) == 0:
    print(-1)
else:   
    print(sum(primeNumber))
    print(min(primeNumber)) 