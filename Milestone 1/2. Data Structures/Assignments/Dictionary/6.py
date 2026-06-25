# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
d={1:"A",2:"B",3:"C"}
for i in d:
    print(i)
for i in d.values():
    print(i)
for k,v in d.items():
    print(k,v)