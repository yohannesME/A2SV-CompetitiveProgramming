n = int(input())

output = 0

for _ in range(n):
    bit = []
    bit[ : ] = input()
    bit = set(bit)
    for val in bit:
        if val == '+':
            output += 1
            break
        elif val == '-':
            output -= 1
            break

print(output)