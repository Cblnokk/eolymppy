n=int(input())
a = [[0 for j in range(n)] for i in range(n)]
k=0
for i in range(n):
    for j in range(n):
        f=k+j+a[i-1][j]
        if(f>100):
            a[i][j]=10
        else:
            a[i][j]=f
    k+=1

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()