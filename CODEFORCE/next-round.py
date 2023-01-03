#accept the number of contestants and the pass
n, k = list(map(int,input().split()))

participant = list(map(int,input().split()))

if participant[k-1] < 1:
    printed = False
    for index in range(k-1, -1,-1):
        if participant[index] > 0:
            printed = True
            print(index+1)
            break
    if not printed:
        print(0)
else:
    more = 0
    for index in range(k-1,len(participant)):
        if participant[index] == participant[k-1]:
            more += 1
    print(more + k-1)