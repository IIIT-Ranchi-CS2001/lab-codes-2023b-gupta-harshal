names = [x for x in input("Enter Names :\n").split()]
roll = [x for x in input("Enter Roll No. :\n").split()]
marks = [x for x in input("Enter Marks:\n").split()]


mx = 0
for i in range(len(marks)):
    mx = i
    for j in range(i, len(marks)):
        if marks[mx] < marks[j]:
            mx = j
    tempM = marks[i]
    marks[i] = marks[mx]
    marks[mx] = tempM

    tempN = names[i]
    names[i] = names[mx]
    names[mx] = tempN

    tempR = roll[i]
    roll[i] = roll[mx]
    roll[mx] = tempR

lst = []
for i in range(len(names)):
    lst.append((names[i], roll[i], marks[i]))

print(lst)