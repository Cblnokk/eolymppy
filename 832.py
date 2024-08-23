f1 = open('input.txt')
f2 = open('output.txt','w')
n=int(f1.readline())


f2.write(str(n))
f2.close()

n=int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
a.sort(key = lambda x: x[1], reverse=True)
x=list(map(int,input().split()))

p=[0]*n
for i in range (n-1,-1,-1):
    m=0
    for j in range (i+1,n):
        if (x[i]<x[j]) and (p[j]>m):
            m=p[j]
    p[i]=m+1
k=max(p)

while k>0:
    if (p[i]==k):
        print(x[i],end=' ')
        k-=1



x=[]
for i in range(0,n):



    x.append([a,b])


x.reverse()
print(*x)


#много чисел через пробел в разных строках
import sys
s=0
for i in sys.stdin:
    for j in i.split():
        s=s+int(j)
print(s);


#алгоритм флойда
n=int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if(a[i][k]+a[k][j]<a[i][j]):
                a[i][j]=a[i][k]+a[k][j]


print("%.3f"%s)