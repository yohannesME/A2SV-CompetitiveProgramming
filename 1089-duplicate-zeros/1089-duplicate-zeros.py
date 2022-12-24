class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        #count of the zero inserted elements
        undiscardedElements = 0
        outOfBound = False

        
        #count how many elements will be kept when we add the zeroes
        elementCount = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                elementCount += 2
            else:
                elementCount += 1

            if elementCount >= len(arr):
                if elementCount > len(arr):
                    outOfBound = True
                undiscardedElements = i
                break
        

        #replacing pointers
        rightBound = len(arr)-1
        leftBound = undiscardedElements
        
        #temp variable to store in the case of rightBound replacing the left one
        tempLeft = -1
        
        while rightBound >= 0:
            
            #if the the last element that will remain from the original array is zero 
            #it will not be repeated.
            if leftBound == undiscardedElements and arr[leftBound] == 0 and outOfBound:
                arr[rightBound] = arr[leftBound]
                leftBound -= 1
                rightBound -= 1
                continue
                
                
            #to make sure that the zero does not replace any non zero while the pointer runs
            #make a copy of the leftBound Element
            if arr[leftBound] == 0:
                tempLeft = arr[leftBound-1]
                arr[rightBound] = 0
                rightBound -= 1
                arr[rightBound] = 0
                rightBound -= 1
            else:
                if tempLeft == -1:
                    arr[rightBound] = arr[leftBound]
                else:
                    arr[rightBound] = tempLeft
                rightBound -= 1
                tempLeft = -1
                
            leftBound -= 1
            