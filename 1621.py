n=int(input())
if (n == 0):
    print(1)
else:
    res=int((1 + abs(n)) * n // 2)
    if(n<0):
        print(res+1)
    else:
        print(res)