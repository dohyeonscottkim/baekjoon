n = int(input())

words = []

for i in range(n):
    word = str(input())
    item = [len(word), word]
    if item not in words:
        words.append(item)
        
words.sort()

for i in range(len(words)):
    print(words[i][1])