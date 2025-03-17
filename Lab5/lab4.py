s=input("Enter the string")
Map={}
for char in s:
    if char not in Map:
        Map[char]=0
    Map.update({char:Map.get(char)+1})
print(Map)