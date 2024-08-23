a=list(map(int,input().split()))
n=a[0]
a.remove(n)
if(n==4):
    print(sum(a))
else:
    m=0
    for i in range(n-1):
        if(a[m]+a[m+1]<a[i]+a[i+1]):
            m=i
    max1=a[m]+a[m+1]
    a[m]=-1
    a[m+1] = -1

    m=0
    for i in range(n-1):
        if (a[m]+a[m+1]<a[i]+a[i+1]):
            m = i
    max2 = a[m] + a[m + 1]
    print(max1+max2)
