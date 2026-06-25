# Write a program to count the number of upper and lower case letters in a String.
s=input()
u=0
l=0
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("Uppercase letters:",u)
print("Lowercase letters:",l)