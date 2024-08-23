s=input()
a=[]
l=len(s)
k=0
for i in range(l):
    a.append(int(s[i]))
    if(s[i]=="0"):
        k+=1
if(k==l):
    print(0)
else:
    a.sort()
    f=0
    s1=""
    s2=""
    for i in range(l):
        if(a[i]==0 and f==0):
            s1+=""
        else:
            f=1
            s1+=str(a[i])
    a.reverse()
    for i in range(l):
        s2+=str(a[i])
    print(int(s1)+int(s2))