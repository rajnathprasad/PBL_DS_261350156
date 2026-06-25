# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
l=[10,-5,20,-8,15,-2,30,-1,40,-9]
try:
    i=int(input())
    if l[i]>=0:
        print("Positive")
    else:
        print("Negative")
except Exception:
    print("Error")