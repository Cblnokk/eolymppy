n,m=map(int,input().split())
a = [[0 for j in range(m)] for i in range(n)]
b = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j]=i*m+j+1
        b[i][j]=j*n+i+1
sum=0
for i in range(n):
    for j in range(m):
        if(a[i][j]==b[i][j]):
            sum+=1
print(sum)