class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #create a map of the elements
        numHash = {}
        
        #populate the hash map
        for index,value in enumerate(arr):
            numHash[str(value)] = index
            
        #look for the double
        for index, value in enumerate(arr):
            if value//2 == value/2 and str(value//2) in numHash:
                if index != numHash[str(value//2)]:
                    return True
        
        return False
        