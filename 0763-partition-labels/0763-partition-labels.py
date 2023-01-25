class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #declare all the last occurance of each letter
        lastIndexHash = {}
        
        #output and lenght
        output = []
        N = len(s)
        
        #get the last index
        for i in range(N):
            lastIndexHash[s[i]] = i
        
        #declare the right and left Bound of the solution
        leftBound = 0
        rightBound = N-1
        
        #move from the left
        while leftBound < N:
            #check the last index of current index occurance to the left most of all the elements it contain if that is the case then take the size of that sub array 
            #a - 0 -- first occurance
            #a - 7 -- last occurane in the middle if there is a value greater index occurance then change that right bound to that index and keep on moving
            if leftBound < lastIndexHash[s[leftBound]]:
                rightBound = lastIndexHash[s[leftBound]]
                start = leftBound
                while leftBound != rightBound:
                    leftBound += 1
                    rightBound = max(rightBound, lastIndexHash[s[leftBound]])
                output.append(rightBound-start+1)
            else:
                output.append(1)
                
            leftBound += 1
        return output