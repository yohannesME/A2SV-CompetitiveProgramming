test = int(input())

def checker(mid, contestant, lowestCount):
    return mid*4 <= contestant and lowestCount >= mid

for t in range(test):
    programmer, mathimatician = list(map(int, input().split()))

    lowestCount = min(programmer, mathimatician)
    contestant  = programmer + mathimatician

    left = 0
    right = (programmer + mathimatician)//4

    while left < right:
        mid = left + (right-left)//2

        if not checker(mid, contestant, lowestCount):
            right = mid
        else:
            left = mid + 1
    print(left if checker(left, contestant, lowestCount) else left - 1)
