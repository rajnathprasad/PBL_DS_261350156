import sys

like=sys.argv[1].split("-")
dislike=sys.argv[2].split("-")
given=sys.argv[3].split("-")

happiness=0

for i in given:
    if i in like:
        happiness+=1
    elif i in dislike:
        happiness-=1

print("Final happiness is",happiness)