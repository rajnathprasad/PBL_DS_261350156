# Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    n=int(input())
    if n<2:
        print("Not Prime")
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")
except Exception:
    print("Error")