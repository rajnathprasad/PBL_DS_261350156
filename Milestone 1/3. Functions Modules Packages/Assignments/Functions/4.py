# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_case(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    print("Uppercase letters:",u)
    print("Lowercase letters:",l)

s=input()
count_case(s)