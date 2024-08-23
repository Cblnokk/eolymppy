n=int(input())
def char(i,j):
    if(i<j):
        return "2"
    elif(i==j):
        return "0"
    else:
        return "1"
for i in range(n):
    print(''.join(reversed([char(i,j) for j in range(n)])))
