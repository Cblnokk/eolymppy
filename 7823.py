def funk(a):
    a=a[1]/a[0]
    return a
n=int(input())
t=list(map(int,input().split()))
b=list(map(int,input().split()))
sumb=sum(b)
tb=[]
v=0
for i in range (n):
    tb.append([t[i],b[i]])
tb.sort(key=funk, reverse=True)
for i in range (n):
    v+=tb[i][0]*sumb
    sumb-=tb[i][1]
print(v)