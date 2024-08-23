a,b=map(float,input().split())
n=int(input())
c=a/b
for i in range (n):
    print(i,end=' ')
print(divmod(a,b))
print(round(c,2))