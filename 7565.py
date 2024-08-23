n,k=map(int,input().split())
a = [[int(j) for j in input().split()] for i in range(n)]
b=[]
for i in range(n):
    b.append(a[i][0])

for i in range(b):
    for j in range(n):

print(a)
print(b)
