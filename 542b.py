e,f,c=map(int,input().split())
if(f+e==0):
    res=0
else:
    res=(e+f-1)//(c-1)
print(res)
