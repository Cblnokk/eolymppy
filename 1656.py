n=int(input())
s=set()
for i in range(n):
    n1=int(input())
    s.add(n1)

s1=list(s)
if(n%2==0):
    s1.sort(reverse=True)
else:
    s1.sort()
l=len(s1)
for i in range(l):
    print(s1[i])