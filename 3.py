n=int(input())
ans=0
if (n % 2 == 1):
    ans = (n // 2 + 1) * 12 + (n // 2) * 4
else:
    ans = (n // 2) * 12 + (n // 2 - 1) * 4 + 8
print(ans)