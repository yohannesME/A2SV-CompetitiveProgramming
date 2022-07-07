n = m = a = 0

n = input().split()
arr = []
for str in n:
    if str.isdigit():
       arr.append(int(str)) 

n, m, a = arr
r = int(n / a)
if n % a != 0:
    r = r + 1

c = int(m / a)
if m % a != 0:
    c = c + 1

print(r * c)
