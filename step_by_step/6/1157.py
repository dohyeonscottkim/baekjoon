word = str(input())

alphabet = {}

for i in range(97, 122 + 1):
    alphabet[chr(i)] = 0
    
for j in word:
    alphabet[j.lower()] += 1

nMostUsed = max(alphabet.values())

mostUsed = [k for k, v in alphabet.items() if v == nMostUsed]

if len(mostUsed) != 1:
    print('?')
else:
    print(mostUsed[0].upper())