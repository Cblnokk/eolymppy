s=input()
s1=input()
s2=''
for i in s:
    c=ord(i)-65
    if(c<0 or c>32):
        s2+=i
    else:
        #print(s1[c])
        s2+=s1[c]
print(s2)