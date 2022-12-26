from collections import defaultdict

n, m = list(map(int, input().split()))
A = defaultdict(list)

#input the first array of A element
for i in range(n):
    letter = input()
    A[letter].append(i+1)

#input the second array of B elements and map them to the first
for i in range(m):
    letter = input()
    if letter in A:
        print(*A[letter])
    else:
        print(-1)


