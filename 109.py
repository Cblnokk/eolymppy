n=int(input())
i=1
a=1
b=10
while(n > 0):
    if (i < b):
        n = n - a
    if (i == b - 1):
        a+=1
        b = b * 10
    if (n == 0):
        print(i)
    elif (n < 0):
        print(0)
    i+=1

