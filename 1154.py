import sys
for s in sys.stdin:
    a1,b1=s.split()
    b=int(b1)
    a=int(a1)
    while ((a * b) != 0):
        if (a > b):
            a = a % b
        else:
            b = b % a
    if(a + b==1):
        print("YES")
    else:
        print("NO")
