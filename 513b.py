n,m=map(int,input().split())
if(n>=m):
    res=0
else:
    res=1
    for i in range(1,n+1):
        res=(res*i)%m
print(res)

