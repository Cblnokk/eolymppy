n=int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
n1=0
n2=0
for i in range(n):
    n1+=a[i][i]
    n2+=a[i][n-1-i]
print(n1,n2)
