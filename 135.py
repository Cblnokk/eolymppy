import math

n = int(input())
a = list(map(int,input().split()))

for i in range(0,n):
    for j in range(1+i,n):
        temp=math.gcd(a[i], a[j])
        a[j] //= temp

res = 1
for i in range(0,n):
    res = res * a[i]
print(res)
