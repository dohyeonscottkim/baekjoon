# solution 1

str2time = {
    "A":3, "B":3, "C":3,
    "D":4, "E":4, "F":4,
    "G":5, "H":5, "I":5,
    "J":6, "K":6, "L":6,
    "M":7, "N":7, "O":7,
    "P":8, "Q":8, "R":8, "S":8,
    "T":9, "U":9, "V":9,
    "W":10, "X":10, "Y":10, "Z":10
}

word = str(input())

time = 0

for i in word:
    time += str2time[i]
    
print(time)

# solution 2
# use list rather than dictionary... more faster...

timeList = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
word = str(input())
time = 0
for i in word: time += timeList[ord(i)-ord('A')]
print(time)