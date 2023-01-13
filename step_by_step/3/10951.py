#this problem was about how to end while loop when EOF

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
        
    except:
        break
