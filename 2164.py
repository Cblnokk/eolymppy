s=input()
n=int(input())
s1=''
for i in s:
    k=ord(i)
    c=k-n
    if c<65:
        c+=26
    s1+=chr(c)



print(s1)