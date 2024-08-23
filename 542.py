e,f,c=map(int,input().split())
ans=0
a=(e+f)//c
ans+=a
k=(e+f)%c
k+=ans
while(k>=c and k!=0):
    ans+=k//c
    k=k%c+k//c

print(ans)
