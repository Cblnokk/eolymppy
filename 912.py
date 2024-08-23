s=input()
k=0
f=0
for i in s:
    if(i=="." or i=="?" or i=="!"):
        if(f==0):
            k+=1
        f=1
    elif(i!="." or i!="?" or i!="!"):
        f=0
    #print(i,f,k)
print(k)
