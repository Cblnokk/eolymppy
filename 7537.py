n=int(input())
for i in range(n):
    m=int(input())
    ma=0
    a=[]
    for j in range(m):
        n1=int(input())
        a.append(n1)
    su=sum(a)
    ma=max(a)
    t=a.count(ma)
    if(t>1):
        print("no winner")
    else:
        if((su/2)>=ma):
            s="minority winner"
        else:
            s="majority winner"
        x=a.index(ma)
        print(s,x+1)
        

