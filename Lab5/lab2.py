Names=[x for x in input("Enter the name of the student").split()]
RollNumber=[y for y in input("Enter the Roll Number").split()]
Marks=[z for z in input("Enter the marks ").split()]
myList=list(zip(RollNumber,Names,Marks))
sortedList=sorted(myList)
print(sortedList)