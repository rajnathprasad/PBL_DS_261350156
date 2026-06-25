file=open("Sample.txt","r")

lines=file.readlines()

count=len(lines)

if count>12:
    time=str(count-12)+" PM"
else:
    time=str(count)+" AM"

freq={}

for line in lines:
    words=line.split()
    for word in words:
        word=word.strip(".,!?()\"'").capitalize()
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

place=max(freq,key=freq.get)

print("Meeting time:",time)
print("Meeting place:",place+" Street")

file.close()