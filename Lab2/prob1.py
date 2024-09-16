s1="Maha Bharat"
list=s1.split(" ")
print(s1.swapcase())
print(s1.split(" ")[0])
print(s1.split(" ")[0]*3)
list[0]="Mera"
print(f"{list[0]} {list[1]}")
list.append("Mahan")
for item in list:
    print(item,end=" ")