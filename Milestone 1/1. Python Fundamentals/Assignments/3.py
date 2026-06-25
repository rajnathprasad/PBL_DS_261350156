# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
a=int(input())
b=int(input())
if a%10==b%10:
    print(True)
else:
    print(False)