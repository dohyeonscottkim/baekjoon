n = int(input())

pn = list(str(input()))

stack = []

numbers = {}

for i in range(n):
    numbers[chr(i+65)] = int(input())

op = {"+": lambda x, y: x+y,
      "-": lambda x, y: x-y,
      "*": lambda x, y: x*y,
      "/": lambda x, y: x/y}


for i in pn:
    if i in numbers.keys():
        stack.append(numbers[i])
    else:
        y = stack.pop()
        x = stack.pop()
        
        temp = op[i](x, y)
        
        stack.append(temp)
        

print(f"{stack.pop():.2f}")