class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        
        #current even values
        evens = {}
        evensum = 0
        
        #create a sum of all even values in num and create a hash map of all element and store
        #there evenity or oddity
        for index, num in enumerate(nums):
            if num%2==0:
                evens[index] = True
                evensum += num
            else:
                evens[index] = False
        
        #go through the query and
        #if even just add to the evensum, the num and record it on the answer
        #if the num is odd just add to it the val nothing to update
        #else if it is odd there are two cases
            #if the num at the index is even then the addition of that number will make it odd and
            #that will lead to decrease the evensum, Falsify from evens and record data
            #if the number is odd another even will be contributed then evens will Trufy, evensum
            #will increase and all data will be recorded.
            
        for val, index in queries:
            
            if val%2==0:
                if evens[index]:
                    evensum+=val   
                    nums[index] += val
                else:
                    nums[index] += val
                    
            else:
                if evens[index]:
                    evensum -= nums[index]
                    evens[index] = False
                    nums[index] += val
                else:
                    nums[index] += val
                    evens[index] = True
                    evensum += nums[index]
                    
            answer.append(evensum)
        
        return answer