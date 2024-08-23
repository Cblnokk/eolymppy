n=int(input())

a=list(map(int,input().split()))
b=[0]*10
for i in range(1,10):
    b[i]=a.count(i)
print(n-max(b))