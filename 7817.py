m=int(input())
def func1(n:int):
    sum=0
    while(n>0):
        sum+=n%10
        n=n//10
    return sum

i=m
if(m>80 and m<95):
    while(func1(i)!=m):
        i+=m

print(i)








