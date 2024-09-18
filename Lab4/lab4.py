ns=int(input("Enter the number of singers of class "))
singers=[]
for i in range(ns):
    singers.append(input("Enter the singer name "))
nd=int(input("Enter the number of dancers of class "))
dancers=[]
for i in range(nd):
    dancers.append(input("Enter the name of the dancers"))
set_singers=set(singers)
set_dancers=set(dancers)
print(f"Artists are {set_singers | set_dancers}")
print(f"All rounders of class are {set_singers & set_dancers}")
print(f"Dancers but not singers are {set_dancers-set_singers}")
print(f"Singers but not dancers are {set_singers-set_dancers}")
print(f"dancers but not singers cum singers but not dancers are{set_singers^set_dancers}")