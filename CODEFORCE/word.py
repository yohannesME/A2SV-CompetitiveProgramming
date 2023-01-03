import math

word = input()

N = len(word)
lowers = 0

for letter in word:
    if letter.islower():
        lowers += 1
if lowers >= math.ceil(N/2):
    print(word.lower())
else:
    print(word.upper())

