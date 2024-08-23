s=input()
k1=s.count("f")
s1=""
if k1==0:
    print(-2)
elif k1==1:
    print(-1)
else:
    s1=s.replace("f","a",1)
    k = s1.find("f")
    print(k)
