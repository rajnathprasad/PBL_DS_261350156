# Write a program to sum all the values in a dictionary, considering the values will be of int type.
d={1:10,2:20,3:30,4:40}
s=0
for i in d.values():
    s+=i
print(s)