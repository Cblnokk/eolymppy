a=list(map(int,input().split()))
n=a[0]
a.remove(a[0])
ma=max(a)
mi=min(a)
for i in range(n):
    if(a[i]==ma):
        a[i]=mi
print(*a)