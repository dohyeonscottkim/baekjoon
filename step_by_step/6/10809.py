s = list(str(input()))
alphabet = {}

for i in range(97, 122 + 1):
    alphabet[chr(i)] = -1

for i in range(len(s)):
    char = s[i]
    if alphabet[char] != -1:
        continue
    else:
        alphabet[char] = i
        
print(*alphabet.values())