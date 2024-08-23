n,t=map(int,input().split())
a=list(map(int, input().split()))
res=0
for i in range(n):
    t-=a[i]
    if(t>=0):
        res+=1
print(res)
