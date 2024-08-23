n=int(input())
if(n<2):
    print("Ooops!")
else:
    x = list(map(int, input().split()))
    print(min(x),max(x))
