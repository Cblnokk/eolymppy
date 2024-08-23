n=int(input())
res=0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if(i+j+k==n):
                res+=1

print(res*res)