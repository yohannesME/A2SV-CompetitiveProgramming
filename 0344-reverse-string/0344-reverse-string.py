class Solution:
    def reverseString(self, s: List[str]) -> None:
        #two variable at the begining and end of the array and move inward to the array
        leftBound = 0
        rightBound = len(s)-1
        
        while leftBound < rightBound:
            #swap the two opposite side of the array
            s[leftBound], s[rightBound] = s[rightBound], s[leftBound]
            
            #increment and decrement the left and right Bound
            rightBound -= 1
            leftBound += 1