# Write a program to concatenate the following dictionaries to create a new one.
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
d={}
d.update(dic1)
d.update(dic2)
d.update(dic3)
print(d)