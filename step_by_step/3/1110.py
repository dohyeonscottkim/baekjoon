#solution 1

# n = str(input())

# def sum(n:str):
#     if len(n) == 1:
#         return str(int(n))
#     else:
#         return str(int(n[0]) + int(n[1]))
    
# def new(new_n:str):
#     return new_n[-1] + sum(new_n)[-1]

# new_n = new(n)
# cycle = 1

# while True:
#     if int(new_n) == int(n):
#         print(cycle)
#         break
#     # print(new_n)
#     new_n = new(new_n)
#     cycle += 1
    
#solution 2
n = int(input())
new = n
count = 0
while True:
    a = new // 10
    b = new % 10
    new = (a+b)%10 + b*10
    count += 1
    if new == n:
        print(count)
        break