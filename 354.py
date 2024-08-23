x=list(map(int,input().split()))
n=x[0]
x.remove(n)
ma=max(x)
x1=[0]*(ma+1)
f=0
for i in range(n):
    a=x[i]
    x1[a]+=1

for i in range(1,ma+1):
    if(x1[i]==0):
        f=i
if(f==0):
    print(0)
else:
    print(f)