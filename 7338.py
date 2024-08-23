n=int(input())
k=0
for i in range(10,100):
    dob=n*i
    sum=(i//10)+(i%10)
    sum2=(dob//100)+(dob%10)+(dob//10)%10
    if (sum==sum2):
        k+=1
print(k)