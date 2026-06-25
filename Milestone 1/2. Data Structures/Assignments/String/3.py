# Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.
s=input()
print(s[:2]*len(s))