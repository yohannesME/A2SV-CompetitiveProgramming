from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #hash map to keep out of all the encounterd 
        #create ordered hash element of the digits
        digits = defaultdict(list)
        output = 0
        
        #enumerate all and find all occurence of that digit
        for index,digit in enumerate(nums):  
            digits[digit].append(index)

        #check if occurence is more than one and add the possible arrangement
        for occur in digits.values():
            c = len(occur)
            output += (c*(c-1))/2

        return int(output)
