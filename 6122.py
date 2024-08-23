import sys
st=[]
for i in sys.stdin:
    s=list(i.split())
    if(s[0]=="push"):
        st.append(int(s[1]))
        print("ok")

    if (s[0] == "pop"):
        print(st[-1])
        st.pop()

    if(s[0]=="back"):
        print(st[-1])

    if (s[0] == "size"):
        print(len(st))

    if (s[0] == "clear"):
        st.clear()
        print("ok")

    if(s[0] == "exit"):
        print("bye")
        break
