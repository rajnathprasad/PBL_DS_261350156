# Write a program to reverse a given number and print.
n=int(input())
r=0
while n>0:
    r=r*10+n%10
    n//=10
print(r)