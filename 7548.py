j=0
while(True):
    l, p, v=map(int,input().split())
    if(l==0 and p==0 and v==0):
        break
    else:
        res=0
        while(v>0):
            v-=p
            res+=l
        s = p - l
        if(v<0 and abs(v)>s):
            res+=v+s
        j+=1
        print("Case "+str(j)+": "+str(res))


