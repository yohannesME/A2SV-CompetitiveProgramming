import collections
n, m = [int(i) for i in input().split(' ')]
myIntHash = collections.Counter(input().split(' '))

A = input().split(' ')
B = input().split(' ')

happiness = 0

for i in range(m):
    happiness += myIntHash.get(A[i],0)
    happiness -= myIntHash.get(B[i],0)
    
print(happiness)
