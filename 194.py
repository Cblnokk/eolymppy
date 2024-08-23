n=int(input())
a=[0]*10
d=2
while(n>1) and (d<8):
    if(n%d==0):
        n//=d
        a[d]+=1
    else:
        d+=1
b=a.copy()
while(a[3]>1):
    a[9]+=1
    a[3]-=2

while(a[2]>2):
    a[8]+=1
    a[2]-=3

while(a[2]>0) and (a[3]>0):
    a[6]+=1
    a[2]-=1
    a[3]-=1

while(a[2]>1):
    a[4]+=1
    a[2]-=2

if(n>1):
    print("-1 -1")
else:
    for i in range(1,10):
        for j in range(1,a[i]+1):
            print(i,end="")
    print(end=" ")
    for i in range(9,0,-1):
        for j in range(1,b[i]+1):
            print(i,end="")

