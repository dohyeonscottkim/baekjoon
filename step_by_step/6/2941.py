word = str(input())

cAlphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
count = 0

while i < len(word):
    if i+2 <= len(word) or i+3 <= len(word):
        if word[i:i+2] in cAlphabet:
            count += 1
            i += 2
        elif word[i:i+3] in cAlphabet:
            count += 1
            i += 3
        else:
            count += 1
            i += 1
    else:
        count += 1
        i += 1
        
print(count)