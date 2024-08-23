n=int(input())
for j in range(n):
    a=list(map(str,input().split()))
    s=""
    while(s!="what does the fox say?"):
        s=input()
        if(s!="what does the fox say?"):
            b=s.split()
            k=b[2]
            for i in range(len(a)):
                if(k in a):
                    a.remove(k)
        #print(b)
    print(*a)
