s=input()
if(len(s)%2==0):
    print("no")
else:
    f=0
    n = len(s)//2
    s1=s[0:n]
    s2=s1[::-1]
    s3=s1+s2
    for i in range(len(s)-1):
        if(s[i]!=s3[i] and f==0):
            res=s[:i]+s[i+1:]
            f=1
    if(f==0):
        res=s[:(len(s)-1)]
    if(res==s3):
        print("yes")
        print(s3)
    else:
        print("no")
    #print(res,s3)