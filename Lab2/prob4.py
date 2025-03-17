s=input("Enter your name")
rn=input("Enter your roll no.")
marks=int(input("Enter your marks"))
print(f"Name : {s}")
print(f"Roll No : {rn}")
print(f"Marks : {marks}")
if marks>=90:
    grade=10
    remarks="Outstanding"
elif marks>=80:
    grade=9
    remarks="Very Good"
elif marks>=70:
    grade=8
    remarks="Good"
elif marks>=60:
    grade=7
    remarks="Average"
elif marks>=50:
    grade=6
    remarks="Pass"
else:
    grade=0
    remarks="Fail"
print(f"Grade : {grade}")
print(f"remarks: {remarks}")