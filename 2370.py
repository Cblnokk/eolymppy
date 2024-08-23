n=int(input())
s=0
for c1 in range(100):
    for c2 in range(100):
                if(c1+c2==n):
                    s+=1
print(s)