l=int(input("Enter the length of the lists"))
course_code=[]
course_name=[]
for i in range(l):
    course_name.append(input("Enter the name of the course"))
    course_code.append(input("Enter the course code of the course"))
list=list(zip(course_name,course_code))
print(list)