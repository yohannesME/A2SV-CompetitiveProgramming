case = int(input())

for _ in range(case):
    num = int(input())
    # print(bin(num))
    output = 0
    for i in range(num.bit_length()):
        if num & (1 << i):
            if output > 0:
                break
            output = 1 << i
    else:
        while output & 1 == 0 or output == num:
            output += 1
    print(output)