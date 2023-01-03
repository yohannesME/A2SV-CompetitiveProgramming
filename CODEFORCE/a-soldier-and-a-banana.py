k,n,w = list(map(int,input().split(' ')))

totalcost = (w/2)*(1+w)*k

additional = int(totalcost)-n

if additional <= 0:
    print(0)
else:
    print(additional)