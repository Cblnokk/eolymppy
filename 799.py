n=int(input())
i=0
a = [[int(j) for j in input().split()] for i in range(n)]


for i in range(3):
    for j in range(n):
        a[i][j] = max(a[i - 1][j], a[i][j - 1]) + a[i][j]
print(a)
