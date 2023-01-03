n = int(input())

output = 0

for _ in range(n):
    solution = list(map(int, input().split()))
    
    if sum(solution) > 1:
        output += 1


print(output)