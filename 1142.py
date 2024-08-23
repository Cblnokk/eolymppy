a,b=map(int,input().split())
if(b==0 or a%b!=0):
    print("ERROR")
else:
    print(a//b)
