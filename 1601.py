a,b=map(int,input().split())
while((a*b)!=0):
    if (a > b):
        a=a%b
    else:
        b=b%a
print(a+b)