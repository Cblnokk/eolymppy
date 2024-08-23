s=input()
s1="aeiou"
s2="y"
k=0
k1=0
u1=0
l=len(s)
for i in s1:
    k+=s.count(i)
k1=s.count(s2)

u=l-k-k1
while(k<=u):
    k+=1
    u-=1
    u1+=1
if u1==0 and k<=u:
    u1+=1
if u1<0:
    print(0)
else:
    print(u1)

