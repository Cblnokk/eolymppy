n=input()
max1='0'
min1='9'
n1=len(n)
for i in range (0,n1):
    if(n[i]>max1):
        max1=n[i]
        imax=i
    if (n[i] < min1):
        min1 = n[i]
        imin = i

n[imax]=min1
n[imin]=max1