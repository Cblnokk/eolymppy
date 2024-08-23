n=int(input())
a=list(map(int,input().split()))
b=sorted(enumerate(a,start=1),key=lambda x:(-x[1],x[0]))
for i in b:
    print(i[0],end=" ")



#print(*b)
