n=input()
b=n[-1]
a=n[-3]
s=n[0:-4]
s1=""
for i in range(len(s)):
    if(s[i]==a):
        s1+=b
    else:
        s1+=s[i]

if(s1[0]=="0"):
    i=0
    s1 += " "
    while(s1[i]=="0" and s1[i]!=" "):
        i+=1
    if(i+1==len(s1)):
        print(0)
    else:
        print(s1[i:-1])
else:
    print(s1)
