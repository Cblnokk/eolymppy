s=input()
k = s.find("f")
k1 = s.rfind("f")
if k==-1:
    print()
else:
    if k==k1:
        print(k)
    else:
        print(k, k1)