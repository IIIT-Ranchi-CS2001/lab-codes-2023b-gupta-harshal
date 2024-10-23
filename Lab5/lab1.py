from math import sqrt
p1=tuple(int(x) for x in input("Enter the points ").split())
p2=tuple(int(x) for x in input("Enter the points ").split())
print(p1)
print(p2)
distance=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2
print(f"Distance between the points {p1} & {p2} is {distance}")