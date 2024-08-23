import sys
s=0
for i in sys.stdin:
    for j in i.split():
        s=s+int(j)
print(s);