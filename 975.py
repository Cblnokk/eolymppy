n=int(input())
a = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    for j in range(n):
        if(a[i][j]==-1):
            a[i][j]=10000000

for k in range(n):
    for i in range(n):
        for j in range(n):
            if(a[i][k]+a[k][j]<a[i][j]):
                a[i][j]=a[i][k]+a[k][j]

ma=0
for i in range(n):
    for j in range(n):
        if(a[i][j]>ma and a[i][j]!=10000000):
            ma=a[i][j]
print(ma)

