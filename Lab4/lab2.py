import statistics
length=int(input("Enter the number of elements of the list"))
print("Enter the elements of the list")
list=[]
for i in range(length):
    list.append(int(input("Enter each element")))
print(f"Mean is {statistics.mean(list)}")
print(f"Median is {statistics.median(list)}")
print(f"The mode of the data is {statistics.mode(list)}")
