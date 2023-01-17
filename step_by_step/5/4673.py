# self number

wholeN = {i for i in range(1, 10001)}

not_selfN = []

def d(n:int):
    return n + sum(list(map(int, str(n))))

for i in range(1, 10001):
    dn = d(i)
        
    while dn <= 10000:
        not_selfN.append(dn)
        dn = d(dn)
    
not_selfN = set(not_selfN)

selfN = wholeN - not_selfN

selfN = list(selfN)
selfN.sort()

for i in selfN:
    print(i)
