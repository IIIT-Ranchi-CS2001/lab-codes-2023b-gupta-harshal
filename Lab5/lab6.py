names = [x for x in input("Enter Names :\n").split()]
salaries= [int(x) for x in input("Enter Salary:\n").split()]

dct = dict({})
for name, salary in zip(names, salaries):
    dct[name] = salary

print(dct)

mx = 0
for i in range(len(salaries)):
    mx = i
    for j in range(i, len(salaries)):
        if salaries[mx] < salaries[j]:
            mx = j
    tempM = salaries[i]
    salaries[i] = salaries[mx]
    salaries[mx] = tempM

    tempN = names[i]
    names[i] = names[mx]
    names[mx] = tempN

for (i, (name, salary)) in enumerate(zip(names, salaries)):
    print(f"{i+1}. {name} : {salary}")