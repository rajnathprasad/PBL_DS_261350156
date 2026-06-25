# Write a program to read contents from a txt file line by line and store each line into a list.
f=open("sample.txt","r")
l=f.readlines()
f.close()
print(l)