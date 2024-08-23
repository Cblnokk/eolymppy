s=input()
n= len(s)
a=[0]*n
f=False
n1=0

for i in range(n):
    if(s[i]=='1'):
        n1+=1

if(n1==n):
    print(0)
else:
    for i in range(n):
        if (int(s[i]) % 2) == 0:
            a[i]=(int(s[i])+1)
        elif (int(s[i]) % 2) == 1:
            a[i]=(int(s[i])-1)

    for i in range(n):
        if a[i]==0 and f==True:
          print(a[i],end="")
        elif a[i]!=0:
           print(a[i], end="")
           f=True
