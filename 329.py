x=list(map(str,input().split()))
k=len(x)
for i in x:
    if(i=="-"):
        k-=1
print(k)

