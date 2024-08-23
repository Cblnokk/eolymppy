n=int(input())
for i in range(1,n+1):
    k=0
    for j in range(1,n+1):
        if (n-i+1== j):
            print(0, end="")
            k=1
        else:
            if(k==0):
                print(2, end="")
            elif(k==1):
                print(1, end="")


    print()


