word = input()

if word[0].isupper():
    print(word)
else:
    print(word[0].upper()+word[1:])