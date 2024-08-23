n=int(input())
t=0
for i in range(n):
    t+=int(input())

if(t>n-t):
    print(n-t)
else:
    print(t)


