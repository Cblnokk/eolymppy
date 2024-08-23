n1, m = map(int, input().split())
s=0
def d(n):
    i = 2
    while (n % i != 0 and i * i < n):
        i += 1
    if (n == 2):
        return True
    else:
        return (n % i != 0)

k=m+1
while(k<m+n1 and s!=1):
    if(d(k)):
        print(k-m-1)
        s=1
    k+=1
if(s==0):
    print(-1)

