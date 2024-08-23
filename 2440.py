n=int(input())
for i in range(n):
    x = list(map(int, input().split()))
    a=x[0]
    x.remove(a)
    x.sort()
    print(i+1,x[-3])
