i = 100
cnt = 0

for i in range(100, 1000):
    one = i % 10
    two = (i//10) % 10
    three = (i // 100) % 10
    #print(three, two, one)
    if(three == two):
        a = 0
    elif(three < two):
        a = 1
    else:
        a = -1
    
    if(two == one):
        b = 0
    elif(two < one):
        b = 1
    else:
        b = -1

    if(a*b == -1):
        cnt += 1
    
print("1번 변화하는 수의 개수 : ", cnt)
