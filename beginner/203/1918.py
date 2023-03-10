infix = list(str(input()))

postfix = ""

stack = []

for i in infix:
    if i.isalpha():
        postfix += i
    else:
        if i == "(":
            stack.append(i)
        elif i in ["*", "/"]:
            while stack and stack[-1] in ["*", "/"]:
                postfix += stack.pop()
            stack.append(i)
        elif i in ["+", "-"]:
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
            
while stack:
    postfix += stack.pop()
    
print(postfix)