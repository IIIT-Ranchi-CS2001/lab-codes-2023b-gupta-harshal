import math
def calculate(i,n,x,sum):
    if(i>=n):
        return sum
    else :
        sum=sum+(((-1)**(i))*x**(2*i))/math.factorial(2*i)
        return calculate(i+1,n,x,sum)
n=int(input("Enter the numbers of terms you want"))
x=float(input("Enter the value in radians"))
print(calculate(0,n,x,0))