n=int(input())
a=list(map(int,input().split()))
n1=int(input())
b=list(map(int,input().split()))
k=0
s=''
k1=0
for i in a:
    k=b.count(i)
    if k==0:
        s+=str(i)+" "
        k1+=1
print(k1)
print(s)
