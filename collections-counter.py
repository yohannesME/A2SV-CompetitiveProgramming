import collections

#output variable of all the money spent
moneySpent = 0

#input the shoe collection
N = map(int,input())
shoeSizeAvailable = list(map(int,input().split()))

#create a counter an which keeps count of all the available shoes
shoeSizeAvailable = collections.Counter(shoeSizeAvailable)

#input the purchases
purchaseSize = int(input())

for i in range(purchaseSize):
    [shoeSize, money] = list(map(int, input().split()))
    
    #if shoe is unavailable then ignore the request
    if shoeSizeAvailable[shoeSize] != 0:
        moneySpent += money
        shoeSizeAvailable[shoeSize] -= 1

print(moneySpent)
