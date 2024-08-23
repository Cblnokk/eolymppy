a=list(map(int,input().split()))
n=a[0]
a.remove(n)
a.sort()
f=0
for i in range(1,n):
    #print(a[i-1],i)
    if(a[i-1]!=i):
        f=1
        break

if(f!=1):
    print(i+1)
else:
    print(i)