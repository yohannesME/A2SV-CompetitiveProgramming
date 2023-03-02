class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #offset the arr to force the first and last element to be evaluated
        arr = [0] + arr + [0]
        stack = []
        result = 0
        N = len(arr)


        for index in range(N):
            while stack and arr[stack[-1]] > arr[index]:
                current = stack.pop()
                #get the element range that current can be the minimum and then multiply it by that
                result += arr[current]*(index-current)*(current - stack[-1])
            
            stack.append(index)
        
        return result%(10**9+7)