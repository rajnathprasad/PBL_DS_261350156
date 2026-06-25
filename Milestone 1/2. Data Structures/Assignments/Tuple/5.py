# Write a program to replace last value of tuples in a list to 100.
l=[(10,20,40),(40,50,60),(70,80,90)]
r=[]
for i in l:
    r.append(i[:-1]+(100,))
print(r)