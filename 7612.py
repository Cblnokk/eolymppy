h,w=map(int,input().split())
if(w<h):
    h,w=w,h
if(w>3*h):
    a1=h
else:
   a1=max(h/2,w/3)


print("%.3f"%a1)


