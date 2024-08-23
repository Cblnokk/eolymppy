s=input()
s1=''
for i in s:
    if(i.isdigit()):
        s1+=i
n=len(s)
s1=s1[::-1]
a=[set()]*n
a[0]={s1[0]}
for i in range(1,n):
    a[i]=a[i-1] | {s1[i]}
b=set(s1)
while(len(b)>0):
    k='0'
    for i in range(n-1,-1,-1):
        if(b==a[i] and (s1[i] in b) and s1[i]>k):
            k=s1[i]
            n=i
    print(k,end="")
    b-={k}
    for i in range(n):
        a[i]=a[i]-{k}
#print(len(b))


