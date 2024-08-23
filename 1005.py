t=int(input())


for i in range(t):
    n, m = map(int, input().split())
    if(n%(m+1)==0):
        print(2,end="")
    else:
        print(1,end="")