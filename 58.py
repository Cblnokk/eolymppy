m,n =map(int,input().split())
a=m
b=n
while(a!=0 and b!=0):
    if (a > b):
        a=a%b
    else:
        b=b%a
k=a+b
n=n//k
m=m//k
nsk=(m*n//k)
n1=(nsk//n)
m1=(nsk//m)
v=n1+m1-2
if(n1%2==0):
    l=2
else:
    if(m1%2==0):
        l=4
    else: l=3
print(v,l)
