n=int(input())
i=2
while(n%i!=0 and i*i<n):
    i+=1
if(n==2):
    print(True)
else:
    print(n%i!=0)