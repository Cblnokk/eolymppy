n,m=map(int,input().split())
k=1
for i in range(1,n+1):
    k*=i
    k=k%m
print(k)

