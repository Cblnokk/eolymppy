n=int(input())
n1=str(bin(n+1))[3:]
for i in n1:
    k=int(i=='0')*'1'+int(i=='1')*'7'
    print(k,end='')

