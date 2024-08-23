a,b,c,d=map(int,input().split())
x=0
a1=set()
if(a>b):
    a,b=b,a
if(c>d):
    c,d=d,c
for i in range(a,b+1):
    for j in range(c,d+1):
        a1.add(i*j)
print(len(a1))

