import sys
dq=[]
for i in sys.stdin:
    a=list(i.split())
    if(a[0]=="push_front"):
        dq.insert(0,a[1])
        print("ok")
    if (a[0] == "push_back"):
        dq.append(a[1])
        print("ok")
    if (a[0] == "pop_front"  and len(dq)!=0):
        print(dq[0])
        dq.pop(0)
    elif(a[0]=="pop_front" and len(dq)==0):
        print("error")
    if (a[0] == "pop_back"  and len(dq)!=0):
        print(dq[-1])
        dq.pop()
    elif (a[0] == "pop_back" and len(dq) == 0):
        print("error")
    if (a[0] == "back" and len(dq)!=0):
        print(dq[-1])
    elif (a[0] == "back" and len(dq) == 0):
        print("error")
    if (a[0] == "front"  and len(dq)!=0):
        print(dq[0])
    elif (a[0] == "front" and len(dq) == 0):
        print("error")
    if (a[0] == "size"):
        print(len(dq))
    if (a[0] == "clear"):
        dq.clear()
        print("ok")
    if(a[0] == "exit"):
        print("bye")
        break
