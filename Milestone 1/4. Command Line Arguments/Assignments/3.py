# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
import sys

def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

s=0
for i in range(1,11):
    n=int(sys.argv[i])
    if prime(n):
        s+=n
print(s)