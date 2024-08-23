a,c = map(int,input().split())
b=a
while (a%c)!=0:
    b+=1
    a=int(str(a%c)+str(b))
print(b)

