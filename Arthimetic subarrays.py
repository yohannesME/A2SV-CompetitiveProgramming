class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        answer = []
        for i in range(len(l)):
            lst = nums[l[i]:r[i]+1]
            isNot = True
            lst.sort()
            val = lst[0]-lst[1]

            for j in range(len(lst)-1):
                if((lst[j]-lst[j+1]) != val):
                    isNot = False
            answer.append(isNot)
        return answer
            
            
        
