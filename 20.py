n=int(input())
res=0
while(n>0):
    k=n
    sum=0
    while(k>0):
        sum+=k%10
        k//=10
    n-=sum
    res+=1
print(res)