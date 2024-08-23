n,c=map(int,input().split())
sum=0
bed=0
bal=0
d=0
for i in range(n):
    a,b=map(str, input().split())
    sum+=int(a)
    if(b=="bedroom"):
        bed+=int(a)
    if(b == "balcony"):
        bal+=int(a)
    else:
        d+=int(a)
d1=d+(bal/2)
res=d1*c
print(sum)
print(bed)
print("%.1f"%res)


