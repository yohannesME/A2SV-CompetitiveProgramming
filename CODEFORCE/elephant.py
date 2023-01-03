pos = int(input())

#the elephant can move 5,4,3,2,1 so first move by five and when you are done just move once as what is left is done by
#1,2,3,4

if pos%5==0:
    print(pos//5)
else:
    print(pos//5 + 1)