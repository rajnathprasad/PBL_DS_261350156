# Write a function to calculate and return the factorial of a number (a non-negative integer).
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

n=int(input())
print(fact(n))