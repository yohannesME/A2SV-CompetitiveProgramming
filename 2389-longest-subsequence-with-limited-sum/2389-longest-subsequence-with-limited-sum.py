class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        #the output generated
        output = []
        
        #to do that first sort the num
        nums.sort()
        
        #create a prefix sum to store all the possible highest values 
        prefixsum = [nums[0]]
              
        #create the prefix sum
        for i in range(1,len(nums)):
            prefixsum.append(prefixsum[-1]+nums[i])
   
        
        for query in queries:

            #go through the query and check where the prefix sum ends
            prefixLeftBound = 0
            
            while prefixLeftBound < len(prefixsum) and query >= prefixsum[prefixLeftBound]:
                prefixLeftBound += 1
            output.append(prefixLeftBound)           

        return output
            