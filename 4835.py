n=int(input())
j=0
for i in range (2**n):
    k=bin(i)[2:]
    dk=len(k)
    if(k.find('11')==-1):
        s=' '.join('0'*(n-dk)+k)
        print(s)
s1=str(n)*5
print('#'.join(''+s1))
