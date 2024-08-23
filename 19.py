s=input()
d=len(s)
k=0
if(d%2==1):
    k+=1
for i in range(d//2):
    if(s[i]==s[d-i-1]):
        k+=1
print(k)