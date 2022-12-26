#input the superset and n, 
superset = set(map(int, input().split()))
n = int(input())

#varibles used for determination of superset
supersetSize = len(superset)
isSuperset = True

#input n sets
for _ in range(n):
    newset = set(map(int, input().split()))
    
    setdiff = newset.difference(superset)
    
    # if the difference is not empty and the superset and subset are 
    #are equal isSubset must be false
    if len(setdiff) == 0:
        if len(newset) == supersetSize:
            isSuperset = False
            break
    else:
          isSuperset = False
          break
        
print(isSuperset)
