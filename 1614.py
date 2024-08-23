import math
from math import *
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
b=sqrt(pow(x3-x2,2)+pow(y3-y2,2))
c=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
res1=acos((pow(a,2)+pow(b,2)-pow(c,2))/(2*a*b))
res2=acos((pow(b,2)+pow(c,2)-pow(a,2))/(2*c*b))
res3=acos((pow(a,2)+pow(c,2)-pow(b,2))/(2*a*c))
ma=max(res1,res2,res3)
n=(ma*180)/math.pi
print("%.6f"%n)
