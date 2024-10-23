names=[x for x in input("Enter name").split()]
marks=[int(y) for y in input("Enter marks").split()]
Details={}
for name,mark in zip(names,marks):
    Details[f"{name}"]=mark
high_performers=[]
mid_performers=[]
low_performers=[]
for x,y in Details.items():
    if y>=85:
        high_performers.append(x)
    elif y>=65:
        mid_performers.append(x)
    else:
        low_performers.append(x)
print(high_performers)
print(mid_performers)
print(low_performers)
Keymax = max(zip(Details.values(), Details.keys()))[1]
print(f"The student with the highest marks is {Keymax}")