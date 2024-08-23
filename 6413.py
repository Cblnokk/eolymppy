t=int(input())
for i in range(t):
    sum=int(input())
    n=int(input())
    for j in range(n):
        q, p = map(int, input().split())
        sum+=q*p
    print(sum)