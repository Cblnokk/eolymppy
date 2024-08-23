n=int(input())
if(n==1):
    print(1)
else:
    k=1
    for i in range(1,n):
        k=k*i
    k=k*n
    print(k)
