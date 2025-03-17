s="Ba Ba Black Sheep"
print(len(s))
print(s.index('e'))
print(s.count('a'))
list=s.split()
list[0]="Ta"
list[1]="Ta"
for item in list:
    print(item,end=" ")