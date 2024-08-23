n,k=map(int,input().split())
x=[]
l=0
for i in range(0,n):
    a,b=map(int,input().split())
    x.append([a,b])

x.sort()
for i in range(0,n):
        if(k>=x[i][0]):
            k+=x[i][1]
            l+=1


print(l)