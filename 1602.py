a,b=map(int,input().split())
a1=a
b1=b
while((a*b)!=0):
    if (a > b):
        a=a%b
    else:
        b=b%a

print(a1*b1//(a+b))