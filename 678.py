count=0
def kot(a,b,c):
    global count
    if(a>n):
        count+=1
        exit
    if(c==b):
        kot(a+1,b-1,c)
    else:
        if(b>0):
            kot(a+1,b-1,c)
        if(c>0):
            kot(a+1,b,c-1)


n=int(input())
kot(1,n//2,n//2)
print(count//2)




