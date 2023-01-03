n = int(input())

maximum = 0

first = 0

for _ in range(n):
    coming = list(map(int,input().split()))
    current = first-coming[0]+coming[1]
    maximum = max(maximum, current)
    first = current

print(maximum)