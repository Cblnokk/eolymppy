n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
k=a[n-1]
for i in range(k,0,-1):
    p=0
    #print(i)
    for j in range(0,n):
        #print(a[j]//i)
        p=p+a[j]//i
    if(p>=m):
        p1=i
        break

print(p1)