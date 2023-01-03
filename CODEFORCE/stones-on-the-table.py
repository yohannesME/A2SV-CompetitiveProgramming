n = int(input())

stones = input()

output = 0


for i in range(1,n):
    if stones[i-1] == stones[i]:
        output += 1
print(output)