num, rep = list(map(int, input().split()))

i  = 0
while i < rep:
    sub = num%10
    if sub == 0:
        num = num//10
    else:
        if sub <= rep-i:
            num -= sub
            i += sub-1
        else:
            num -= rep-i
            break

    i += 1


print(num)