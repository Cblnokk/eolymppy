from math import *
x1,y1,x2,y2,x3,y3=map(float,input().split())
a=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
b=sqrt(pow(x3-x2,2)+pow(y3-y2,2))
c=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
p=a+b+c
pp=p/2
s=sqrt(pp*(pp-a)*(pp-b)*(pp-c))
print("%.4f"%p,"%.4f"%s)