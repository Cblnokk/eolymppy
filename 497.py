n1=int(input())
for i in range(n1):
    n=int(input())
    mi=0
    ma=32
    for j in range(n):
        a, b = map(int, input().split())
        if(a>mi):
            mi=a
        if (b<ma):
            ma = b
    #print(mi,ma)
    if mi<=ma:
        print("YES")
    else:
        print("NO")

