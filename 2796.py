s=input()
l=len(s)
k='0'
for i in range (1,l):
    k=max(k,s[:i]+s[i+1:])
    print(k)

print(k)
