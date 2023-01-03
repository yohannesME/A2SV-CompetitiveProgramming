word = input()
revword = input()


if ''.join(reversed(word[:])) == revword:
    print('YES')
else:
    print('NO')