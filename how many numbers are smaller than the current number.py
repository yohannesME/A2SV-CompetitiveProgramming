class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            temp = 0;
            for num in nums:
                if(n > num):
                    temp = temp + 1;
            output.append(temp);
            temp = 0;
        return output;
        
