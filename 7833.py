n=int(input())
a=list(map(int,input().split()))
ar=sum(a)/n
sum=0
k=0
for i in range(n):
    if(a[i]>ar):
        sum+=a[i]
        k+=1
print(sum,k)
