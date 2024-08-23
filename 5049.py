s=input()
k = 0
l = len(s)
s1=''
for i in range(0,l):
    c = s[i]
    if (c != ' '):
        s1 += c
        k = 0;
    if (c == ' ' and k == 0):
        s1 += c
        k=1

print(s1)
