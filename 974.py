n=int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(a[i][k]+a[k][j]<a[i][j]):
                a[i][j]=a[i][k]+a[k][j]
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()