n=int(input("Enter a number"))
i=n
sum=0
while(n>0):
    sum+=n%10
    n=int(n/10)
print(f"Number is {i} and the sum of its digit is {sum}")