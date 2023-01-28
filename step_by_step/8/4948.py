def sieveOfErastosthenes(number:int):
    primeList = [1 for _ in range(number+1)]
    
    primeList[0] = 0
    primeList[1] = 0
    
    for i in range(2, int(number**1/2) +1):
        n = 2
        while i*n <= number:
            primeList[i*n] = 0
            n += 1
            
    return primeList

while True:
    n = int(input())
    
    if n == 0:
        break
    
    primeList = sieveOfErastosthenes(2*n)
    
    print(sum(primeList[n+1:2*n+1]))