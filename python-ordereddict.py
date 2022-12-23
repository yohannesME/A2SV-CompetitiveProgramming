from collections import OrderedDict

#ordered shopping catalogue
shoppingCatalogue = OrderedDict()

#the amount of purchases
itemCount = int(input())

for _ in range(itemCount):
    [name, price] = input().rsplit(' ', 1)
    price = int(price)
    
    if name in shoppingCatalogue:
        shoppingCatalogue[name] += price
    else:
        shoppingCatalogue[name] = price

#print the catalogue in the order of purchase
for name, net_price in shoppingCatalogue.items():
    print(name, net_price)
