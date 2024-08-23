n=int(input())
x=list(map(int,input().split()))
x1=[]
for i in range(n):
    if x[i] in x1:
        k=1
    else:
        x1.append(x[i])
print(*x1)

