t = int(input())

def sieveOfErastosthenes(number:int):
    primeList = [1 for _ in range(number+1)]
    
    primeList[0] = 0
    primeList[1] = 0
    
    primeNumbers = []
    for i in range(2, int(number**1/2) +1):
        n = 2
        while i*n <= number:
            primeList[i*n] = 0
            n += 1
            
    return primeList

for i in range(t):
    n = int(input())
    
    primeList = sieveOfErastosthenes(n)
    firstPrimeNumbers = [i for i in range(n//2+1) if primeList[i] == 1]
    secondPrimeNumbers = [i for i in range(n//2, n+1) if primeList[i] == 1]

    for i in firstPrimeNumbers[::-1]:
        if n-i in secondPrimeNumbers:
            print(f"{i} {n-i}")
            break