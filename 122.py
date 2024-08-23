x1=0
def dfs(s,b,d):
    global x1
    #print(s,b,d)
    '''if(x1>d):
        return
    if(s==b):
        x1+=1
        return
    '''
    visit[s]=1
    for u in g[s]:
        if (visit[u]==0):
            x1+=1
            print(u,x1)
            dfs(u,b,x1)



n, k, a, b, d =map(int,input().split())
g=[[] for i in range (n+1)]
for i in range(k):
    x,y=map(int,input().split())
    g[x-1].append(y - 1)

print(g)
visit=[0]*(n+1)
dfs(a,b,d)
#print(x1)
