limak, bob = list(map(int, input().split()))

for i in range(10):
    bob *= 2
    limak *= 3
    if limak > bob:
        print(i+1)
        break
