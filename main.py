k=int(input())
a = [[1 for j in range(71)] for i in range(71)]

for i in range(1,71):
    for j in range(1,71):
        a[i][j]=a[i-1][j]+a[i][j-1]
#print(a)
for i in range(k):
    n,t,p= map(int, input().split())
    k1=t-(n*p)

    print(a[n-1][k1])

