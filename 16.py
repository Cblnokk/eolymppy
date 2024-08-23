s,k,a,b=map(int,input().split())
res=-1
if(s*a==b):
    res=s*k
else:
    for n in range(s*k):
        if((a*s-b)%(s*k-n)==0 and (s*a-b)*(s*k-n)>0 and (n-k*s)*(n*a-b*k)>0):
            res=n
            break
print(res)