# Write a function that takes a number as a parameter and checks whether the number is prime or not.
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input())
if prime(n):
    print("Prime")
else:
    print("Not Prime")