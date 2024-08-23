n=int(input())

def d(k1):
    kor=round(k1**0.5)
    j=2
    b=k1
    res=False
    while(j<=kor and b%j>0):
        j+=1
    if(j>kor):
        res=True
    else:
        while(b%j==0):
            b//=j
        res=(b==1)
        #print(res,b)
    return res

k=1
a=1
while(k<(a+n)):
    a=k
    k=a+1
    while(k<=(a+n-1) and not d(k)):
        k+=1
print(a)


'''
1 1
2 5   +4
3 13  +8
4 19  +6
5 32  +13
6 
'''