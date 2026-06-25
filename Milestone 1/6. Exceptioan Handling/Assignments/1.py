# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    a=int(input())
    b=int(input())
    print(a/b)
except Exception:
    print("Error")