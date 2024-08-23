n=int(input())
if (n == 1):
    print(1)
else:
    a=list(map(int,input().split()))
    k=(n*(n+1))//2
    s=sum(a)
    print(k-s)