# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
try:
    name=input()
    f=open(name,"r")
    print(f.read().title())
    f.close()
except Exception:
    print("Error")