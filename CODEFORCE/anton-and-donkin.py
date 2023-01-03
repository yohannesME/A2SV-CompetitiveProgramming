from collections import Counter

n = input()

match = Counter(input())

if match['A'] > match['D']:
    print('Anton')
elif match['A'] < match['D']:
    print('Danik')
else:
    print('Friendship')