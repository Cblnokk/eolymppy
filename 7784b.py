x1,x2,x3=map(int,input().split())
d=(x1+x2+x3)//2
if(x1==d or x2==d or x3==d):
    print(0)
elif(x1>d):
    print(1)
    print(x1-d,d)
elif(x2>d):
    print(2)
    print(x2-d,d)
elif(x3>d):
    print(3)
    print(x3-d,d)
else:
    print(1)
    print(d-x2,d-x3)