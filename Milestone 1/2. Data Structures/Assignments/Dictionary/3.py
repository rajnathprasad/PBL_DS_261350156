# Write a program to check if a given key already exists in a dictionary.
d={1:"A",2:"B",3:"C"}
k=int(input())
if k in d:
    print("Key exists")
else:
    print("Key does not exist")