# solution 1 : O(n)
# def isPrimeNumber(number:int):
#     if number == 1:
#         return 0
#     for i in range(2, number):
#         if number % i == 0:
#             return 0
#     return 1

# solution 2
# def isPrimeNumber(number:int):
#     if number == 1:
#         return 0
#     for i in range(2, int(number ** 1/2) + 1):
#         if number % i == 0:
#             return 0
#     return 1

# solution 3 : Sieve of Eratosthenes
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
    
    

m, n = map(int, input().split())

primeList = sieveOfErastosthenes(n)

for i in range(m, n+1):
    if primeList[i] == 1:
        print(i)