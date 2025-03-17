from math import sqrt
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
d=b**2-4*a*c
if(d==0):
    print(f"Roots are same and is {-b/(2*a)}")
elif d>0:
    print(f"Roots are distinct and are r1={(b*-1+sqrt(d))/2*a} and r2={(b*-1-sqrt(d))/2*a}")
else:
    print(f"Real part is {(b*-1)/(2*a)} and imaginary part is {sqrt(d*-1)/(2*a)}")

