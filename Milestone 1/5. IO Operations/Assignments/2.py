# Write a program to read first n lines from a txt file. Get n as user input.
n=int(input())
f=open("sample.txt","r")
for i in range(n):
    print(f.readline(),end="")
f.close()