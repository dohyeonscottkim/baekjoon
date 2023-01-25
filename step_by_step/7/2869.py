a, b, v = map(int, input().split())

climbPerDay = a - b

if (v-a) % climbPerDay == 0:
    day = (v-a) // climbPerDay + 1
else:
    day = (v-a) // climbPerDay + 2
    
print(day)