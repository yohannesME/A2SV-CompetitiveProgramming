class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #left and right bound of numbers
        leftBound = 0
        rightBound = int(math.sqrt(c))
        
        #iterate through the bounds
        while leftBound <= rightBound:
            #get the square sum
            squaresum = leftBound**2 + rightBound**2 

            #check with the given value
            if squaresum == c:
                return True
            
            #if number is greater than the given number right bound should move down else left should move up
            if squaresum > c:
                rightBound -= 1
            else:
                leftBound += 1
        
        return False