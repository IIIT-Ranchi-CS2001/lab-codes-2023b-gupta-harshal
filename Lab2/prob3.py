def palindrome(s):
    i=0
    l=len(s)-1
    while(i<=l):
        if not (s[i]==s[l-i]):
            return False
        i+=1
    return True
s=input("Enter a string")
print(palindrome(s))