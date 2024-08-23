import sys
k=0
for i in sys.stdin:
    for j in i.split():
        if(k==0):
            n=j
            k=1
        elif(k==1):
            n1=j
            k=0

    print(int(n)+int(n1))


