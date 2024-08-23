a1,b1,y1=map(int,input().split())
a2,b2,y2=map(int,input().split())

c = a1 * b2 - a2 * b1
c1 = y1 * b2 - y2 * b1
c2 = a1 * y2 - a2 * y1

print("%.3f"%(c1 / c))
print("%.3f"%(c2 / c))
