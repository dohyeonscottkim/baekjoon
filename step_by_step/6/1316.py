def isGWord(word:str):
    flag = [0 for i in range(26)]
    i = 0
    while i < len(word):
        if flag[ord(word[i]) - 97] == 0:
            alphabet = word[i]
            flag[ord(word[i]) - 97] = 1
            i += 1
            while i < len(word) and word[i] == alphabet:
                i += 1
        else:
            return False
        
    return True


n = int(input())
nGWord = 0

for i in range(n):
    word = input()
    if isGWord(word) == True:
        nGWord += 1

print(nGWord)
    