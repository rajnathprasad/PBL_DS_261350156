# Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
s=input()
n=int(input())
print(s[-n:]*n)