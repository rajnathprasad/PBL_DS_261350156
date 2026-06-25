# Write a program to accept input from user and append it to a txt file.
s=input()
f=open("sample.txt","a")
f.write(s+"\n")
f.close()