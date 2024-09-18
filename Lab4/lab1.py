s=input("Enter the string")
list=s.split()
def isPalind(string):
    if (string==string[::-1]):
        return True
    return False
count=0
for item in list:
    if isPalind(item):
        count+=1
print(f"The number of palindrome words are {count}")