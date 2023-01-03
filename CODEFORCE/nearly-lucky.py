from collections import Counter

num = input()

digits = Counter(num)

luckycount = 0

if '4' in digits:
    luckycount += digits['4']
if '7' in digits:
    luckycount += digits['7']

if luckycount == 4 or luckycount == 7:
    print('YES')
else:
    print('NO')
