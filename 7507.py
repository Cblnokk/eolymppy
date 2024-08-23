n = int(input())
x = list(map(int,input().split()))
if n==3: print(x[-1]*x[-2]*x[-3])
elif(n<1000000):
    ma1=max(x);
    mi1=min(x);
    x.remove(ma1)
    x.remove(mi1)
    ma2=max(x);
    mi2=min(x);
    x.remove(ma2)
    ma3=max(x);
    print(max(mi1*mi2*ma1,ma1*ma2*ma3))
else:
    ma1 = max(x);
    mi1 = min(x);
    #x.remove(ma1)
    x.remove(mi1)
    #ma2 = max(x);
    mi2 = min(x);
    #x.remove(ma2)
    #ma3 = max(x);
    print(ma1 * mi1 * mi2)

