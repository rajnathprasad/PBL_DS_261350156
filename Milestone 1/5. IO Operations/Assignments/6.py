# Write a program to count the frequency of a user entered word in a txt file.
word=input()
f=open("sample.txt","r")
c=f.read().split().count(word)
f.close()
print(c)