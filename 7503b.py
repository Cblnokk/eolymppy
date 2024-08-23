n,m=map(int,input().split())
a=list(map(int,input().split()))
print(max(sum(a)//m+int(sum(a)%m!=0),max(a)))
