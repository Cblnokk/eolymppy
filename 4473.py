n=int(input())
a=list(map(float,input().split()))
q=int(input())
for i in range(q):
    l,r = map(int, input().split())
    if(l>r):
        l,r=r,l
    if(max(a[l-1:r])!=int(max(a[l-1:r]))):
        print(max(a[l-1:r]))
    else:
        print(int(max(a[l - 1:r])))