# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
f=open("sample.txt","r")
w=f.read().split()
f.close()
print(max(w,key=len))