n,m=map(int,input().split())
c=m//n
if(m%n==0):
    c1=0
else:
    c1=1
#c1=m%n
print(c+c1)
