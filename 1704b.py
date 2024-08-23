m,n=map(int,input().split())
a=[[0]*(n+1) for i in range(m+1)]
for i in range(1,m+1):
    a[i][1]=1

for j in range(1,n+1):
    a[1][j]=1

for i in range(2,m+1):
    for j in range(2, n + 1):
        a[i][j]=a[i-1][j]+a[i][j-1]

print(a)
print(a[m][n])


