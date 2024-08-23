a = list(map(int,input().split()))
a.sort()
if(len(a)%2!=0):
    i=(len(a))//2
    print(a[i])
else:
    print(-1)