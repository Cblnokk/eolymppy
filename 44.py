n=int(input())
a=[0]*(n+1)
a[1]=1
for i in range(2,n+1):
    m=n
    for j in range(2,round(i**0.5)+1):
        if((i%j) == 0 and a[j]+a[i//j]<m):
            m=a[j]+a[i//j]
    a[i]=min(a[i-1]+1,m)
print(a[n])

'''
while(True):
        k+=1
'''