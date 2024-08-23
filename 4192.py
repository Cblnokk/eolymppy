n,m=map(int,input().split())
mal=0
dev=0
for i in range(n):
    a, b = map(int, input().split())
    mal+=a
    dev+=b
k1=mal/m
k2=dev/m
if(k1>int(k1)):
    k1=int(k1)+1
if(k2>int(k2)):
    k2=int(k2)+1
print(int(k1+k2))
