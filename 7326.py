s=input()
l=len(s)
res=0
r=0
for i in range(l):
    if(s[i]=="k"):
        r+=1
    else:
        r=0
    res=max(res,r)
print(res)