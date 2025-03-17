import sys
def my_max(arg):
    max_val=-10e9
    for i in arg:
        if(i>max_val):
            max_val=i
    return max_val
tup=(1,4,6,2,8)
setval={5,3,7,8,1}
list=[6,3,2,1]
print(my_max(tup))
print(my_max(setval))
print(my_max(list))