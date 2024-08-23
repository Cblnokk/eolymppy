n=int(input())
k1=1
cur=1.0
ans=0
while(k1==1):
    cur *= 2;
    ans+=1
    if(int(cur + 0.001) == n):
        break
    if(cur > n):
        cur /= 10
print(ans)
