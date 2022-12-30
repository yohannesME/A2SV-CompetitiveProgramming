def compute(size):
    first = ''
    additional = ''
    for letter in size:
        if letter == 'X':
            additional += '.'
        elif letter == 'S':
            first = '1' + additional
            break
        elif letter == 'M':
            first = '2' + additional
            break
        elif letter == 'L':
            first = '3' + additional
            break
    return first


n = int(input())

toCompare = []

for _ in range(n):
    toCompare.append(input().split(' '))

for compare in toCompare:
    first = compute(compare[0])
    second = compute(compare[1])

    if first[0] == second[0] and first[0] == '1':

        if len(first) < len(second):
            print('>')
        elif len(first) == len(second):
            print('=')
        else:
            print('<')
        continue
    if compute(compare[0]) > compute(compare[1]):
        print('>')
    elif compute(compare[0]) == compute(compare[1]):
        print('=')
    else:
        print('<')

