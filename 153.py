x1,y1,x2,y2=map(float,input().split())
x3,y3,x4,y4=map(float,input().split())
if x1>x2:
    x1,x2=x2,x1
if x3 > x4:
    x3, x4 = x4, x3

if y1 > y2:
     y1, y2 = y2, y1
if y3 > y4:
     y3, y4 = y4, y3

l=max(x1,x3)
r=min(x2,x4)
ll=max(y1,y3)
rr=min(y2,y4)

if(l<r) and (ll<rr):
    s=(r-l)*(rr-ll)
else:
    s=0


print("%.3f"%s)
