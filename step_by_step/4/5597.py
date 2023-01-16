# solution 1 44ms
# a = [i for i in range(1, 31)]

# for j in range(28):
#     a.remove(int(input()))
    
# a.sort()

# print(a[0])
# print(a[1])

# solution 2 36ms
a = [i for i in range(1, 31)]

b = []
for j in range(28):
    b.append(int(input()))

c = list(set(a) - set(b))    
c.sort()

print(c[0])
print(c[1])