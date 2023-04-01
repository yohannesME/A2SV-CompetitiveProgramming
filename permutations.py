class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []

        def backtrack(bitTrack, current, N):
            if len(current) == N:
                output.append(current[:])
                return
        
            
            for index,value in enumerate(nums):
                if bitTrack & (1 << index) == 0:
                    current.append(value)
                    bitTrack |= (1 << index)
                    backtrack(bitTrack, current, N)
                    bitTrack &= ~(1 << index)

                    current.pop()
        
        backtrack(0, [], len(nums))

        return output