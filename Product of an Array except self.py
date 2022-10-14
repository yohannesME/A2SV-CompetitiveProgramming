class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiple = 1
        output = []
        count = 0
        zero = False
        
        for num in nums:
            if num == 0:
                count += 1
                if count > 1:
                    return [0]*len(nums)
                zero = True
            else:
                multiple *= num
        
        if zero:
            for num in nums:
                if num ==0:
                    output.append(multiple)
                else:
                    output.append(0)
        else:
            for num in nums:
                output.append(multiple//num)

        return output
