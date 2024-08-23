n,m=map(int,input().split())
r=201
a1=[[int(0)for j in range(r)]for i in range(r)]
for i in range(m):
    a,b=map(int,input().split())
    a1[a][b]=a1[b][a]=1

k=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for j1 in range(j+1,n+1):
            if(a1[i][j]==0 and a1[i][j1]==0 and a1[j][j1]==0):
                k+=1

print(k)
