j=0
while(True):
    l, p, v=map(int,input().split())
    if(l==0 and p==0 and v==0):
        break
    else:
        res=(v//p)*l+min(v%p,l)
        j+=1
        print("Case "+str(j)+": "+str(res))
