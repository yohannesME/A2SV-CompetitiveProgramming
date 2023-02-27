class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        
        #handle edge case of length of two
        if N == 1:
            return 1
        
        elif N == 2:
            if arr[0] == arr[1]:
                return 1
            return 2
        
        #variables to handle        
        checker = []
        left = 0
        right = 1
        Max = 0
        
        
        while right < N:
            #move both of them if they are equal
            if arr[left] == arr[right]:
                left += 1
                right += 1

                #reinialize
                Max = max(Max, len(checker))
                checker = []
                
            elif arr[left] > arr[right]:
                if len(checker) == 0:
                    checker.append(1)
                    left += 1
                    right += 1
                elif checker[-1] == 0:
                    checker.append(1)
                    left += 1
                    right += 1
                else:
                    Max = max(Max, len(checker))
                    checker = []
                    checker.append(1)
                    left += 1
                    right += 1
            elif arr[left] < arr[right]:
                if len(checker) == 0:
                    checker.append(0)
                    left += 1
                    right += 1
                elif checker[-1] == 1:
                    checker.append(0)
                    left += 1
                    right += 1
                else:
                    Max = max(Max, len(checker))
                    checker = []
                    checker.append(0)
                    left += 1
                    right += 1
                    
        Max = max(Max, len(checker))
        
        return Max + 1