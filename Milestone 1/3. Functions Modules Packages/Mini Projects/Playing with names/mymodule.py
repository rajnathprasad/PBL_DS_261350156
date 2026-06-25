def ispalindrome(name):
    if name==name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    count=0
    for i in name.lower():
        if i in "aeiou":
            count+=1
    print("No of vowels:",count)

def frequency_of_letters(name):
    freq={}
    for i in name.lower():
        if i!=" ":
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
    print("Frequency of letters:",end=" ")
    for k,v in freq.items():
        print(k+"-"+str(v),end=", ")