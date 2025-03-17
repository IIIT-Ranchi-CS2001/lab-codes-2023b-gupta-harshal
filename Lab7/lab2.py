def myzip(name, id, point, strct= False):
    if strct:
        if len(name) == len(id) and len(id) == len(point):
            pass
        else:
            return "Unequal Lengths"
    return list(zip(name, id, point))

def my_sort(lst, ke = 0):
    mx = 0
    for i in range(len(lst)):
        mx = i
        for j in range(i, len(lst)):
            if lst[mx] < lst[j]:
                mx = j
        tempM = lst[i]
        lst[i] = lst[mx]
        lst[mx] = tempM
    return lst

print(myzip(["aakri", "utk", "ras"], ["122", "123"], [122, 1234]))
print(my_sort(myzip(["aakri", "utk", "ras"], ["142", "123"], [1239, 1234]), 2))