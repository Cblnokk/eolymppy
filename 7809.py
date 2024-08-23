a=list(map(int,input().split()))
b={}
res=0
for i in a:
    if (i not in b):
        b[i] = 1
    else:
        b[i] += 1

for value in b.values():
    res+=value//2

print(res)
