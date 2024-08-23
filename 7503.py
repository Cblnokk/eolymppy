n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
k=m
res=1
for i in range(n):
    k-=a[i]
    if(k<0):
        while(k<0):
            res+=1
            k+=m
while(res<a[-1]):
    res+=1
print(res)

