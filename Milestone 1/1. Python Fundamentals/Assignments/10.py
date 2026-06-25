# Write a program to find if the given number is palindrome or not.
n=int(input())
t=n
r=0
while t>0:
    r=r*10+t%10
    t//=10
if n==r:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")